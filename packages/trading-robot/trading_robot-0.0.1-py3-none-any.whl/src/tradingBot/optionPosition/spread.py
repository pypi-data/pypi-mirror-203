import pandas as pd
import numpy as np
import math
import mibian

from tradingBot.optionPosition import core

from tradingBot.settings.tradeConfig import entryCrit
from tradingBot.settings.tradeConfig import runtimeConfig

from tradingBot.utils.optionTool import BSCallStrikeFromDelta
from tradingBot.utils.optionTool import BSPutStrikeFromDelta

from tradingBot.utils.calcProb import predicted_list
from tradingBot.utils.calcProb import calc_prob_higher_than
from tradingBot.utils.calcProb import calc_prob_lower_than

import tradingBot.consts.strategy as st
import tradingBot.consts.asset as at

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('spread')

class spread_position(core.core):
    
    def __init__(self, symbol, entry_crit=entryCrit(), runtime_config=runtimeConfig()):                
        super().__init__(symbol, entry_crit, runtime_config)        
        
    def get_positions(self, strategy_list):     

        if len(strategy_list) == 0:
            return self.df


        max_days_to_expire = self.runtime_config.max_days_to_expire        
        exp_date_list = self._get_exp_date_list(max_days_to_expire)        
        spreads = self.runtime_config.spreads

        entry_crit = self.entry_crit
                
        for strategy in strategy_list:          
                           
            s = 0
            for exp_date in exp_date_list:           
                try:
                    call_opt = self.option_chain(exp_date.strftime("%Y-%m-%d")).calls        
                    put_opt = self.option_chain(exp_date.strftime("%Y-%m-%d")).puts  
                except:
                    logger.error('Cannot get option table for expiration date %s' % exp_date.strftime("%Y-%m-%d"))
                    continue
   
                self.predList = predicted_list(self.symbol, self.data, exp_date)  
    
                for spread in spreads:
                    df = self.df.append(pd.Series(dtype='float64'), ignore_index=True)                 
                    self.np = df.iloc[-1]
                    self.np.STRATEGY = strategy
                    self.np.SYMBOL=self.symbol            
                    self.np.INIT_TREND = self.trend.trend
                    self.np.INIT_SLOPE = self.trend.slope            
                    self.np.TRADE_STOCK_PRICE = self.stock_price
                    self.np.TRADE_DATE = self.trade_date                      
                    self.np.EXP_DATE = exp_date                    
                    self.np.SPREAD = spread
                
                    lk, sk = self.set_strike()
                    if math.isnan(lk):
                        continue

                    so_price, lo_price = self.set_open_price(call_opt, put_opt)
                    if math.isnan(so_price):
                        continue                        
                    
                    delta = self.set_delta(lo_price, so_price)
                    if math.isnan(delta):
                        continue                    
                    
                    max_profit = self.set_max_profit()
                    if math.isnan(max_profit):
                        continue
                    s = s + 1
                    self.df = df        

            logger.info('Processing %s for %s get %d' % (strategy, self.symbol, s))   

        return self.df
                            
    def set_strike(self):        
        
        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL
        trend = self.np.INIT_TREND
        slope = self.np.INIT_SLOPE
        spread = self.np.SPREAD
        entry_crit = self.entry_crit        
        
        if strategy ==  st.CREDIT_CALL_SPREAD:
            if trend == 'increasing' and abs(slope) > entry_crit.max_slope:
                logger.debug('%s %s Trend not favored %s slope %.2f' %(symbol, strategy, trend, slope))                
                return [np.nan, np.nan]   

            osk = BSCallStrikeFromDelta(stock_price, trade_date, exp_date, 
                                              sigma=self.sigma, delta=self.entry_crit.max_delta_for_short)

            if trend == 'decreasing':
                sk = osk - (osk % 5)
            else:
                sk = osk + (5-(osk%5))                    

            lk = sk + spread
            
        elif strategy ==  st.CREDIT_PUT_SPREAD:            
            if trend == 'decreasing' and abs(slope) > entry_crit.max_slope:
                logger.debug('%s %s Trend not favored %s slope %.2f' %(symbol, strategy, trend, slope))                    
                return [np.nan, np.nan]   
            
            osk = BSPutStrikeFromDelta(stock_price, trade_date, exp_date, 
                                          sigma=self.sigma, delta=self.entry_crit.max_delta_for_short)
            if trend == 'increasing': 
                sk = osk + (5-(osk%5))    
            else:
                sk = osk - (osk%5)             
                
            lk = sk - spread 
            
        elif strategy ==  st.DEBIT_CALL_SPREAD:                    
            if trend == 'decreasing' and abs(slope) > entry_crit.max_slope:
                logger.debug('%s %s Trend not favored %s slope %.2f' %(symbol, strategy, trend, slope))
                return [np.nan, np.nan]   

            olk = BSCallStrikeFromDelta(stock_price, trade_date, exp_date, 
                                          sigma=self.sigma, delta=self.entry_crit.min_delta_for_long) 
            if trend == 'increasing':
                lk = olk + (5- (olk%5))
            else:
                lk = olk - ( olk%5)   
            sk = lk + spread 


        elif strategy ==  st.DEBIT_PUT_SPREAD:
            if trend == 'increasing' and abs(slope) > entry_crit.max_slope:            
                logger.debug('%s %s Trend not favored %s slope %.2f' %(symbol, strategy, trend, slope)) 
                return [np.nan, np.nan]   

            olk = BSPutStrikeFromDelta(stock_price, trade_date, exp_date, 
                                          sigma=self.sigma, delta=self.entry_crit.min_delta_for_long)
            
            if trend == 'decreasing':                
                lk = olk + (spread - (olk%5))                   
            else:
                lk = olk - (olk%5)

            sk = lk - spread
        else:
            logger.error('Unknown strategy %s' % strategy)
                           

        self.np.P1LK = lk
        self.np.P1SK = sk
        
        return [lk, sk]
    
    
    def set_open_price(self, call_opt, put_opt):
        
        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL        
        entry_crit = self.entry_crit        
        sk = self.np.P1SK
        lk = self.np.P1LK
        spread = self.np.SPREAD
        
        if strategy ==  st.CREDIT_CALL_SPREAD:
            lo = call_opt.loc[call_opt['strike']==lk]
            so = call_opt.loc[call_opt['strike']==sk]     
            self.np.P1ST = at.CALL
            self.np.P1LT = at.CALL                             
            self.np.MARGIN = spread              
            op = so
        elif strategy ==  st.CREDIT_PUT_SPREAD:            
            lo = put_opt.loc[put_opt['strike']==lk]
            so = put_opt.loc[put_opt['strike']==sk]
            self.np.P1ST = at.PUT
            self.np.P1LT = at.PUT                       
            self.np.MARGIN = spread                
            op = so
        elif strategy ==  st.DEBIT_CALL_SPREAD:                    
            lo = call_opt.loc[call_opt['strike']==lk]
            so = call_opt.loc[call_opt['strike']==sk]
            self.np.P1ST = at.CALL
            self.np.P1LT = at.CALL           
            self.np.MARGIN = np.nan                  
            op = lo
        elif strategy ==  st.DEBIT_PUT_SPREAD:
            lo = put_opt.loc[put_opt['strike']==lk]
            so = put_opt.loc[put_opt['strike']==sk]
            self.np.P1ST = at.PUT
            self.np.P1LT = at.PUT               
            self.np.MARGIN = np.nan                 
            op = lo
        else:
            logger.error('Unknown strategy %s' % strategy)            
            return [np.nan, np.nan]
            
        if len(so.bid) == 0 or len(lo.bid) == 0:
            logger.debug('cannot found option quote for %.2f [%d] or %.2f [%d]' % (sk, len(so.bid), lk, len(lo.bid)))                    
            return [np.nan, np.nan]

        if float(so.volume) < self.entry_crit.min_opt_vol or float(lo.volume) < self.entry_crit.min_opt_vol:              
            logger.debug('volumn s %.2f l %.2f less than crit.min_return min_opt_vol %d' %
                     ((float(so.volume), float(lo.volume), self.entry_crit.min_opt_vol)))                
            return [np.nan, np.nan]

        if float(so.bid) == 0.0 or float(so.ask) == 0.0:
            so_price = float(so.lastPrice)
        else:
            so_price = (float(so.bid)+float(so.ask))/2
                        
        if float(lo.bid) == 0.0 or float(lo.ask) == 0.0:
            lo_price = float(lo.lastPrice)     
        else:
            lo_price = (float(lo.bid)+float(lo.ask))/2                 
 
        open_price = abs(so_price - lo_price)
                        
        self.np.OPEN_PRICE = open_price
        self.np.INIT_impliedVolatility = float(op.impliedVolatility) 
        self.np.INIT_volume = float(op.volume)       
        self.np.INIT_openInterest = float(op.openInterest)       

        self.np.P1SP = so_price
        self.np.P1LP = lo_price

        return so_price, lo_price    
    
    def set_delta(self, so_price, lo_price):

        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL
        open_price = self.np.OPEN_PRICE
        entry_crit = self.entry_crit        
        sk = self.np.P1SK
        lk = self.np.P1LK

        
        days_to_expire = (exp_date-trade_date.tz_localize(None)).days             

        if strategy ==  st.CREDIT_CALL_SPREAD:

            if math.isnan(so_price):
                logger.debug('%s so price is nan' % strategy)
                return np.nan
            
            d = mibian.BS([stock_price, sk, 0.05, days_to_expire], callPrice=so_price)
            d = mibian.BS([stock_price, sk, 0.05, days_to_expire], volatility = d.impliedVolatility)                         
            delta = d.callDelta   
            if delta > entry_crit.max_delta_for_short:                   
                logger.debug('delta %.2f greater than crit.max_delta_for_short %.2f' % (delta, entry_crit.max_delta_for_short))                                           
                return np.nan               
        elif strategy ==  st.CREDIT_PUT_SPREAD:
            if math.isnan(so_price):
                logger.debug('%s so price is nan' % strategy)
                return np.nan            
            d = mibian.BS([stock_price, sk, 0.05, days_to_expire], putPrice= so_price)
            d = mibian.BS([stock_price, sk, 0.05, days_to_expire], volatility= d.impliedVolatility)          
            delta = d.putDelta 
            if delta > entry_crit.max_delta_for_short:                   
                logger.debug('delta %.2f greater than crit.max_delta_for_short %.2f' % (delta, entry_crit.max_delta_for_short))                                           
                return np.nan               
        elif strategy ==  st.DEBIT_CALL_SPREAD:   
            if math.isnan(lo_price):
                logger.debug('%s so price is nan' % strategy)
                return np.nan             
            d = mibian.BS([stock_price, lk, 0.05, days_to_expire], callPrice=lo_price)
            d = mibian.BS([stock_price, lk, 0.05, days_to_expire], volatility = d.impliedVolatility)
            delta = d.callDelta
            if abs(delta) < entry_crit.min_delta_for_long:
                logger.debug('delta %.2f less than crit.min_delta_for_long %.2f' % (delta, entry_crit.min_delta_for_long))                       
                return np.nan              
        elif strategy ==  st.DEBIT_PUT_SPREAD:
            if math.isnan(lo_price):
                logger.debug('%s so price is nan' % strategy)
                return np.nan              
            d = mibian.BS([stock_price, lk, 0.05, days_to_expire], putPrice= lo_price)
            d = mibian.BS([stock_price, lk, 0.05, days_to_expire], volatility= d.impliedVolatility)                
            delta = d.putDelta
            if abs(delta) < entry_crit.min_delta_for_long:
                logger.debug('delta %.2f less than crit.min_delta_for_long %.2f' % (delta, entry_crit.min_delta_for_long))                       
                return np.nan                          
        else:
            logger.error('Unknown strategy %s' % strategy)
            return np.nan
                               
        self.np.INIT_DELTA = delta   
        
        return delta    


    def set_max_profit(self):
        
        strategy = self.np.STRATEGY
        open_price = self.np.OPEN_PRICE        
        sk = self.np.P1SK
        lk = self.np.P1LK
        predList = self.predList
        spread = self.np.SPREAD
        entry_crit = self.entry_crit
        
        if strategy ==  st.CREDIT_CALL_SPREAD:
            max_profit = open_price                
            max_loss = spread-open_price
            breakeven = sk+open_price
            win_prob = calc_prob_lower_than(predList, breakeven)   
            self.np.BREAKEVEN_H = breakeven
        elif strategy ==  st.CREDIT_PUT_SPREAD:            
            max_profit = open_price                
            max_loss = spread-open_price
            breakeven = sk-open_price
            win_prob = calc_prob_higher_than(predList, breakeven)      
            self.np.BREAKEVEN_L = breakeven            
        elif strategy ==  st.DEBIT_CALL_SPREAD:                    
            max_profit = spread-open_price 
            max_loss = open_price    
            breakeven = lk+open_price
            win_prob = calc_prob_higher_than(predList, breakeven)               
            self.np.BREAKEVEN_L = breakeven                   
        elif strategy ==  st.DEBIT_PUT_SPREAD:
            max_profit = spread-open_price 
            max_loss = open_price    
            breakeven = lk+open_price
            win_prob = calc_prob_lower_than(predList, breakeven) 
            self.np.BREAKEVEN_H = breakeven            
        else:
            logger.error('Unknown strategy %s' % strategy)            
            return np.nan
                
        if win_prob < entry_crit.min_chance_of_win:                    
            logger.debug('open price %.2f win_prob %.2f less than crit.min_chance_of_win %.2f' %
                     (open_price, win_prob, entry_crit.min_chance_of_win))                    
            return np.nan                    

        if max_loss == 0:
            logger.error('max_loss == 0')
            return np.nan
                        
        pnl = max_profit / max_loss            
        if pnl < entry_crit.min_pnl:
            logger.debug('open price %.2f pnl %.2f less than crit.min_pnl %.2f' %
                      (open_price, pnl, entry_crit.min_pnl))                                                               
            return np.nan
        
        self.np.PNL = pnl
        self.np.MAX_PROFIT = max_profit
        self.np.MAX_LOSS = max_loss
        self.np.WIN_PROB = win_prob

        return max_profit