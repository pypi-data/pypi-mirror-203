import pandas as pd
import xlwings as xw
import numpy as np
import math
import json
from datetime import time, date, datetime, timedelta
import pytz
import pandas_ta as ta
import pymannkendall as mk
import mibian

from tradingBot.utils.dataGetter import get_price_history

from tradingBot.settings.tradeConfig import entryCrit
from tradingBot.settings.tradeConfig import exitCrit
from tradingBot.settings.tradeConfig import runtimeConfig
from tradingBot.settings.tradeConfig import marketCondition

from tradingBot.excel import positionSheet as ps
from tradingBot.excel import fundamentalSheet as fs

from tradingBot.utils.dataGetter import get_price_history
from tradingBot.utils.dataGetter import get_next_earning_date
from tradingBot.utils.dataGetter import get_option_chain

from tradingBot.optionPosition import single_leg as sl 
from tradingBot.optionPosition import spread as sp
from tradingBot.optionPosition import iron_condor as ic
from tradingBot.optionPosition import butterfly as bf   

import tradingBot.consts.strategy as st
from tradingBot.consts import asset as at
from tradingBot.consts import RGB


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('postionBook')

def dump_crit(sheet, entry_crit, runtime_config, market_condition):
    
    sheet.update_cell('AO', 2, font_bold = True, value='Entry Crit')           
    sheet.update_cell('AP', 2, font_bold = True, value='%s' % json.dumps(vars(entry_crit)))            
            
    sheet.update_cell('AO', 4, font_bold = True, value='Runtime Config')           
    sheet.update_cell('AP', 4, font_bold = True, value='%s' % json.dumps(vars(runtime_config))) 

    sheet.update_cell('AO', 6, font_bold = True, value='Market Condition')           
    sheet.update_cell('AP', 6, font_bold = True, value='%s' % json.dumps(vars(market_condition))) 

class positionBook():
    
    def __init__(self, file_path=None):
        self.file_path = file_path
        if file_path == None:
            self.wb = xw.Book()
        else:
            self.wb = xw.Book(file_path) 
        vix = get_price_history('^VIX', '1d')
        self.current_vix = vix['Close'][-1]
        
    def get_position_candidate(self, symbol_list,                    
                            entry_crit = entryCrit(),
                            runtime_config = runtimeConfig(),
                            market_condition = marketCondition()): 

        market_condition.current_vix = self.current_vix                            
        today = datetime.now(timezone(at.TIMEZONE)).date().strftime("%Y-%m-%d") 
        max_days_to_expire = runtime_config.max_days_to_expire
        spreads = runtime_config.spreads        
        
        for symbol in symbol_list: 
            uid = 1           
            logger.info('Processing %s', symbol)
            sheet = ps.positionSheet(self.wb, sheet_name="%s %s" % (symbol, today))   

            q = sl.single_leg_position(symbol, entry_crit, runtime_config)
            q.get_positions([st.LONG_CALL, st.LONG_PUT, st.COVERED_CALL, st.SHORT_PUT])
            init_uid = uid             
            uid = self._map_df_to_sheet(q.df, sheet, uid, symbol)
            logger.info('Get %d one leg positions for %s' % ((uid-init_uid), symbol))
    
            q =sp.spread_position(symbol, entry_crit, runtime_config)
            q.get_positions([st.CREDIT_CALL_SPREAD, st.CREDIT_PUT_SPREAD, st.DEBIT_CALL_SPREAD, st.DEBIT_PUT_SPREAD])
            init_uid = uid             
            uid = self._map_df_to_sheet(q.df, sheet, uid, symbol)
            logger.info('Get %d spread positions for %s' % ((uid-init_uid), symbol)) 
    
            q =bf.butterfly_position(symbol, entry_crit, runtime_config)
            q.get_positions([st.CREDIT_CALL_BUTTERFLY, st.CREDIT_PUT_BUTTERFLY, st.DEBIT_CALL_BUTTERFLY, st.DEBIT_PUT_BUTTERFLY, st.IRON_BUTTERFLY, st.REVERSE_IRON_BUTTERFLY])
            init_uid = uid             
            uid = self._map_df_to_sheet(q.df, sheet, uid, symbol)
            logger.info('Get %d butterfly positions for %s' % ((uid-init_uid), symbol))

            q =ic.iron_condor_position(symbol, entry_crit, runtime_config)
            q.get_positions([st.CREDIT_IRON_CONDOR, st.DEBIT_IRON_CONDOR])
            init_uid = uid             
            uid = self._map_df_to_sheet(q.df, sheet, uid, symbol)
            logger.info('Get %d iron condor positions for %s' % ((uid-init_uid), symbol))

            dump_crit(sheet, entry_crit, runtime_config, market_condition)


    def get_one_leg_positions(self,
                            watch_list,                   
                            entry_crit = entryCrit(),
                            runtime_config = runtimeConfig(),
                            market_condition = marketCondition()): 

        max_days_to_expire = runtime_config.max_days_to_expire

        market_condition.current_vix = self.current_vix
        
        today = datetime.now(timezone(at.TIMEZONE)).date().strftime("%Y-%m-%d")       
        
        sheet = ps.positionSheet(self.wb, sheet_name='Single Leg ' + today)      
        symbol_list = watch_list[fs.fundamentalSheet.SYMBOL_t].to_list()   
        uid = 1
        
        for symbol in symbol_list: 
           
            logger.info('Processing %s', symbol)                                   
            q =sl.single_leg_position(symbol, entry_crit, runtime_config)
            q.get_positions([st.LONG_CALL, st.LONG_PUT, st.COVERED_CALL, st.SHORT_PUT])
            init_uid = uid             
            uid = self._map_df_to_sheet(q.df, sheet, uid, symbol)
            logger.info('Get %d one leg positions for %s' % ((uid-init_uid), symbol))
    
        dump_crit(sheet, entry_crit, runtime_config, market_condition)
        
            
    def get_spread_positions(self, 
                                watch_list,                         
                                entry_crit = entryCrit(),
                                runtime_config = runtimeConfig(),
                                market_condition = marketCondition()):
                                            
        max_days_to_expire = runtime_config.max_days_to_expire
        spreads = runtime_config.spreads     

        today = datetime.now(timezone(at.TIMEZONE)).date().strftime("%Y-%m-%d") 
        
        market_condition.current_vix = self.current_vix

        sheet = ps.positionSheet(self.wb, sheet_name='Spread Quote ' + today)                 
         
        symbol_list = watch_list[fs.fundamentalSheet.SYMBOL_t].to_list()    
                  
        uid = 1
        
        for symbol in symbol_list: 
           
            logger.info('Processing %s', symbol)
            
            q =sp.spread_position(symbol, entry_crit)

            q.get_positions([st.CREDIT_CALL_SPREAD, st.CREDIT_PUT_SPREAD, st.DEBIT_CALL_SPREAD, st.DEBIT_PUT_SPREAD])

            init_uid = uid 
            
            uid = self._map_df_to_sheet(q.df, sheet, uid, symbol)

            logger.info('Get %d spread positions for %s' % ((uid-init_uid), symbol)) 
        
        dump_crit(sheet, entry_crit, runtime_config, market_condition)
        
    def get_butterfly_positions(self,
                                watch_list,                             
                                entry_crit = entryCrit(),
                                runtime_config = runtimeConfig(),
                                market_condition = marketCondition()):

        max_days_to_expire = runtime_config.max_days_to_expire
        spreads = runtime_config.spreads     

        today = datetime.now(timezone(at.TIMEZONE)).date().strftime("%Y-%m-%d")        

        market_condition.current_vix = self.current_vix
        
        sheet = ps.positionSheet(self.wb, sheet_name='Butterfly Quote ' + today)      
            
        symbol_list = watch_list[fs.fundamentalSheet.SYMBOL_t].to_list()    
            
        uid = 1
        
        for symbol in symbol_list: 
            
            logger.info("process %s", symbol)   
            
            q =bf.butterfly_position(symbol, entry_crit, runtime_config)
            
            q.get_positions([st.CREDIT_CALL_BUTTERFLY, st.CREDIT_PUT_BUTTERFLY, st.DEBIT_CALL_BUTTERFLY, st.DEBIT_PUT_BUTTERFLY, st.IRON_BUTTERFLY, st.REVERSE_IRON_BUTTERFLY])

            init_uid = uid 
            
            uid = self._map_df_to_sheet(q.df, sheet, uid, symbol)

            logger.info('Get %d butterfly positions for %s' % ((uid-init_uid), symbol))
            
        dump_crit(sheet, entry_crit, runtime_config, market_condition)
                    
    def get_iron_condor_positions(self, 
                                watch_list,                            
                                entry_crit = entryCrit(),
                                runtime_config = runtimeConfig(),
                                market_condition = marketCondition()):      

        max_days_to_expire = runtime_config.max_days_to_expire
        spreads = runtime_config.spreads                                       
      
        today = datetime.now(timezone(at.TIMEZONE)).date().strftime("%Y-%m-%d")         
        
        market_condition.current_vix = self.current_vix
        
        sheet = ps.positionSheet(self.wb, sheet_name='Iron Condor ' + today)      
 
        symbol_list = watch_list[fs.fundamentalSheet.SYMBOL_t].to_list()   

        uid = 1
        
        for symbol in symbol_list: 
           
            logger.info("process %s for iron condor", symbol)   
                            
            q =ic.iron_condor_position(symbol, entry_crit, runtime_config)

            q.get_positions([st.CREDIT_IRON_CONDOR, st.DEBIT_IRON_CONDOR])

            init_uid = uid 
            
            uid = self._map_df_to_sheet(q.df, sheet, uid, symbol)

            logger.info('Get %d iron condor positions for %s' % ((uid-init_uid), symbol))
        
        dump_crit(sheet, entry_crit, runtime_config, market_condition)        
        
        
    def _map_df_to_sheet(self, df, sheet, uid, symbol):    
                    
        report_date = get_next_earning_date(symbol)
            
        for index, row in df.iterrows():
        
            uid += 1
            
            sheet.update_cell(sheet.STRATEGY, uid, value = row.STRATEGY)                                        
            sheet.update_cell(sheet.SYMBOL, uid, value=row.SYMBOL, font_bold=True)  
            if report_date != None:
                sheet.update_cell(sheet.EARNING_DATE, uid, value = report_date.strftime("%m-%d-%y"))

            if math.isnan(row.SPREAD) == False:
                sheet.update_cell(sheet.SPREAD, uid, value=row.SPREAD)                
                
            #if Type == 'Call':
            #    font_color = SEA_GREEN    
            #else:
            #    font_color = LIGHT_CORAL

            if math.isnan(row.P1SK) == False:
                sheet.update_cell(sheet.P1SK, uid, value =  "{:.1f}".format(row.P1SK))
                sheet.update_cell(sheet.P1SP, uid, value =  "{:.1f}".format(row.P1SP))
                sheet.update_cell(sheet.P1SK, uid, value =  row.P1ST)

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
            sheet.update_cell(sheet.WIN_PROB, uid, value = "{:.2f}".format(row.WIN_PROB)) 
            if math.isnan(row.MARGIN) == False:
                sheet.update_cell(sheet.PNL, uid, value = "{:.2f}".format(row.MARGIN)) 

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

        return uid
        

    def _init_data(self, symbol, runtime_config):
    
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
        s = runtime_config.trend_window_size # sample size for Mann-Kendall Trend Test
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
     
        
    def cv(self, stock_price, strike):
        return max(stock_price-strike, 0)

    def pv(self, stock_price, strike):
        return max(strike-stock_price, 0)
        
    def _proc_exp_position(self, sheet, uid, data, row):
                                 
        exp_date_index = data.index.to_list().index(row[sheet.EXP_DATE_t].tz_localize(data.index[-1].tz))                    
        quote_date = data.index[exp_date_index] #last_date_index]      
        exp_stock_price = data['Close'][row[sheet.EXP_DATE_t].tz_localize(data.index[-1].tz)]                         
        open_price = row[sheet.OPEN_PRICE_t]              
                        
        strategy = row[sheet.STRATEGY_t]
            
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
        if strategy == st.IRON_BUTTERFLY or strategy == st.REVERSE_IRON_BUTTERFLY:  
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
            logger.error('Unknown strategy %s' % strategy)
            return                                                          

        sheet.update_cell(sheet.P1SP, uid, value=row[sheet.P1SP_t]) 
        sheet.update_cell(sheet.P1LP, uid, value=row[sheet.P1LP_t]) 
        sheet.update_cell(sheet.P2SP, uid, value=row[sheet.P2SP_t]) 
        sheet.update_cell(sheet.P2LP, uid, value=row[sheet.P1LP_t]) 
                    
        pl = gain
        
        gain = 100 * gain / open_price
                            
        sheet.update_cell(sheet.GAIN, uid, value = "{:.2f}".format(gain))   
        sheet.update_cell(sheet.PL, uid, value = "{:.2f}".format(pl))             
        sheet.update_cell(sheet.EXP_PRICE, uid, value = "{:.2f}".format(exp_price))
        sheet.update_cell(sheet.LAST_PRICE, uid, value = "{:.2f}".format(exp_price))   
        
    def ov(self, op):
        if (len(op.bid) == 0 or float(op.bid) == 0.0) or (len(op.ask)==0 or float(op.ask) == 0):                                
            if len(op.lastPrice) == 0:
                return 0
            else:
                return float(op.lastPrice)
        else:
            return (float(op.bid)+float(op.ask))/2                  
                
    def _update_current_pnl(self, sheet, uid, data, x, option_chain, row, exit_crit):
                  
        quote_date = data.index[-1]
        
        exp_date = row[sheet.EXP_DATE_t].tz_localize(quote_date.tz)                     
        days_to_expire = (exp_date-quote_date).days   
        if days_to_expire <= exit_crit.days_before_expire:
            font_color = RGB.RED                                                                                       
        else:
            font_color = RGB.BLACK
            
        sheet.update_cell(sheet.EXP_DATE, uid, font_color=font_color)
        
        if row[sheet.EXP_DATE_t]!= '':                               
            earning_date = row[sheet.EARNING_DATE_t].tz_localize(data.index[-1].tz)                     
            days_to_earning = (earning_date-quote_date).days

            if days_to_earning  <= exit_crit.days_before_earning:
                font_color = RGB.RED                                                                                       
            else:
                font_color = RGB.BLACK
                
            sheet.update_cell(sheet.EARNING_DATE, uid, font_color=font_color)
                        
        stock_price = data['Close'][-1]
                                                   
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
                gain = last_price - open_price
            else:
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
                gain = last_price - open_price
            else:
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
            logger.error('Unknown strategy %s' % strategy)
            return

        pl = gain
        gain = 100 * gain / open_price                   
                                                   
        if gain >= 0 and gain >= exit_crit.stop_gain:
            font_color = RGB.SEA_GREEN
            font_bold = True

        elif gain < 0 and abs(gain) >= exit_crit.stop_loss:
            font_color = RGB.RED
            font_bold = True                                                                                          
            
        else:
            font_color = RGB.BLACK
            font_bold = False

        #print('uid %d sheet.Gain %s gain %.2f' % (uid, str(sheet.GAIN), gain))
        sheet.update_cell(sheet.PL, uid, font_color=font_color, font_bold = font_bold, value = "{:.2f}".format(pl))        
        sheet.update_cell(sheet.GAIN, uid, font_color=font_color, font_bold = font_bold, value = "{:.2f}".format(gain))
        sheet.update_cell(sheet.LAST_PRICE, uid, value = "{:.2f}".format(last_price))
                                  
        if x.trend == 'increasing':
            font_color = RGB.SEA_GREEN 
        elif x.trend == 'decreasing':
            font_color = RGB.RED  
        else:
            font_color = RGB.BLUE                  
                          
        sheet.update_cell(sheet.LAST_STOCK_PRICE, uid, value=stock_price)
        sheet.update_cell(sheet.LAST_QUOTE_DATE, uid, value=quote_date ) 
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
                        
    def load_quotes(self, pattern):
        
        df = []
        for sh in self.wb.sheets:                        
            if pattern not in sh.name:
                logger.debug('%s %s' % (pattern, sh.name))
                continue

            logger.info('loading %s' % sh.name)
            sheet = ps.positionSheet(self.wb, sheet_name=sh.name, create=False)   

            df.append(sheet.to_df())

        return pd.concat(df)

    def update_quotes(self, 
                      pattern, 
                      runtime_config = runtimeConfig(),
                      exit_crit = exitCrit()):   
       
        for sh in self.wb.sheets:            
            
            if pattern not in sh.name:
                logger.debug('%s %s' % (pattern, sh.name))
                continue
             
            logger.info('Processing %s' % sh.name)
            
            sheet = ps.positionSheet(self.wb, sheet_name=sh.name, create=False)                  

            df = sheet.to_df() 
                        
            symbol_list = df[ps.positionSheet.SYMBOL_t].unique()
            
            sheet.update_cell('AO', 8, font_bold = True, value='Exit Crit')           
            sheet.update_cell('AP', 8, font_bold = True, value='%s' % json.dumps(vars(exit_crit)))            
        
            for symbol in symbol_list:

                logger.info('Updating %s' % symbol)                                
                dfs = df[df['Symbol'] == symbol]                         
                data, x, option_chain = self._init_data(symbol, runtime_config)                        
                for rid in dfs.index:          
                    row = df.iloc[rid]          
                    uid = rid+2        
                    try:  
                        if datetime.now(timezone(at.TIMEZONE)).date() > row[sheet.EXP_DATE_t].date():  # already expired                                               
                            self._proc_exp_position(sheet, uid, data, row)                        
                        else: # get current PNL
                            self._update_current_pnl(sheet, uid, data, x, option_chain, row, exit_crit)
                    except: # wired data mean not yet processed
                        logger.error('Invalid exp date %s' % row[sheet.EXP_PRICE_t])           