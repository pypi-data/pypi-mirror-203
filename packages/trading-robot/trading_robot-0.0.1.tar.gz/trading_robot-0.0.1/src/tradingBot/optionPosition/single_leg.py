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
logger = logging.getLogger('single_leg')

class single_leg_position(core.core):
        
    def __init__(self, symbol, entry_crit=entryCrit(), runtime_config=runtimeConfig()):                
        super().__init__(symbol, entry_crit, runtime_config)        

    def get_positions(self, strategy_list):      

        if len(strategy_list) == 0:
            return self.df

        max_days_to_expire = self.runtime_config.max_days_to_expire
        entry_crit = self.entry_crit
        exp_date_list = self._get_exp_date_list(max_days_to_expire)        
        for strategy in strategy_list:             
            
            logger.info('Processing %s for %s get %d' % (strategy, self.symbol, s))   

            s = 0                              
            for exp_date in exp_date_list:          
                try:
                    call_opt = self.option_chain(exp_date.strftime("%Y-%m-%d")).calls        
                    put_opt = self.option_chain(exp_date.strftime("%Y-%m-%d")).puts  
                except:
                    logger.error('Cannot get option table for expiration date %s' % exp_date.strftime("%Y-%m-%d"))
                    continue
                    
                df = self.df.append(pd.Series(dtype='float64'), ignore_index=True)                 
                self.np = df.iloc[-1]
                self.np.STRATEGY = strategy
                self.np.SYMBOL=self.symbol            
                self.np.INIT_TREND = self.trend.trend
                self.np.INIT_SLOPE = self.trend.slope            
                self.np.TRADE_STOCK_PRICE = self.stock_price
                self.np.TRADE_DATE = self.trade_date                    
                self.predList = predicted_list(self.symbol, self.data, exp_date) 
                self.np.EXP_DATE = exp_date             
                
                strike = self.set_strike()
                if math.isnan(strike):
                    continue
    
                open_price = self.set_open_price(call_opt, put_opt)
                if math.isnan(open_price):
                    continue
                    
                delta = self.set_delta()
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
        
        if strategy == st.LONG_CALL:
            if trend == 'decreasing':
                logger.debug('%s %s Trend not favored %s' %(self.symbol, strategy, self.trend.trend))                    
                return np.nan

            strike = BSCallStrikeFromDelta(stock_price, trade_date, exp_date, 
                                              sigma=self.sigma, delta=self.entry_crit.min_delta_for_long)

            strike = strike - (strike%5)        
            
            self.np.P1LK = strike
            self.np.P1LT = at.CALL
              
        elif strategy  ==  st.LONG_PUT:            
            if trend == 'inccreasing':
                logger.debug('%s %s Trend not favored %s' %(symbol, strategy, trend.trend))                    
                return np.nan   

            strike = BSPutStrikeFromDelta(stock_price, trade_date, exp_date, 
                                              sigma=self.sigma, delta=self.entry_crit.min_delta_for_long) 
            strike = strike + (5-strike%5) 

            self.np.P1LK = strike
            self.np.P1LT = at.PUT            
            
        elif strategy  ==  st.COVERED_CALL:            
            if trend == 'inccreasing':
                logger.debug('%s %s Trend not favored %s' %(symbol, strategy, trend.trend))                    

                return np.nan   

            strike = BSCallStrikeFromDelta(stock_price, trade_date, exp_date, 
                                              sigma=self.sigma, delta=self.entry_crit.max_delta_for_short)

            strike = strike + (5-strike%5)
            
            self.np.P1SK = strike
            self.np.P1ST = at.CALL              

        elif strategy  ==  st.SHORT_PUT:
            if trend == 'increasing':
                logger.debug('%s %s Trend not favored %s' %(symbol, strategy, trend))                    
                return np.nan

            strike = BSPutStrikeFromDelta(stock_price, trade_date, exp_date, 
                                              sigma=self.sigma, delta=self.entry_crit.max_delta_for_short)

            strike = trike = strike + (5-strike%5)
            
            self.np.P1SK = strike
            self.np.P1ST = at.PUT                
        else:
            logger.error('Unknown strategy %s' %strategy)                    
            
            strike = np.nan
        
        return strike
    
    
    def set_open_price(self, call_opt, put_opt):
        
        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL           
        
        if strategy ==  st.LONG_CALL:  
            op = call_opt.loc[call_opt['strike']==self.np.P1LK]  
            strike = self.np.P1LK            
        elif strategy ==  st.COVERED_CALL:
            op = call_opt.loc[call_opt['strike']==self.np.P1SK]  
            strike = self.np.P1SK
        elif strategy ==  st.LONG_PUT:
            op = put_opt.loc[put_opt['strike']==self.np.P1LK] 
            strike = self.np.P1LK
        elif strategy == st.SHORT_PUT:
            op = put_opt.loc[put_opt['strike']==self.np.P1SK] 
            strike = self.np.P1SK
        else:
            logger.error('Unknown strategy %s' % strategy)
            return np.nan
            
        if len(op.ask) == 0 or len(op.bid) == 0:
            logger.debug('%s open quote not found for strike %.2f' % (strategy, strike))                              
            return np.nan

        if float(op.volume) < self.entry_crit.min_opt_vol:   
            logger.debug('%s volumn %.2f less than crit.min_return min_opt_vol %d' %
                     (strategy, (float(op.volume), self.entry_crit.min_opt_vol)))                

            return np.nan

        if float(op.bid) == 0 or float(op.ask) == 0:
            open_price = float(op.lastPrice)
        else:
            open_price = (float(op.bid)+float(op.ask))/2

        self.op = op
        
        self.np.OPEN_PRICE = open_price
        self.np.INIT_impliedVolatility = op.impliedVolatility 
        self.np.INIT_volume = op.volume       
        self.np.INIT_openInterest = op.openInterest       

        if strategy ==  st.LONG_CALL or strategy ==  st.LONG_PUT:
            op = call_opt.loc[call_opt['strike']==self.np.P1LK]  
            self.np.P1LP = open_price            
        elif strategy ==  st.COVERED_CALL or strategy == st.SHORT_PUT:
            op = put_opt.loc[put_opt['strike']==self.np.P1LK] 
            self.np.P1SP = open_price

        return open_price    
    
    def set_delta(self):

        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL
        open_price = self.np.OPEN_PRICE
        
        days_to_expire = (exp_date-trade_date.tz_localize(None)).days             
        
        if math.isnan(open_price):
            self.np.INIT_DELTA = delta            
            return np.nan
            
        if strategy  ==  st.LONG_CALL:            
            c = mibian.BS([stock_price, self.np.P1LK, 0.05, days_to_expire], callPrice=open_price)
            c = mibian.BS([stock_price, self.np.P1LK, 0.05, days_to_expire], volatility = c.impliedVolatility)
            delta = c.callDelta            
            if abs(delta) < self.entry_crit.min_delta_for_long:
                logger.debug('%s delta %.2f less than crit.min_delta_for_long %.2f' % 
                             (strategy, delta, self.entry_crit.min_delta_for_long))                       
                return np.nan            
        elif strategy  ==  st.COVERED_CALL:
            c = mibian.BS([stock_price, self.np.P1SK, 0.05, days_to_expire], callPrice=open_price)
            c = mibian.BS([stock_price, self.np.P1SK, 0.05, days_to_expire], volatility = c.impliedVolatility)
            delta = c.callDelta            
            if abs(delta) > self.entry_crit.max_delta_for_short:
                logger.debug('%s delta %.2f greater than crit.max_delta_for_short %.2f' % 
                             (strategy, delta, self.entry_crit.max_delta_for_short))                       
                return np.nan              
        elif strategy  ==  st.LONG_PUT:
            p = mibian.BS([stock_price, self.np.P1LK, 0.05, days_to_expire], putPrice= open_price)
            p = mibian.BS([stock_price, self.np.P1LK, 0.05, days_to_expire], volatility= p.impliedVolatility)
            delta = p.putDelta 
            if abs(delta) < self.entry_crit.min_delta_for_long:                   
                logger.debug('%s delta %.2f less than crit.min_delta_for_long %.2f' % 
                             (strategy, delta, self.entry_crit.min_delta_for_long))                                           
                return np.nan                           
        elif strategy  ==  st.SHORT_PUT:
            p = mibian.BS([self.stock_price, self.np.P1SK, 0.05, days_to_expire], putPrice= open_price)
            p = mibian.BS([self.stock_price, self.np.P1SK, 0.05, days_to_expire], volatility= p.impliedVolatility)
            delta = p.putDelta 
            if abs(delta) > self.entry_crit.max_delta_for_short:                   
                logger.debug('%s delta %.2f greater than crit.max_delta_for_short %.2f' % 
                             (strategy, delta, self.entry_crit.max_delta_for_short))                                           
                return np.nan   
        else:
            logger.error('Unknown strategy %s' % strategy) 
            return np.nan
        
        self.np.INIT_DELTA = delta     

        return delta    


    def set_max_profit(self):
        
        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL
        open_price = self.np.OPEN_PRICE        

        if strategy ==  st.LONG_CALL:
            max_profit = np.nan
            max_loss = open_price
            pnl = np.nan
            self.np.BREAKEVEN_L = breakeven = stock_price - open_price
            win_prob = calc_prob_higher_than(self.predList, breakeven)         
            self.np.MARGIN = np.nan            
        elif strategy ==  st.LONG_PUT:            
            max_profit = stock_price - open_price
            max_loss = open_price  
            pnl = max_profit / max_loss
            self.np.BREAKEVEN_H = breakeven = stock_price-open_price
            win_prob = calc_prob_lower_than(self.predList, breakeven)         
            self.np.MARGIN = np.nan               
        elif strategy ==  st.COVERED_CALL:
            max_profit = open_price
            max_loss = stock_price-open_price       
            pnl = np.nan
            self.BREAKEVEN_H = breakeven = stock_price+open_price
            win_prob = calc_prob_lower_than(self.predList, breakeven)          
            self.np.MARGIN = np.nan               
        elif strategy ==  st.SHORT_PUT:
            max_profit = open_price
            max_loss = stock_price - open_price     
            pnl = max_profit / max_loss
            self.BREAKEVEN_L = breakeven = stock_price-open_price
            win_prob = calc_prob_higher_than(self.predList, breakeven)
            self.np.MARGIN = stock_price               
        else:
            logger.error('Unknown strategy %s' % strategy)
            return np.nan

        if win_prob < self.entry_crit.min_chance_of_win:                    
            logger.debug('%s open price %.2f win_prob %.2f less than crit.min_chance_of_win %.2f' %
                     (strategy, open_price, win_prob, self.entry_crit.min_chance_of_win))                    
            return np.nan
        
        self.np.PNL = pnl
        self.np.MAX_PROFIT = max_profit
        self.np.MAX_LOSS = max_loss
        self.np.WIN_PROB = win_prob

        return max_profit