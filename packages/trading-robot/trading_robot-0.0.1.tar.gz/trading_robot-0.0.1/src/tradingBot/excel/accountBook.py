import xlwings as xw
import pandas as pd
import math
import numpy as np
from datetime import time, date, datetime, timedelta
from pytz import timezone
import pandas_ta as ta
import pymannkendall as mk
import mibian

from tradingBot.consts import RGB
from tradingBot.consts import strategy as st
from tradingBot.consts import asset as at

from tradingBot.excel import positionSheet as ps
from tradingBot.excel import acctPositionSheet as aps
from tradingBot.excel import transactionSheet as trxs
from tradingBot.settings.tradeConfig import entryCrit, riskManager, marketCondition, runtimeConfig

from tradingBot.optionPosition import single_leg as sl 
from tradingBot.optionPosition import spread as sp
from tradingBot.optionPosition import iron_condor as ic
from tradingBot.optionPosition import butterfly as bf   

from tradingBot.utils.dataGetter import get_price_history
from tradingBot.utils.dataGetter import get_next_earning_date
from tradingBot.utils.dataGetter import get_option_chain

import uuid

import logging

logger = logging.getLogger('accountBook')

class accountBook():

    def __init__(self, 
                file_path=None, 
                entry_crit=entryCrit(),
                runtime_config=runtimeConfig(),
                market_condition=marketCondition(), 
                risk_mgr=riskManager(), 
                strategy_list=[]):

        self.file_path = file_path
        if file_path == None:
            self.wb = xw.Book()
        else:
            self.wb = xw.Book(file_path) 

        self.entry_crit = entry_crit
        self.runtime_config = runtime_config
        self.market_condition = market_condition
        self.risk_mgr = risk_mgr
        self.strategy_list = strategy_list   
        self.single_option_list = []     
        self.spread_option_list = []
        self.butterfly_option_list = []
        self.condor_option_list = []

        if file_path == None: # new open            
            self.option_summary_sheet = ps.positionSheet(self.wb, sheet_name='option summary')     
            self.acct_position_sheet = aps.acctPositionSheet(self.wb, sheet_name='position')               
            self.transaction_sheet = trxs.transactionSheet(self.wb, sheet_name='transaction')                        
            self.acct_position_sheet.update_cell(self.acct_position_sheet.INIT_BALANCE, 2, value= runtime_config.init_balance, font_bold=True)             
            self.cash_position =  self.update_cash_position(runtime_config.init_balance)
            self.margin_position =  self.update_margin_position(0)            
        else:
            self.option_summary_sheet = ps.positionSheet(self.wb, sheet_name='option summary', create=False)     
            self.acct_position_sheet = aps.acctPositionSheet(self.wb, sheet_name='position', create=False)               
            self.transaction_sheet = trxs.transactionSheet(self.wb, sheet_name='transaction', create=False)                           
            self.cash_position = self.get_cash_position()
            self.margin_position = self.get_margin_position()                

        for strategy in strategy_list:
            if strategy in [st.LONG_CALL, st.LONG_PUT, st.COVERED_CALL, st.SHORT_PUT]:
                self.single_option_list.append(strategy)
            elif strategy in [st.CREDIT_CALL_SPREAD, st.CREDIT_PUT_SPREAD, st.DEBIT_CALL_SPREAD, st.DEBIT_PUT_SPREAD]:
                self.spread_option_list.append(strategy)
            elif strategy in [st.CREDIT_CALL_BUTTERFLY, st.CREDIT_PUT_BUTTERFLY, st.DEBIT_CALL_BUTTERFLY, st.DEBIT_PUT_BUTTERFLY, st.IRON_BUTTERFLY, st.REVERSE_IRON_BUTTERFLY]:
                self.butterfly_option_list.append(strategy)
            elif strategy in [st.CREDIT_IRON_CONDOR, st.DEBIT_IRON_CONDOR]:
                self.condor_option_list.append(strategy)        
 
################ actions #################
    def run(self, watch_list):                     
        self.update_all_strategy_positions()   
                
        self.try_open_new_strategy_positions(watch_list) 

    def pick_asset_candidates(self, watch_list):
        df = watch_list.loc[ watch_list['Rating'].empty == False and watch_list['Rating'] <= self.entry_crit.max_rating]
        return df  
            
    def pick_strategy_candidates(self, candiates):

        symbol_list = candiates['Symbol'].to_list()        
        per_symbol_list = pd.DataFrame()  # one per symbol

        for symbol in symbol_list:           
    
            dfi = dfs = dfb = dfp = pd.DataFrame()

            if len(self.condor_option_list) > 0:
                q = ic.iron_condor_position(symbol, self.entry_crit, self.runtime_config)
                dfi = q.get_positions(self.condor_option_list)

            if len(self.single_option_list) > 0:
                q = sl.single_leg_position(symbol, self.entry_crit, self.runtime_config)
                dfs = q.get_positions(self.single_option_list)
  
            if len(self.spread_option_list) > 0:
                q =sp.spread_position(symbol, self.entry_crit, self.runtime_config)
                dfp = q.get_positions(self.spread_option_list)
        
            if len(self.butterfly_option_list) > 0:
                q =bf.butterfly_position(symbol, self.entry_crit, self.runtime_config)
                dfb = q.get_positions(self.butterfly_option_list)

            df = pd.concat([dfi, dfs, dfb, dfp], axis=0)        

            logger.debug('pick_option_candidates %s get %d' % (symbol, df.shape[0]))

            if df.shape[0] > 0:
                df = df.sort_values(by = 'PNL')
                per_symbol_list = per_symbol_list.append(df.tail(1))

        return per_symbol_list


    def try_open_new_strategy_positions(self, watch_list):
        df = self.option_summary_sheet.to_df()
        self.active_option_count = len(df[df[self.option_summary_sheet.STATUS_t] == at.OPENED])
        if self.active_option_count > self.risk_mgr.max_option_positions:
            logger.info('Active option count %d exceeded max option position %d' % 
                (self.active_option_count, self.risk_mgr.max_option_positions))
            return        
        asset_candiates = self.pick_asset_candidates(watch_list)
        per_symbol_candiates = self.pick_strategy_candidates(asset_candiates)
        self.pick_and_open_strategy_positions(per_symbol_candiates)
        return

    def pick_and_open_strategy_positions(self, candidates):       
        for index, opt in candidates.iterrows():  

            #if self.cash_position < self.risk_mgr.min_cash_position:
            #    logger.info('Cash level %.2f lower than max per position %.2f' % (self.cash_position, self.risk_mgr.max_risk_per_position))
            #    return            

            q = self.risk_mgr.max_loss_per_position // (opt.MAX_LOSS * 100)
            if q == 0:
               logger.info('max loss %.2f exceeded max per position risk %.2f' % (opt.MAX_LOSSS, self.risk_mgr.max_option_positions))
               continue

            if math.isnan(opt.MARGIN) == False:             
                margin =  (q * 100 * opt.MARGIN)
                cash =  (q * 100 * opt.OPEN_PRICE)
                self.margin_position += margin
                self.cash_position += (cash - margin)              
                self.update_margin_position(self.margin_position)  
            else:
                self.cash_position = self.cash_position - (q * 100 * opt.OPEN_PRICE)

            self.update_cash_position(self.cash_position)                

            self.open_new_strategy_position(opt, q)       

            self.active_option_count = self.active_option_count + 1

            if self.active_option_count > self.risk_mgr.max_option_positions:
                logger.info('Active option count %d exceeded max option position %d' % 
                    (self.active_option_count, self.risk_mgr.max_option_positions))
                return
        

    def open_new_strategy_position(self, op, q):

        UUID = uuid.uuid4().hex
        self.map_to_option_summary_sheet(op, q, UUID)    
        strategy = op.STRATEGY          

        if   strategy == st.LONG_CALL or\
             strategy  ==  st.LONG_PUT or\
             strategy  ==  st.COVERED_CALL or\
             strategy  ==  st.SHORT_PUT:
             self.map_1legs_option(op, q, UUID)
        elif strategy ==  st.CREDIT_CALL_SPREAD or\
             strategy == st.CREDIT_PUT_SPREAD or\
             strategy ==  st.DEBIT_CALL_SPREAD or\
             strategy ==  st.DEBIT_PUT_SPREAD:
             self.map_2legs_option(op, q, UUID)            
        elif strategy ==  st.CREDIT_IRON_CONDOR or\
             strategy == st.DEBIT_IRON_CONDOR or\
             strategy == st.IRON_BUTTERFLY or\
             strategy == st.REVERSE_IRON_BUTTERFLY:              
             self.map_4legs_option(op, q, UUID)
        elif strategy == st.CREDIT_CALL_BUTTERFLY or\
             strategy ==  st.DEBIT_CALL_BUTTERFLY or\
             strategy == st.CREDIT_PUT_BUTTERFLY or\
             strategy == st.DEBIT_PUT_BUTTERFLY:   
             self.map_3legs_option(op, q, UUID)                              
        else:
            logger.error('open_new_strategy_position Unknown strategy %s' %strategy)                        

        return    
    
    def update_all_strategy_positions(self):
        sheet = self.option_summary_sheet                                   
        df = sheet.to_df()                             

        today = datetime.now().astimezone(timezone(at.TIMEZONE)).date()        

        symbol_list = df[sheet.SYMBOL_t].unique()               
        for symbol in symbol_list:
            logger.info('Updating %s' % symbol)                                
            dfs = df[df[sheet.SYMBOL_t] == symbol]          
            data, trend, option_chain = self.init_data(symbol)                                                      
            for rid in dfs.index:          
                row = df.iloc[rid]    

                if row[sheet.STATUS_t] != at.OPENED:
                    continue

                uid = rid+2 
                exp_date = row[sheet.EXP_DATE_t].tz_localize(timezone(at.TIMEZONE)).date()
                days_to_expire = (exp_date - today).days               
        
                if days_to_expire <= 0:
                    exp_stock_price = data['Close'][row[sheet.EXP_DATE_t].tz_localize(data.index[-1].tz)]                     
                    self.close_one_expired_strategy_position(uid, exp_stock_price, row)          
                else: # get current PNL
                    stock_price = data['Close'][-1]
                    self.update_one_strategy_position(uid, stock_price, trend, option_chain, row)
 
    def update_one_strategy_position(self, uid, stock_price, x, option_chain, row):            

        sheet = self.option_summary_sheet     
        today = datetime.now().astimezone(timezone(at.TIMEZONE)).date()
        exp_date = row[sheet.EXP_DATE_t].tz_localize(timezone(at.TIMEZONE)).date()
        days_to_expire = (exp_date - today).days  
        if days_to_expire <= self.risk_mgr.close_days_before_expire:
            font_color = RGB.RED                                                                                       
        else:
            font_color = RGB.BLACK
        sheet.update_cell(sheet.EXP_DATE, uid, font_color=font_color)
        if isinstance(row[sheet.EARNING_DATE_t], pd.Timestamp) != False:                           
            earning_date = row[sheet.EARNING_DATE_t].tz_localize(timezone(at.TIMEZONE)).date()                     
            days_to_earning = (earning_date-today).days
            if days_to_earning  <= self.risk_mgr.close_days_before_earning:
                font_color = RGB.RED                                                                                       
            else:
                font_color = RGB.BLACK                
            sheet.update_cell(sheet.EARNING_DATE, uid, font_color=font_color)
                             
        call_opt = option_chain(exp_date.strftime("%Y-%m-%d")).calls                                                   
        put_opt = option_chain(exp_date.strftime("%Y-%m-%d")).puts                                        
        strategy = row[sheet.STRATEGY_t]    
        open_price = row[sheet.OPEN_PRICE_t]
        if strategy == st.LONG_CALL or strategy == st.COVERED_CALL:
            if strategy == st.LONG_CALL:
                strike =  row[sheet.P1LK_t]
            else:
                strike =  row[sheet.P1SK_t]                       
            op = call_opt.loc[call_opt['strike']==strike]                          
            last_price = self.ov(op)      
            if strategy == st.LONG_CALL:
                row[sheet.P1LP_t] = last_price                
                gain = last_price - open_price
            else:
                row[sheet.P1SP_t] = last_price                           
                gain = open_price - last_price

            if math.isnan(last_price) == False and days_to_expire > 0:
                c = mibian.BS([stock_price, strike, 0.05, days_to_expire], callPrice=last_price)
                c = mibian.BS([stock_price, strike, 0.05, days_to_expire], volatility = c.impliedVolatility)            
                last_delta = c.callDelta
            else:
                last_delta = np.nan
        elif strategy == st.LONG_PUT or strategy == st.SHORT_PUT:
            if strategy == st.LONG_PUT:
                strike =  row[sheet.P1LK_t]
            else:
                strike =  row[sheet.P1SK_t]                              
            op = put_opt.loc[put_opt['strike']==strike]                          
            last_price = self.ov(op)         
            
            if strategy == st.LONG_PUT: 
                row[sheet.P1LP_t] = last_price                       
                gain = last_price - open_price
            else:
                row[sheet.P1SP_t] = last_price                       
                gain = open_price - last_price
                
            if math.isnan(last_price) == False and days_to_expire > 0:
                p = mibian.BS([stock_price, strike, 0.05, days_to_expire], putPrice= last_price)
                p = mibian.BS([stock_price, strike, 0.05, days_to_expire], volatility= p.impliedVolatility)
                last_delta = p.putDelta
            else:
                last_delta = np.nan
        elif strategy == st.DEBIT_CALL_SPREAD or\
                strategy == st.CREDIT_CALL_SPREAD or\
                strategy == st.DEBIT_PUT_SPREAD or\
                strategy == st.CREDIT_PUT_SPREAD:
            strike_L = row[sheet.P1LK_t]
            strike_S = row[sheet.P1SK_t]
            if strategy == st.DEBIT_CALL_SPREAD or strategy == st.CREDIT_CALL_SPREAD:                          
                op_L = call_opt.loc[call_opt['strike']==strike_L]     
                op_S = call_opt.loc[call_opt['strike']==strike_S]
            else:
                op_L = put_opt.loc[put_opt['strike']==strike_L]     
                op_S = put_opt.loc[put_opt['strike']==strike_S]                          
            lp = self.ov(op_L)
            sp = self.ov(op_S)
            
            row[sheet.P1SP_t] = sp
            row[sheet.P1LP_t] = lp   

            if strategy == st.CREDIT_CALL_SPREAD or strategy == st.CREDIT_PUT_SPREAD:
                last_price = sp - lp                                   
                gain = open_price - last_price
                sdp = sp
                op = op_S
            else:
                last_price = lp - sp
                gain = last_price - open_price 
                sdp = lp
                op = op_L
                
            if math.isnan(sdp) == False and days_to_expire > 0:                          
                if strategy == st.CREDIT_CALL_SPREAD:
                    c = mibian.BS([stock_price, strike_S, 0.05, days_to_expire], callPrice=sdp)
                    c = mibian.BS([stock_price, strike_S, 0.05, days_to_expire], volatility = c.impliedVolatility)
                    last_delta = c.callDelta    
                    logger.debug('%s strike %.2f days to expire %d, price %.2f delta %.2f' % (strategy, strike_S, days_to_expire, sdp, last_delta))                    
                elif strategy == st.DEBIT_CALL_SPREAD:
                    c = mibian.BS([stock_price, strike_L, 0.05, days_to_expire], callPrice=sdp)
                    c = mibian.BS([stock_price, strike_L, 0.05, days_to_expire], volatility = c.impliedVolatility)
                    last_delta = c.callDelta
                    logger.debug('%s strike %.2f days to expire %d, price %.2f delta %.2f' % (strategy, strike_L, days_to_expire, sdp, last_delta))                                        
                elif strategy == st.CREDIT_PUT_SPREAD:
                    p = mibian.BS([stock_price, strike_S, 0.05, days_to_expire], putPrice=sdp)
                    p = mibian.BS([stock_price, strike_S, 0.05, days_to_expire], volatility = p.impliedVolatility)
                    last_delta = p.putDelta 
                    logger.debug('%s strike %.2f days to expire %d, price %.2f delta %.2f' % (strategy, strike_S, days_to_expire, sdp, last_delta))                                        
                else:
                    p = mibian.BS([stock_price, strike_L, 0.05, days_to_expire], putPrice=sdp)
                    p = mibian.BS([stock_price, strike_L, 0.05, days_to_expire], volatility = p.impliedVolatility)
                    last_delta = p.putDelta                     
                    logger.debug('%s strike %.2f days to expire %d, price %.2f delta %.2f' % (strategy, strike_L, days_to_expire, sdp, last_delta))                                                            
            else:
                last_delta = np.nan
                
        elif strategy == st.CREDIT_IRON_CONDOR or\
                strategy == st.DEBIT_IRON_CONDOR:
            p_strike_L = row[sheet.P1LK_t]
            p_strike_S = row[sheet.P1SK_t]
            c_strike_L = row[sheet.P2LK_t]
            c_strike_S = row[sheet.P2SK_t]
                                  
            p_op_L = put_opt.loc[put_opt['strike']==p_strike_L]     
            p_op_S = put_opt.loc[put_opt['strike']==p_strike_S]
            c_op_L = call_opt.loc[call_opt['strike']==c_strike_L]     
            c_op_S = call_opt.loc[call_opt['strike']==c_strike_S]                          
            
            p_lp = self.ov(p_op_L)
            p_sp = self.ov(p_op_S)
            c_lp = self.ov(c_op_L)
            c_sp = self.ov(c_op_S)
            
            row[sheet.P1SP_t] = p_sp
            row[sheet.P1LP_t] = p_lp   
            row[sheet.P2SP_t] = c_sp
            row[sheet.P2LP_t] = c_lp   
            
            if strategy == st.CREDIT_IRON_CONDOR:
                last_price = (p_sp - p_lp) + (c_sp - c_lp)
                gain = open_price - last_price
                sdp = p_sp
                op = p_op_S
            else:
                last_price = (p_lp - p_sp) + (c_lp - c_sp)
                gain = last_price - open_price 
                sdp = p_lp
                op = p_op_L
                
            if math.isnan(sdp) == False and days_to_expire > 0:                          
                p = mibian.BS([stock_price, p_strike_S, 0.05, days_to_expire], putPrice=sdp)
                p = mibian.BS([stock_price, p_strike_S, 0.05, days_to_expire], volatility = p.impliedVolatility)
                last_delta = p.putDelta
                logger.debug('%s sk %.2f oprice %.2f' % (strategy, p_strike_S, sdp))
            else:
                last_delta = np.nan

        elif strategy == st.CREDIT_CALL_BUTTERFLY or\
                strategy == st.DEBIT_CALL_BUTTERFLY or\
                strategy == st.CREDIT_PUT_BUTTERFLY or\
                strategy == st.DEBIT_PUT_BUTTERFLY or\
                strategy == st.IRON_BUTTERFLY or\
                strategy == st.REVERSE_IRON_BUTTERFLY:
            
            p1_strike_L = row[sheet.P1LK_t]
            p1_strike_S = row[sheet.P1SK_t]
            p2_strike_L = row[sheet.P2LK_t]
            p2_strike_S = row[sheet.P2SK_t]
              
            if strategy == st.CREDIT_CALL_BUTTERFLY or strategy == st.DEBIT_CALL_BUTTERFLY:    
                p1_op_L = call_opt.loc[call_opt['strike']==p1_strike_L]     
                p1_op_S = call_opt.loc[call_opt['strike']==p1_strike_S]
                p2_op_L = call_opt.loc[call_opt['strike']==p2_strike_L]     
                p2_op_S = call_opt.loc[call_opt['strike']==p2_strike_S]   
            elif strategy == st.CREDIT_PUT_BUTTERFLY or strategy == st.DEBIT_PUT_BUTTERFLY:
                p1_op_L = put_opt.loc[put_opt['strike']==p1_strike_L]     
                p1_op_S = put_opt.loc[put_opt['strike']==p1_strike_S]
                p2_op_L = put_opt.loc[put_opt['strike']==p2_strike_L]     
                p2_op_S = put_opt.loc[put_opt['strike']==p2_strike_S]                 
            else: # condor
                p1_op_L = put_opt.loc[put_opt['strike']==p1_strike_L]     
                p1_op_S = put_opt.loc[put_opt['strike']==p1_strike_S]
                p2_op_L = call_opt.loc[call_opt['strike']==p2_strike_L]     
                p2_op_S = call_opt.loc[call_opt['strike']==p2_strike_S]                  
            
            p1_lp = self.ov(p1_op_L)
            p1_sp = self.ov(p1_op_S)
            p2_lp = self.ov(p2_op_L)
            p2_sp = self.ov(p2_op_S)

            row[sheet.P1SP_t] = p1_sp
            row[sheet.P1LP_t] = p1_lp   
            row[sheet.P2SP_t] = p2_sp
            row[sheet.P2LP_t] = p2_lp            
            
            if strategy == st.CREDIT_CALL_BUTTERFLY or\
                strategy == st.CREDIT_PUT_BUTTERFLY or\
                strategy == st.REVERSE_IRON_BUTTERFLY:
                logger.debug('%s p1_sp %.2f p1_lp %.2f p2_sp %.2f p2_lp %.2f' %
                         (strategy, p1_sp, p1_lp, p2_sp, p2_lp))
                last_price = abs((p1_sp - p1_lp) + (p2_sp - p2_lp))               
                gain = open_price - last_price
                sdp = p1_lp
                op = p1_op_L
                strike = p1_strike_L 
                logger.debug('%s price for delta %.2f' %(strategy, sdp))
            else:
                logger.debug('%s p1_sp %.2f p1_lp %.2f p2_sp %.2f p2_lp %.2f' %
                         (strategy, p1_sp, p1_lp, p2_sp, p2_lp))                
                last_price = abs((p1_lp - p1_sp) + (p2_lp - p2_sp))
                gain = last_price - open_price 
                sdp = p1_sp
                op = p1_op_S
                strike = p1_strike_S
                logger.debug('%s price for delta %.2f' %(strategy, sdp))                
                                 
            
            if math.isnan(sdp) == False and days_to_expire > 0:            
                if strategy == st.CREDIT_CALL_BUTTERFLY or strategy == st.DEBIT_CALL_BUTTERFLY:
                    c = mibian.BS([stock_price, strike, 0.05, days_to_expire], callPrice=sdp)
                    c = mibian.BS([stock_price, strike, 0.05, days_to_expire], volatility = c.impliedVolatility)
                    last_delta = c.callDelta        
                    logger.debug('%s sk %.2f days %d op %.2f delta %.2f' %(strategy, strike, days_to_expire, sdp, last_delta))
                else:
                    p = mibian.BS([stock_price, strike, 0.05, days_to_expire], putPrice=sdp)
                    p = mibian.BS([stock_price, strike, 0.05, days_to_expire], volatility = p.impliedVolatility)
                    last_delta = p.putDelta                    
                    logger.debug('%s sk %.2f days %d op %.2f delta %.2f' %(strategy, strike, days_to_expire, sdp, last_delta))                                        
            else:
                last_delta = np.nan
        else:
            logger.error('update_one_strategy_position Unknown strategy %s' % strategy)
            return

        pl = gain
        gain = 100 * gain / open_price                   
        if gain > 0:
            font_color = RGB.SEA_GREEN
        else:
            font_color = RGB.RED                                                                                         

        sheet.update_cell(sheet.PL, uid, font_color=font_color, value = "{:.2f}".format(pl))        
        sheet.update_cell(sheet.GAIN, uid, font_color=font_color, value = "{:.2f}".format(gain))
        sheet.update_cell(sheet.LAST_PRICE, uid, value = "{:.2f}".format(last_price))

        row[sheet.PL_t] = pl
        row[sheet.GAIN_t] = gain
        row[sheet.LAST_PRICE_t] = last_price               

        if x.trend == 'increasing':
            font_color = RGB.SEA_GREEN 
        elif x.trend == 'decreasing':
            font_color = RGB.RED  
        else:
            font_color = RGB.BLUE                  
                          
        sheet.update_cell(sheet.LAST_STOCK_PRICE, uid, value=stock_price)
        sheet.update_cell(sheet.LAST_QUOTE_DATE, uid, value=today ) 
        sheet.update_cell(sheet.LAST_TREND, uid, value = x.trend, font_color = font_color) 
        sheet.update_cell(sheet.LAST_SLOPE, uid, value = "{:.2f}".format(x.slope))                             
        if last_delta != None:                                                                                                      
            sheet.update_cell(sheet.LAST_delta, uid, value = "{:.2f}".format(float(last_delta)))                         
        if len(op.impliedVolatility) > 0:
            sheet.update_cell(sheet.LAST_impliedVolatility, uid, value = "{:.2f}".format(float(op.impliedVolatility)))                         
        if len(op.volume) > 0:
            sheet.update_cell(sheet.LAST_volume, uid, value = "{:.0f}".format(float(op.volume)))                         
        if len(op.openInterest) > 0:
            sheet.update_cell(sheet.LAST_openInterest, uid, value = "{:d}".format(int(op.openInterest)))                         
  
        sheet.update_cell(sheet.P1SP, uid, value=row[sheet.P1SP_t])  
        sheet.update_cell(sheet.P1SP, uid, value=row[sheet.P1LP_t])
        sheet.update_cell(sheet.P2SP, uid, value=row[sheet.P2SP_t])
        sheet.update_cell(sheet.P2SP, uid, value=row[sheet.P2LP_t])      

        self.update_all_strategy_legs(row)         

        self.try_stop_one_strategy_position(uid, stock_price,  row)         
 
 
    def update_all_strategy_legs(self, row):
        sheet = self.acct_position_sheet
        df = sheet.to_df()   
        if row[self.option_summary_sheet.P1SP_t]  != False:          
            dfs = df[df[sheet.UUID_t] == row[self.option_summary_sheet.UUID_t]+'P1S']
            if dfs.shape[0] > 0:
                if dfs.shape[0] > 1:
                    logger.warnings('too many option legs %d found %s' % (dfs.shape[0], row[self.option_summary_sheet.UUID_t]+'P1S') )                              
                uid = dfs.index[0] + 2
                self.update_one_strategy_leg(uid, dfs.iloc[0], row[self.option_summary_sheet.P1SP_t])                
            else:
                logger.error('option leg not found %s' % row[self.option_summary_sheet.UUID_t]+'P1S' )                

        if row[self.option_summary_sheet.P1LP_t]  != None:    
            dfs = df[df[sheet.UUID_t] == row[self.option_summary_sheet.UUID_t]+'P1L']
            if dfs.shape[0] > 0:
                if dfs.shape[0] > 1:
                    logger.warnings('too many option legs %d found %s' % (dfs.shape[0], row[self.option_summary_sheet.UUID_t]+'P1L') )                              
                uid = dfs.index[0] + 2
                self.update_one_strategy_leg(uid, dfs.iloc[0], row[self.option_summary_sheet.P1LP_t])                 
            else:
                logger.error('option leg not found %s' % row[self.option_summary_sheet.UUID_t]+'P1L' )  

        if row[self.option_summary_sheet.P2SP_t]  != None:    
            dfs = df[df[sheet.UUID_t] == row[self.option_summary_sheet.UUID_t]+'P2S']
            if dfs.shape[0] > 0:
                if dfs.shape[0] > 1:
                    logger.warnings('too many option legs %d found %s' % (dfs.shape[0], row[self.option_summary_sheet.UUID_t]+'P2S') )                              

                uid = dfs.index[0] + 2
                self.update_one_strategy_leg(uid, dfs.iloc[0], row[self.option_summary_sheet.P2SP_t])                 
            #else:
            #    logger.error('option leg not found %s' % row[self.option_summary_sheet.UUID_t]+'P2S' )  

        if row[self.option_summary_sheet.P2LP_t] != None:    
            dfs = df[df[sheet.UUID_t] == row[self.option_summary_sheet.UUID_t]+'P2L']
            if dfs.shape[0] > 0:
                if dfs.shape[0] > 1:
                    logger.warnings('too many option legs %d found %s' % (dfs.shape[0], row[self.option_summary_sheet.UUID_t]+'P2L') )                              

                uid = dfs.index[0] + 2
                self.update_one_strategy_leg(uid, dfs.iloc[0], row[self.option_summary_sheet.P2LP_t])                   
            #else:
            #    logger.error('option leg not found %s' % row[self.option_summary_sheet.UUID_t]+'P2L' )  

    def update_one_strategy_leg(self, uid, row, last_price):
        sheet = self.acct_position_sheet
        quantity = row[sheet.QUANTITY_t]
        total_cost = row[sheet.TOTAL_COST_BASIS_t]
        current_value = 100 * last_price * quantity
        if quantity > 0:
            gain_loss = current_value - total_cost
        else:
            gain_loss = current_value + total_cost        

        gain_loss_percent = (gain_loss / total_cost) * 100     
        sheet.update_cell(sheet.LAST_PRICE, uid, value=last_price)     
        sheet.update_cell(sheet.CURRENT_VALUE, uid, value=current_value)               

        if gain_loss > 0:
            font_color = RGB.SEA_GREEN
        else:
            font_color = RGB.RED                                                                                          

        sheet.update_cell(sheet.TOTAL_GAIN_LOSS, uid, value= '%2.f' % gain_loss, font_color=font_color)        
        sheet.update_cell(sheet.TOTAL_GAIN_LOSS_PERCENT, uid, value='%.2f' % gain_loss_percent, font_color=font_color)   
        


    def try_stop_one_strategy_position(self, uid, stock_price,  row):   
        sheet = self.option_summary_sheet     
        gain = row[sheet.GAIN_t]
        today = datetime.now().astimezone(timezone(at.TIMEZONE)).date()
        exp_date = row[sheet.EXP_DATE_t].tz_localize(timezone(at.TIMEZONE)).date()
        days_to_expire = (exp_date - today).days  
        if days_to_expire < 0:
            self.close_one_expired_strategy_position(uid, exp_stock_price, row)
            return
        if gain > self.risk_mgr.stop_gain_percent:
            self.close_one_strategy_position(uid, stock_price, row)
            return
        if gain < 0 and abs(gain) > self.risk_mgr.stop_loss_percent:
            self.close_one_strategy_position(uid, stock_price, row)
            return
        if days_to_expire < self.risk_mgr.close_days_before_expire:
            self.close_one_strategy_position(uid, stock_price, row)
            return
        if pd.isnull(row[sheet.EARNING_DATE_t]) != True:
            earning_date = row[sheet.EARNING_DATE_t].tz_localize(timezone(at.TIMEZONE)).date()                 
            days_to_earning = (earning_date - today).days               
            if days_to_earning < self.risk_mgr.close_days_before_expire:
                self.close_one_strategy_position(uid, stock_price, row)
                return
        return



    def close_all_strategy_legs(self, row):

        sheet = self.acct_position_sheet
        df = sheet.to_df()   
        if row[self.option_summary_sheet.P1SP_t]  != None:          
            dfs = df[df[sheet.UUID_t] == row[self.option_summary_sheet.UUID_t]+'P1S']
            if dfs.shape[0] > 0:
                if dfs.shape[0] > 1:
                    logger.warnings('too many option legs %d found %s' % (dfs.shape[0], row[self.option_summary_sheet.UUID_t]+'P1S') )                              
                uid = dfs.index[0] + 2
                self.close_one_strategy_leg(uid, dfs.iloc[0], row[self.option_summary_sheet.P1SP_t])                                
            else:
                logger.error('option leg not found %s' % row[self.option_summary_sheet.UUID_t]+'P1S' )                

        if row[self.option_summary_sheet.P1LP_t]  != None:    
            dfs = df[df[sheet.UUID_t] == row[self.option_summary_sheet.UUID_t]+'P1L']
            if dfs.shape[0] > 0:
                if dfs.shape[0] > 1:
                    logger.warnings('too many option legs %d found %s' % (dfs.shape[0], row[self.option_summary_sheet.UUID_t]+'P1L') )                              

                uid = dfs.index[0] + 2
                self.close_one_strategy_leg(uid, dfs.iloc[0], row[self.option_summary_sheet.P1LP_t])                 
            else:
                logger.error('option leg not found %s' % row[self.option_summary_sheet.UUID_t]+'P1L' )  

        if row[self.option_summary_sheet.P2SP_t]  != None:    
            dfs = df[df[sheet.UUID_t] == row[self.option_summary_sheet.UUID_t]+'P2S']
            if dfs.shape[0] > 0:
                if dfs.shape[0] > 1:
                    logger.warnings('too many option legs %d found %s' % (dfs.shape[0], row[option_summary_sheet.UUID_t]+'P2S') )                              

                uid = dfs.index[0] + 2
                self.close_one_strategy_leg(uid, dfs.iloc[0], row[option_summary_sheet.P2SP_t])                 
            #else:
            #    logger.error('option leg not found %s' % row[self.option_summary_sheet.UUID_t]+'P2S' )  

        if row[self.option_summary_sheet.P2LP_t] != None:    
            dfs = df[df[sheet.UUID_t] == row[self.option_summary_sheet.UUID_t]+'P2L']
            if dfs.shape[0] > 0:
                if dfs.shape[0] > 1:
                    logger.warnings('too many option legs %d found %s' % (dfs.shape[0], row[self.option_summary_sheet.UUID_t]+'P2L') )                              

                uid = dfs.index[0] + 2
                self.close_one_strategy_leg(dfs.iloc[0], row[self.option_summary_sheet.P2LP_t])                   
            #else:
            #    logger.error('option leg not found %s' % row[self.option_summary_sheet.UUID_t]+'P2L' )  

        PL = 100 * row[self.option_summary_sheet.PL_t] * row[self.option_summary_sheet.QUANTITY_t]

        self.cash_position += PL


        if math.isnan(row[self.option_summary_sheet.MARGIN_t]) == False:
             margin = 100 * row[self.option_summary_sheet.MARGIN_t] * row[self.option_summary_sheet.QUANTITY_t] 

             self.margin_position -= margin
             self.cash_position += margin             
             self.update_margin_position(self.margin_position)                

        self.update_cash_position(self.cash_position)         


    def close_one_strategy_leg(self, uid, row, last_price):
        sheet = self.acct_position_sheet
        symbol = row[sheet.SYMBOL_t]
        quantity = row[sheet.QUANTITY_t]
        total_cost = row[sheet.TOTAL_COST_BASIS_t]
        current_value = 100 * last_price * quantity
        if quantity > 0:
            gain_loss = current_value - total_cost   
        else:
            gain_loss = current_value + total_cost        
        
        gain_loss_percent = (gain_loss / total_cost) * 100     
        sheet.update_cell(sheet.LAST_PRICE, uid, value=last_price)     
        sheet.update_cell(sheet.CURRENT_VALUE, uid, value=current_value)               
        if gain_loss > 0:
            font_color = RGB.SEA_GREEN
        else:
            font_color = RGB.RED                                                                                          
        sheet.update_cell(sheet.TOTAL_GAIN_LOSS, uid, value=gain_loss, font_color=font_color)        
        sheet.update_cell(sheet.TOTAL_GAIN_LOSS_PERCENT, uid, value='%.2f' % gain_loss_percent, font_color=font_color)           
        sheet.update_cell(sheet.STATUS, uid, value = at.CLOSED )  

        exp_date =  row[sheet.EXP_DATE_t]
        strike = row[sheet.STRIKE_t]
        otype = row[sheet.TYPE_t]

        tsheet = self.transaction_sheet
        tid = self.transaction_sheet.sheet.range('A1').current_region.last_cell.row + 1
        trx_time = datetime.now(timezone(at.TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S %Z")  
 
        if quantity < 0:
            buy_sell = at.BUY
        else:
            buy_sell = at.SELL

        self.add_one_option_transaction(tid, trx_time, symbol, buy_sell, at.CLOSE,
                                        otype,strike,last_price,
                                        exp_date, quantity)  

        return gain_loss

    def close_one_expired_strategy_position(self, uid, exp_stock_price, row):

        sheet = self.option_summary_sheet                                                                                                       
        strategy = row[sheet.STRATEGY_t]
        open_price = row[sheet.OPEN_PRICE_t]
        sheet.update_cell(sheet.EXP_PRICE, uid, value=exp_stock_price) 
        sheet.update_cell(sheet.LAST_STOCK_PRICE, uid, value=exp_stock_price)
        sheet.update_cell(sheet.LAST_QUOTE_DATE, uid, value=row[sheet.EXP_DATE_t])                

        if strategy == st.LONG_CALL:
            last_price = row[sheet.P1LP_t] = self.cv(exp_stock_price, row[sheet.P1LK_t])
            gain = last_price - open_price                 
        elif strategy == st.LONG_PUT:
            last_price = row[sheet.P1LP_t]= self.pv(exp_stock_price, row[sheet.P1LK_t])
            gain = last_price - open_price                  
        elif strategy == st.COVERED_CALL:
            last_price = row[sheet.P1SP_t] = self.cv(exp_stock_price, row[sheet.P1SK_t])
            gain = open_price - last_price                    
        elif strategy == st.SHORT_PUT:
            last_price = row[sheet.P1SP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            gain = open_price - last_price                
        elif strategy == st.CREDIT_PUT_SPREAD:
            row[sheet.P1SP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t]  = self.pv(exp_stock_price, row[sheet.P1LK_t])
            last_price = row[sheet.P1SP_t]  - row[sheet.P1LP_t]
            gain = open_price - last_price                
        elif strategy == st.DEBIT_PUT_SPREAD:
            row[sheet.P1SP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t] = self.pv(exp_stock_price, row[sheet.P1LK_t])                          
            last_price = row[sheet.P1LP_t] - row[sheet.P1SP_t]         
            gain = last_price - open_price                            
        elif strategy == st.CREDIT_CALL_SPREAD:
            row[sheet.P1SP_t] = self.cv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t] = self.cv(exp_stock_price, row[sheet.P1LK_t])  
            last_price = row[sheet.P1SP_t] - row[sheet.P1LP_t]          
            gain = open_price - last_price                     
        elif strategy == st.DEBIT_CALL_SPREAD:
            row[sheet.P1SP_t] = self.cv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t]  = self.cv(exp_stock_price, row[sheet.P1LK_t])
            last_price = row[sheet.P1LP_t] - row[sheet.P1SP_t]     
            gain = last_price - open_price                                                        
        elif strategy == st.CREDIT_IRON_CONDOR:         
            row[sheet.P1SP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t] = self.pv(exp_stock_price, row[sheet.P1LK_t])
            row[sheet.P2SP_t] = self.cv(exp_stock_price, row[sheet.P2SK_t])
            row[sheet.P2LP_t] = self.cv(exp_stock_price, row[sheet.P2LK_t])     
            last_price = (row[sheet.P1SP_t] - row[sheet.P1LP_t]) + (row[sheet.P2SP_t] - row[sheet.P2LP_t])                                                       
            gain = open_price - last_price                      
        elif strategy == st.DEBIT_IRON_CONDOR:         
            row[sheet.P1SP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t] = self.pv(exp_stock_price, row[sheet.P1LK_t])
            row[sheet.P2SP_t] = self.cv(exp_stock_price, row[sheet.P2SK_t])
            row[sheet.P2LP_t] = self.cv(exp_stock_price, row[sheet.P2LK_t])          
            last_price = (row[sheet.P1LP_t] - row[sheet.P1SP_t]) + (row[sheet.P2LP_t] - row[sheet.P2SP_t])                                                                                            
            gain = last_price - open_price                
        elif strategy == st.DEBIT_CALL_BUTTERFLY:
            row[sheet.P1LP_t] = self.cv(exp_stock_price, row[sheet.P1LK_t])
            row[sheet.P1SP_t] = row[sheet.P2SP_t] = self.cv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P2LP_t] = self.cv(exp_stock_price, row[sheet.P2LK_t])            
            last_price = abs(row[sheet.P1LP_t] + row[sheet.P2LP_t] - (2 * row[sheet.P1SP_t]))
            gain = last_price - open_price                
        elif strategy == st.CREDIT_PUT_BUTTERFLY:
            row[sheet.P1LP_t] = self.pv(exp_stock_price, row[sheet.P1LK_t])
            row[sheet.P1SP_t] = row[sheet.PSLP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P2LP_t] = self.pv(exp_stock_price, row[sheet.P2LK_t])    
            last_price = abs(row[sheet.P1LP_t] + row[sheet.P2LP_t] - (2 * row[sheet.P1SP_t]))
            gain = last_price - open_price                     
        elif strategy == st.CREDIT_CALL_BUTTERFLY:
            row[sheet.P1SP_t] = self.cv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t] = row[sheet.P2LP_t] = self.cv(exp_stock_price, row[sheet.P1LK_t])
            row[sheet.P2SP_t] = self.cv(exp_stock_price, row[sheet.P2SK_t])            
            last_price = abs(row[sheet.P1SP_t] + row[sheet.P2SP_t] - (2 * row[sheet.P1LP_t]))            
            gain = open_price - last_price                                  
        elif strategy == st.DEBIT_PUT_BUTTERFLY:
            row[sheet.P1SP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t] = row[sheet.P2LP_t]  = self.long_put_v(exp_stock_price, row[sheet.P1LK_t])
            row[sheet.P2SP_t] = self.pv(exp_stock_price, row[sheet.P2SK_t])            
            last_price = abs(row[sheet.P1SP_t] + row[sheet.P2SP_t] - (2 * row[sheet.P1LP_t]))                        
            gain = open_price - last_price                               
        elif strategy == st.IRON_BUTTERFLY or strategy == st.REVERSE_IRON_BUTTERFLY:  
            row[sheet.P1SP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t] = self.pv(exp_stock_price, row[sheet.P1LK_t])
            row[sheet.P2LP_t] = self.cv(exp_stock_price, row[sheet.P2LK_t])            
            row[sheet.P2SP_t] = self.cv(exp_stock_price, row[sheet.P2SK_t])
            last_price = abs(row[sheet.P1SP_t]-row[sheet.P1LP_t]) + abs(row[sheet.P2SP_t]-row[sheet.P2LP_t])             
            gain = open_price - last_price                     
        elif strategy == st.REVERSE_IRON_BUTTERFLY: 
            row[sheet.P1SP_t] = self.pv(exp_stock_price, row[sheet.P1SK_t])
            row[sheet.P1LP_t] = self.pv(exp_stock_price, row[sheet.P1LK_t])
            row[sheet.P2SLP_t]= self.cv(exp_stock_price, row[sheet.P1LK_t])            
            row[sheet.P2SP_t] = self.cv(exp_stock_price, row[sheet.P2SK_t])
            last_price = abs(row[sheet.P1SP_t]-row[sheet.P1LP_t]) + abs(row[sheet.P2SP_t]-row[sheet.P2LP_t])              
        else:
            logger.error('close_one_expired_strategy_position Unknown strategy %s' % strategy)
            return                                                          

        sheet.update_cell(sheet.P1SP, uid, value=row[sheet.P1SP_t]) 
        sheet.update_cell(sheet.P1LP, uid, value=row[sheet.P1LP_t]) 
        sheet.update_cell(sheet.P2SP, uid, value=row[sheet.P2SP_t]) 
        sheet.update_cell(sheet.P2LP, uid, value=row[sheet.P1LP_t]) 

        pl = gain  

        gain = 100 * gain / open_price
                                        
        sheet.update_cell(sheet.PL, uid, value = "{:.2f}".format(pl))        
        sheet.update_cell(sheet.GAIN, uid, value = "{:.2f}".format(gain))
        sheet.update_cell(sheet.LAST_PRICE, uid, value = "{:.2f}".format(last_price))                                                                                                           
        sheet.update_cell(sheet.STATUS, uid, value = at.CLOSED )  

        row[sheet.PL_t] = pl
        row[sheet.GAIN_t] = gain
        row[sheet.LAST_PRICE_t] = last_price
        row[sheet.STATUS_t] = at.CLOSED

        self.close_all_strategy_legs(row)   

    def close_one_strategy_position(self, uid, row):
        sheet = self.option_summary_sheet   
        sheet.update_cell(sheet.STATUS, uid, value=at.CLOSED) 
        self.close_all_strategy_legs(row)                    
        return 
############### Utility Functions #################
    def update_cash_position(self, cash_position):
        #logger.info('update cash position %.2f' % cash_position)     
        df = self.acct_position_sheet.to_df()
        cdf = df.loc[df[self.acct_position_sheet.SYMBOL_t] == at.CASH]         
        cdf.shape[0]
        if cdf.shape[0] == 0:
            uid = df.shape[0] + 2 
            self.acct_position_sheet.update_cell(self.acct_position_sheet.SYMBOL, uid, value= at.CASH, font_bold=True)             
            self.acct_position_sheet.update_cell(self.acct_position_sheet.TYPE, uid, value = at.CASH)        
            self.acct_position_sheet.update_cell(self.acct_position_sheet.QUANTITY, uid, value = cash_position)               
        else:
            uid = cdf.index[0] + 2        
            self.acct_position_sheet.update_cell(self.acct_position_sheet.QUANTITY, uid, value = cash_position)                               

        return cash_position

    def update_margin_position(self, margin_position):
        #logger.info('update margin position %.2f' % margin_position)        
        df = self.acct_position_sheet.to_df()
        cdf = df.loc[df[self.acct_position_sheet.SYMBOL_t] == at.MARGIN]         
        cdf.shape[0]
        if cdf.shape[0] == 0:
            uid = df.shape[0] + 2 
            self.acct_position_sheet.update_cell(self.acct_position_sheet.SYMBOL, uid, value=at.MARGIN, font_bold=True)             
            self.acct_position_sheet.update_cell(self.acct_position_sheet.TYPE, uid, value = at.CASH)        
            self.acct_position_sheet.update_cell(self.acct_position_sheet.QUANTITY, uid, value = margin_position)               
        else:
            uid = cdf.index[0] + 2        
            self.acct_position_sheet.update_cell(self.acct_position_sheet.QUANTITY, uid, value = margin_position)                               

        return margin_position        

    def get_cash_position(self):
        df = self.acct_position_sheet.to_df()
        cdf = df.loc[df[self.acct_position_sheet.SYMBOL_t] == at.CASH]         
        
        if cdf.shape[0] == 0:
            uid = df.shape[0] + 2 
            self.acct_position_sheet.update_cell(self.acct_position_sheet.SYMBOL, uid, value=at.CASH, font_bold=True)             
            self.acct_position_sheet.update_cell(self.acct_position_sheet.TYPE, uid, value = at.CASH)        
            self.acct_position_sheet.update_cell(self.acct_position_sheet.QUANTITY, uid, value = self.runtime_config.init_balance)               
            return self.runtime_config.init_balance
        else:
            return cdf.Quantity.values[0]            

    def get_margin_position(self):
        df = self.acct_position_sheet.to_df()
        cdf = df.loc[df[self.acct_position_sheet.SYMBOL_t] == at.MARGIN]         

        if cdf.shape[0] == 0:
            uid = df.shape[0] + 2 
            self.acct_position_sheet.update_cell(self.acct_position_sheet.SYMBOL, uid, value=at.MARGIN, font_bold=True)             
            self.acct_position_sheet.update_cell(self.acct_position_sheet.TYPE, uid, value = at.MARGIN)        
            self.acct_position_sheet.update_cell(self.acct_position_sheet.QUANTITY, uid, value = 0)               
            return 0
        else:
            return cdf.Quantity.values[0]                              

    def map_1legs_option(self, row, q, UUID):
        uid = self.acct_position_sheet.sheet.range('A1').current_region.last_cell.row + 1
        sheet = self.acct_position_sheet
                  
        if row.P1SP == None:
            self.add_one_option_position(uid+1,row.SYMBOL,row.P1LT,row.P1LK,row.P1LP,\
                                    row.EXP_DATE, q, UUID+'P1L' )                                          
        else:      
            self.add_one_option_position(uid,  row.SYMBOL,row.P1ST,row.P1SK,row.P1SP,
                                    row.EXP_DATE,-1*q, UUID+'P1S' )                

        tsheet = self.transaction_sheet
        tid = self.transaction_sheet.sheet.range('A1').current_region.last_cell.row + 1
        trx_time = datetime.now(timezone(at.TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S %Z")                  
        if row.P1SP != None:  
            self.add_one_option_transaction(tid,trx_time,row.SYMBOL,at.BUY,at.OPEN,\
                                            row.P1LT,row.P1LK,row.P1LP,\
                                            row.EXP_DATE, q)                                   
        else:
            self.add_one_option_transaction(tid,  trx_time,row.SYMBOL,at.SELL,at.OPEN,\
                                            row.P1ST,row.P1SK,row.P1SP,\
                                            row.EXP_DATE, q)            
                                     

    def map_2legs_option(self, row, q, UUID):
                    
        uid = self.acct_position_sheet.sheet.range('A1').current_region.last_cell.row + 1
        sheet = self.acct_position_sheet

        self.add_one_option_position(uid,  row.SYMBOL,row.P1ST,row.P1SK,row.P1SP,
                                    row.EXP_DATE,-1*q, UUID+'P1S' )
        self.add_one_option_position(uid+1,row.SYMBOL,row.P1LT,row.P1LK,row.P1LP,\
                                    row.EXP_DATE, q, UUID+'P1L' ) 

        tsheet = self.transaction_sheet
        tid = self.transaction_sheet.sheet.range('A1').current_region.last_cell.row + 1

        trx_time = datetime.now(timezone(at.TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S %Z")     

        self.add_one_option_transaction(tid,  trx_time,row.SYMBOL,at.SELL,at.OPEN,\
                                        row.P1ST,row.P1SK,row.P1SP,\
                                        row.EXP_DATE, q)
        self.add_one_option_transaction(tid+1,trx_time,row.SYMBOL,at.BUY,at.OPEN,\
                                        row.P1LT,row.P1LK,row.P1LP,\
                                        row.EXP_DATE, q)                               


    def map_3legs_option(self, row, q, UUID):
                    
        uid = self.acct_position_sheet.sheet.range('A1').current_region.last_cell.row + 1
        sheet = self.acct_position_sheet

        strategy = row.STRATEGY     
                 
        if strategy == st.CREDIT_CALL_BUTTERFLY or strategy == st.CREDIT_PUT_BUTTERFLY:
            
            self.add_one_option_position(uid,  row.SYMBOL,row.P1ST,row.P1SK,row.P1SP,
                                        row.EXP_DATE,-1*q, UUID+'P1S' )
            self.add_one_option_position(uid+1,row.SYMBOL,row.P1LT,row.P1LK,row.P1LP,\
                                        row.EXP_DATE, 2 * q, UUID+'P1L' )
            self.add_one_option_position(uid+2,row.SYMBOL,row.P2ST,row.P2SK,row.P2SP,\
                                        row.EXP_DATE,-1*q, UUID+'P2S')

        elif strategy == st.DEBIT_CALL_BUTTERFLY or strategy == st.DEBIT_PUT_BUTTERFLY:    

            self.add_one_option_position(uid,  row.SYMBOL,row.P1LT,row.P1LK,row.P1LP,
                                        row.EXP_DATE, q, UUID+'P1L' )
            self.add_one_option_position(uid+1,row.SYMBOL,row.P1LT,row.P1LK,row.P1SP,\
                                        row.EXP_DATE, -2 * q, UUID+'P1S' )
            self.add_one_option_position(uid+2,row.SYMBOL,row.P2ST,row.P2SK,row.P2SP,\
                                        row.EXP_DATE, q, UUID+'P2L')
        else:
            logger.error('map_3legs_option Unknown strategy %s' % strategy)
            return

        tsheet = self.transaction_sheet
        tid = self.transaction_sheet.sheet.range('A1').current_region.last_cell.row + 1
        trx_time = datetime.now(timezone(at.TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S %Z")

        if strategy == st.CREDIT_CALL_BUTTERFLY or strategy == st.CREDIT_PUT_BUTTERFLY:
                          
            self.add_one_option_transaction(tid,  trx_time,row.SYMBOL,at.SELL,at.OPEN,\
                                            row.P1ST,row.P1SK,row.P1SP,\
                                            row.EXP_DATE, q)
            self.add_one_option_transaction(tid+1,trx_time,row.SYMBOL,at.BUY,at.OPEN,\
                                            row.P1LT,row.P1LK,row.P1LP,\
                                            row.EXP_DATE, q)
            self.add_one_option_transaction(tid+2, trx_time,row.SYMBOL,at.SELL,at.OPEN,\
                                            row.P2ST,row.P2SK,row.P2SP,\
                                            row.EXP_DATE, q)
        elif strategy == st.DEBIT_CALL_BUTTERFLY or strategy == st.DEBIT_PUT_BUTTERFLY:   

            self.add_one_option_transaction(tid,  trx_time,row.SYMBOL,at.BUY,at.OPEN,\
                                            row.P1LT,row.P1LK,row.P1LP,\
                                            row.EXP_DATE, q)
            self.add_one_option_transaction(tid+1,trx_time,row.SYMBOL,at.SELL,at.OPEN,\
                                            row.P1ST,row.P1SK,row.P1LP,\
                                            row.EXP_DATE, q)
            self.add_one_option_transaction(tid+2, trx_time,row.SYMBOL,at.BUY,at.OPEN,\
                                            row.P2LT,row.P2LK,row.P2LP,\
                                            row.EXP_DATE, q)            
        else:
            logger.error('map_3legs_option Unknown strategy %s' % strategy)
            return

    def map_4legs_option(self, row, q, UUID):
                    
        uid = self.acct_position_sheet.sheet.range('A1').current_region.last_cell.row + 1
        sheet = self.acct_position_sheet

        self.add_one_option_position(uid,  row.SYMBOL,row.P1ST,row.P1SK,row.P1SP,
                                    row.EXP_DATE,-1*q, UUID+'P1S' )
        self.add_one_option_position(uid+1,row.SYMBOL,row.P1LT,row.P1LK,row.P1LP,\
                                    row.EXP_DATE,q, UUID+'P1L' )
        self.add_one_option_position(uid+2,row.SYMBOL,row.P2ST,row.P2SK,row.P2SP,\
                                    row.EXP_DATE,-1*q, UUID+'P2S')
        self.add_one_option_position(uid+3,row.SYMBOL,row.P2LT,row.P2LK,row.P2LK,\
                                    row.EXP_DATE,q, UUID+'P2L')      

        tsheet = self.transaction_sheet
        tid = self.transaction_sheet.sheet.range('A1').current_region.last_cell.row + 1

        trx_time = datetime.now(timezone(at.TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S %Z")                           

        self.add_one_option_transaction(tid,  trx_time,row.SYMBOL,at.SELL,at.OPEN,\
                                        row.P1ST,row.P1SK,row.P1SP,\
                                        row.EXP_DATE, q)
        self.add_one_option_transaction(tid+1,trx_time,row.SYMBOL,at.BUY,at.OPEN,\
                                        row.P1LT,row.P1LK,row.P1LP,\
                                        row.EXP_DATE, q)
        self.add_one_option_transaction(tid+2, trx_time,row.SYMBOL,at.SELL,at.OPEN,\
                                        row.P2ST,row.P2SK,row.P2SP,\
                                        row.EXP_DATE, q)
        self.add_one_option_transaction(tid+3, trx_time,row.SYMBOL,at.BUY,at.OPEN,\
                                        row.P2LT,row.P2SK,row.P2SP,\
                                        row.EXP_DATE, q)      

    def add_one_option_position(self, 
                                uid, 
                                symbol, 
                                otype,                         
                                strike,                         
                                price,
                                exp_date,                                   
                                quantity,
                                UUID_tag):         

        sheet = self.acct_position_sheet

        sheet.update_cell(sheet.SYMBOL,    uid, value=symbol, font_bold=True)        
        sheet.update_cell(sheet.TYPE,      uid, value=otype)        
        sheet.update_cell(sheet.STRIKE,    uid, value=strike)    
        sheet.update_cell(sheet.LAST_PRICE,uid, value=price)     
        sheet.update_cell(sheet.EXP_DATE,  uid, value=exp_date)                                  
        sheet.update_cell(sheet.QUANTITY,  uid, value=quantity)   
        sheet.update_cell(sheet.TOTAL_COST_BASIS,  uid, value = abs(quantity) * 100 * price)    
        sheet.update_cell(sheet.AVERAGE_COST_BASIS, uid, value = price )            
        sheet.update_cell(sheet.CURRENT_VALUE, uid, value = quantity * 100 * price )             
        sheet.update_cell(sheet.STATUS, uid, value = at.OPENED )            
        sheet.update_cell(sheet.UUID, uid, value = UUID_tag ) 

    def add_one_option_transaction(self, 
                                    tid, 
                                    trx_time, 
                                    symbol, 
                                    buy_sell, 
                                    open_close, 
                                    otype, 
                                    strike, 
                                    price, 
                                    exp_date,                                        
                                    quantity,
                                    commission=0,
                                    fee=0):
        tsheet = self.transaction_sheet
        tsheet.update_cell(tsheet.TRX_TIME,  tid, value=trx_time)            
        tsheet.update_cell(tsheet.SYMBOL,    tid, value =symbol)        
        tsheet.update_cell(tsheet.BUY_SELL,  tid, value =buy_sell)
        tsheet.update_cell(tsheet.OPEN_CLOSE,tid, value =open_close)
        tsheet.update_cell(tsheet.TYPE,      tid, value =otype)
        tsheet.update_cell(tsheet.EXP_DATE,  tid, value =exp_date)           
        tsheet.update_cell(tsheet.STRIKE,    tid, value =strike)            
        tsheet.update_cell(tsheet.PRICE,     tid, value =price)                             
        tsheet.update_cell(tsheet.QUANTITY,  tid, value =quantity)    
        tsheet.update_cell(tsheet.AMOUNT,    tid, value =quantity*100*price)    
        tsheet.update_cell(tsheet.COMMISSION,tid, value =commission )             
        tsheet.update_cell(tsheet.FEE,       tid, value =fee )      

    def map_to_option_summary_sheet(self, row, q, UUID):
                    
        sheet = self.option_summary_sheet
        uid = self.option_summary_sheet.sheet.range('A1').current_region.last_cell.row + 1

        report_date = get_next_earning_date(row.SYMBOL)

        sheet.update_cell(sheet.STRATEGY, uid, value = row.STRATEGY)     
        sheet.update_cell(sheet.QUANTITY, uid, value = q)                                               
        sheet.update_cell(sheet.SYMBOL, uid, value=row.SYMBOL, font_bold=True) 

        if report_date != None:        
            sheet.update_cell(sheet.EARNING_DATE, uid, value = report_date.strftime("%m-%d-%y"))

        if math.isnan(row.SPREAD) == False:
            sheet.update_cell(sheet.SPREAD, uid, value=row.SPREAD)                

        if math.isnan(row.P1SK) == False:
            sheet.update_cell(sheet.P1SK, uid, value =  "{:.1f}".format(row.P1SK))
            sheet.update_cell(sheet.P1SP, uid, value =  "{:.1f}".format(row.P1SP))
            sheet.update_cell(sheet.P1ST, uid, value =  row.P1ST)                        
        if math.isnan(row.P1LK) == False:
            sheet.update_cell(sheet.P1LK, uid, value =  "{:.1f}".format(row.P1LK))
            sheet.update_cell(sheet.P1LP, uid, value =  "{:.1f}".format(row.P1LP))
            sheet.update_cell(sheet.P1LT, uid, value =  row.P1LT)                       
        if math.isnan(row.P2SK) == False:
            sheet.update_cell(sheet.P2SK, uid, value =  "{:.1f}".format(row.P2SK))
            sheet.update_cell(sheet.P2SP, uid, value =  "{:.1f}".format(row.P2SP))
            sheet.update_cell(sheet.P2ST, uid, value =  row.P2ST)                       
        if math.isnan(row.P2LK) == False:
            sheet.update_cell(sheet.P2LK, uid, value =  "{:.1f}".format(row.P2LK))
            sheet.update_cell(sheet.P2LP, uid, value =  "{:.1f}".format(row.P2LP))
            sheet.update_cell(sheet.P2LT, uid, value =  row.P2LT)                        

        sheet.update_cell(sheet.OPEN_PRICE, uid, value = "{:.2f}".format(row.OPEN_PRICE))
        if math.isnan(row.MAX_PROFIT) == False:
            sheet.update_cell(sheet.MAX_PROFIT, uid, value = "{:.2f}".format(row.MAX_PROFIT))                                       

        sheet.update_cell(sheet.MAX_LOSS, uid, value = "{:.2f}".format(row.MAX_LOSS)) 

        if math.isnan(row.MARGIN) == False:
            sheet.update_cell(sheet.MARGIN, uid, value = "{:.2f}".format(row.MARGIN))         

        sheet.update_cell(sheet.WIN_PROB, uid, value = "{:.2f}".format(row.WIN_PROB))  
        if math.isnan(row.PNL) == False:
            sheet.update_cell(sheet.PNL, uid, value = "{:.2f}".format(row.PNL)) 

        if math.isnan(row.BREAKEVEN_H) == False:
            sheet.update_cell(sheet.BREAKEVEN_H, uid, value = "{:.2f}".format(row.BREAKEVEN_H))
        if math.isnan(row.BREAKEVEN_L) == False:
            sheet.update_cell(sheet.BREAKEVEN_L, uid, value = "{:.2f}".format(row.BREAKEVEN_L))

        sheet.update_cell(sheet.TRADE_DATE, uid, value = row.TRADE_DATE.strftime("%m-%d-%y"))     
        sheet.update_cell(sheet.EXP_DATE, uid, value = row.EXP_DATE )     
        sheet.update_cell(sheet.TRADE_STOCK_PRICE, uid, value = "{:.2f}".format(row.TRADE_STOCK_PRICE))                                

        if row.INIT_TREND == 'increasing':
            font_color = RGB.SEA_GREEN 
        elif row.INIT_TREND == 'decreasing':
            font_color = RGB.RED  
        else:
            font_color = RGB.BLUE            

        sheet.update_cell(sheet.INIT_TREND, uid, value = row.INIT_TREND, font_color = font_color) 
        sheet.update_cell(sheet.INIT_SLOPE, uid, value = "{:.2f}".format(row.INIT_SLOPE))                      
        sheet.update_cell(sheet.INIT_delta, uid, value = "{:.2f}".format(float(row.INIT_DELTA)))  
        sheet.update_cell(sheet.INIT_impliedVolatility, uid, value = "{:.2f}".format(float(row.INIT_impliedVolatility)))   
        sheet.update_cell(sheet.INIT_volume, uid, value = "{:.0f}".format(float(row.INIT_volume)))                         
        sheet.update_cell(sheet.INIT_openInterest, uid, value = "{:.0f}".format(float(row.INIT_openInterest)))                         
        sheet.update_cell(sheet.STATUS, uid, value = at.OPENED )  
        sheet.update_cell(sheet.UUID, uid,value =UUID)                         

    def cv(self, stock_price, strike):
        return max(stock_price-strike, 0)

    def pv(self, stock_price, strike):
        return max(strike-stock_price, 0)
    def ov(self, op):
        if (len(op.bid) == 0 or float(op.bid) == 0.0) or (len(op.ask)==0 or float(op.ask) == 0):                                
            if len(op.lastPrice) == 0:
                return 0
            else:
                return float(op.lastPrice)
        else:
            return (float(op.bid)+float(op.ask))/2   
    


    def init_data(self, symbol):
        
        BBStrategy = ta.Strategy(
            name="Momo and Volatility",
            description="BBANDS",
            ta=[
                {"kind": "bbands", "length": 20},      
            ]
        )     

        data = get_price_history(symbol, period='2mo')
        data.ta.cores = 2        
        data.ta.strategy(BBStrategy)

        data.dropna(subset=["BBL_20_2.0"])
        s = self.runtime_config.trend_window_size # sample size for Mann-Kendall Trend Test
        gfg_data = [0] * s
        data['change'] = data['Close'].pct_change()
        data['rolling_sigma'] = data['change'].rolling(20).std() * np.sqrt(255)                             
        last_date_index = len(data.index)-1 
        for j in range(s):        
            gfg_data[j] = data['BBM_20_2.0'][last_date_index-s+1+j]    

        if math.isnan(gfg_data[0]):
            logger.error('gfg data [0] is nan')
            
        x = mk.original_test(gfg_data)
        
        option_chain = get_option_chain(symbol)

        return data, x, option_chain


    
 
        
                    