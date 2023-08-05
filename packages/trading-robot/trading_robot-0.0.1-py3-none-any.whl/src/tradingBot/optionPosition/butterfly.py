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
from tradingBot.utils.calcProb import calc_prob_between

import tradingBot.consts.strategy as st
import tradingBot.consts.asset as at

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('butterfly')

class butterfly_position(core.core):
    
    def __init__(self, symbol, entry_crit=entryCrit(), runtime_config=runtimeConfig()):                
        super().__init__(symbol, entry_crit, runtime_config)        
        
    def get_positions(self, strategy_list):        

        if len(strategy_list) == 0:
            return self.df      

        trend = self.trend.trend
        slope = self.trend.slope
        entry_crit = self.entry_crit
        spreads =  self.runtime_config.spreads
        max_days_to_expire = self.runtime_config.max_days_to_expire
        
        #if trend == 'increasing' or trend == 'decreasing':
        #    if abs(slope) > entry_crit.max_slope:
        #        logger.debug('Skip buttefly as slope %.2f large than max_slope %.2f' % (slope, entry_crit.max_slope))
        #        return
            
        exp_date_list = self._get_exp_date_list(max_days_to_expire)        
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
                    #logger.debug('Processing spread %.2f' % spread)                        
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
                    
                    lk, mk, hk = self.set_strike()
                    if math.isnan(lk):
                        continue

                    lprice, mprice, hprice, cmprice = self.set_open_price(lk, mk, hk, call_opt, put_opt)
                    if math.isnan(lprice):
                        continue
                    
                    delta = self.set_delta(lk, mk, hk, lprice, mprice, hprice, cmprice)
                    if math.isnan(delta):
                        continue                    

                    max_profit = self.set_max_profit(spread, lk, hk)
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
        trend = self.np.INIT_TREND
        spread = self.np.SPREAD
        
        if trend == 'decreasing':
            mid_strike = stock_price  -  (stock_price%5)
        else:
            mid_strike = stock_price  +  (5-(stock_price % 5))
            
        low_strike = mid_strike - spread
        
        high_strike = mid_strike + spread
        
        if strategy == st.CREDIT_CALL_BUTTERFLY or strategy == st.CREDIT_PUT_BUTTERFLY:
            self.np.P1SK = low_strike 
            self.np.P1LK = mid_strike
            self.np.P2LK = mid_strike 
            self.np.P2SK = high_strike 
            self.np.MARGIN = self.np.SPREAD                
        elif strategy ==  st.DEBIT_CALL_BUTTERFLY or strategy == st.DEBIT_PUT_BUTTERFLY:   
            self.np.P1LK = low_strike 
            self.np.P1SK = mid_strike 
            self.np.P2SK = mid_strike 
            self.np.P2LK = high_strike 
            self.np.MARGIN = np.nan               
        elif strategy == st.IRON_BUTTERFLY:
            self.np.P1SK = low_strike 
            self.np.P1LK = mid_strike 
            self.np.P2LK = mid_strike 
            self.np.P2SK = high_strike  
            self.np.MARGIN = self.np.SPREAD               
        elif strategy == st.REVERSE_IRON_BUTTERFLY:   
            self.np.P1LK = low_strike 
            self.np.P1SK = mid_strike 
            self.np.P2SK = mid_strike 
            self.np.P2LK = high_strike         
            self.np.MARGIN = np.nan
        else:
            logger.error('Unknown strategy %s' % strategy)
            return [np.nan, np.nan, np.nan]             

        '''
        The iron butterfly strategy is a member of a group of option strategies known as 
        “wingspreads” because each strategy is named after a flying creature like a butterfly 
        or condor. The strategy is created by combining a bear call spread with a bull put spread 
        with an identical expiration date that converges at a middle strike price. 
        A short call and put are both sold at the middle strike price, which forms the “body” 
        of the butterfly, and a call and put are purchased above and below the middle strike price, 
        respectively, to form the “wings.”
        '''                
        logger.debug('lk %.2f mk %.2f hk %.2f' %  (low_strike, mid_strike, high_strike))
        
        return [low_strike, mid_strike, high_strike]
        
    
    def set_open_price(self, lk, mk, hk, call_opt, put_opt):
        
        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL           
        entry_crit = self.entry_crit
        
        cmprice = np.nan
        if strategy == st.CREDIT_CALL_BUTTERFLY or strategy ==  st.DEBIT_CALL_BUTTERFLY:
            lo = call_opt.loc[call_opt['strike']==lk]
            mo = call_opt.loc[call_opt['strike']==mk]
            ho = call_opt.loc[call_opt['strike']==hk]             
            self.np.P1ST = at.CALL
            self.np.P1LT = at.CALL 
            self.np.P2ST = at.CALL 
            self.np.P2LT = at.CALL             
        elif strategy == st.CREDIT_PUT_BUTTERFLY or strategy == st.DEBIT_PUT_BUTTERFLY:   
            lo = put_opt.loc[put_opt['strike']==lk]
            mo = put_opt.loc[put_opt['strike']==mk]
            ho = put_opt.loc[put_opt['strike']==hk] 
            self.np.P1ST = at.PUT 
            self.np.P1LT = at.PUT  
            self.np.P2ST = at.PUT  
            self.np.P2LT = at.PUT                                                 
        elif strategy == st.IRON_BUTTERFLY or strategy == st.REVERSE_IRON_BUTTERFLY:          
            lo = put_opt.loc[put_opt['strike']==lk]
            mo = put_opt.loc[put_opt['strike']==mk]
            cmo = call_opt.loc[call_opt['strike']==mk]                
            ho = call_opt.loc[call_opt['strike']==hk]                            
            if cmo.empty:
                logger.debug('Not call option quote for %.2f' % mk)                
                return [np.nan, np.nan, np.nan, np.nan]  
            
            if len(cmo.volume) == 0 or float(cmo.volume) < entry_crit.min_opt_vol:              
                logger.debug('call strike %.2f volumn %.2f less than crit.min_return min_opt_vol %d' %
                         (mid_strike, float(cmo.volume), entry_crit.min_opt_vol))                                    
                return [np.nan, np.nan, np.nan, np.nan]                

            if float(cmo.bid) == 0.0 or float(cmo.ask) == 0:
                cmprice = float(cmo.lastPrice)
            else:
                cmprice = ((float(cmo.bid)+float(cmo.ask))/2)                        
            self.np.P1ST = at.PUT 
            self.np.P1LT = at.PUT  
            self.np.P2ST = at.CALL 
            self.np.P2LT = at.CALL                 
        else:
            logger.error('Unknow strategy %s' % strategy)
            return [np.nan, np.nan, np.nan, np.nan]  

        if lo.empty:
            logger.debug('Empty lo for %.2f' % lk)

        if mo.empty:
            logger.debug('Empty mo for %.2f' % mk)

        if ho.empty:
            logger.debug('Empty ho for %.2f' % hk)
            
        if lo.empty or mo.empty or ho.empty:    
            return [np.nan, np.nan, np.nan, np.nan]            

        if float(lo.volume) < entry_crit.min_opt_vol or \
            float(mo.volume) < entry_crit.min_opt_vol or \
            float(ho.volume) < entry_crit.min_opt_vol:              
            logger.debug('strike %.2f l vol %.2f m vol %.2f h vol %.2f less than crit.min_return min_opt_vol %d' %
                     (id_strike, float(lo.volume), float(mo.volume), float(ho.volume), entry_crit.min_opt_vol))                                    
            return [np.nan, np.nan, np.nan, np.nan]       

        if float(lo.bid) == 0.0 or float(lo.ask) == 0:
            lprice = float(lo.lastPrice)
        else:
            lprice = ((float(lo.bid)+float(lo.ask))/2)    

        if float(mo.bid) == 0.0 or float(mo.ask) == 0:
            mprice = float(mo.lastPrice)
        else:
            mprice = ((float(mo.bid)+float(mo.ask))/2)  

        if float(ho.bid) == 0.0 or float(ho.ask) == 0.0:
            hprice = float(ho.lastPrice)
        else:
            hprice = ((float(ho.bid)+float(ho.ask))/2) 
                                                      

        if strategy == st.IRON_BUTTERFLY or strategy == st.REVERSE_IRON_BUTTERFLY:          
            open_price = abs(mprice-lprice) + abs(cmprice-hprice)
        else:
            open_price = abs(lprice + hprice - (2 * mprice))      
            
        logger.debug('oprice %.2f lprice %.2f mprice %.2f hrice %.2f cmprice %.2f' % 
                     (open_price, lprice, mprice, hprice, cmprice))
            
        if open_price < 0:
            open_price = 0    
                                    
        self.np.OPEN_PRICE = open_price
        self.np.INIT_impliedVolatility = float(mo.impliedVolatility) 
        self.np.INIT_volume = float(mo.volume)       
        self.np.INIT_openInterest = float(mo.openInterest)       

        if strategy == st.CREDIT_CALL_BUTTERFLY or strategy == st.CREDIT_PUT_BUTTERFLY:
            self.np.P1SP = lprice 
            self.np.P1LP = mprice
            self.np.P2LP = mprice 
            self.np.P2SP = hprice 
            self.np.MARGIN = self.np.SPREAD                
        elif strategy ==  st.DEBIT_CALL_BUTTERFLY or strategy == st.DEBIT_PUT_BUTTERFLY:   
            self.np.P1LP = lprice
            self.np.P1SP = mprice 
            self.np.P2SP = mprice 
            self.np.P2LP = hprice 
            self.np.MARGIN = np.nan               
        elif strategy == st.IRON_BUTTERFLY:
            self.np.P1SP = lprice
            self.np.P1LP = mprice 
            self.np.P2LP = cmprice 
            self.np.P2SP = hprice  
            self.np.MARGIN = self.np.SPREAD               
        elif strategy == st.REVERSE_IRON_BUTTERFLY:   
            self.np.P1LP = lprice
            self.np.P1SP = mprice 
            self.np.P2SP = cmprice 
            self.np.P2LP = hprice         
            self.np.MARGIN = np.nan                   
        else:
            logger.error('Invalud strategy %s' % strategy)
            return np.nan, np.nan, np.nan, np.nan 

        return lprice, mprice, hprice, cmprice    
    
    def set_delta(self, lk, mk, hk, lprice, mprice, hprice, cmprice):

        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL
        open_price = self.np.OPEN_PRICE
        entry_crit = self.entry_crit
        
        days_to_expire = (exp_date-trade_date.tz_localize(None)).days       
        
        if strategy == st.CREDIT_CALL_BUTTERFLY or strategy ==  st.DEBIT_CALL_BUTTERFLY:            
            if math.isnan(mprice):
                sd = np.nan
            else:
                c = mibian.BS([stock_price, mk, 0.05, days_to_expire], callPrice=mprice)
                c = mibian.BS([stock_price, mk, 0.05, days_to_expire], volatility = c.impliedVolatility)
                sd = c.callDelta           
        elif strategy == st.CREDIT_PUT_BUTTERFLY or strategy == st.DEBIT_PUT_BUTTERFLY:   
            if math.isnan(mprice):
                sd = np.nan
            else:
                p = mibian.BS([stock_price, mk, 0.05, days_to_expire], putPrice= mprice)
                p = mibian.BS([stock_price, mk, 0.05, days_to_expire], volatility= p.impliedVolatility)
                sd = p.putDelta           
        elif strategy == st.IRON_BUTTERFLY or strategy == st.REVERSE_IRON_BUTTERFLY: 
            if math.isnan(mprice):
                sd = np.nan
            else:
                p = mibian.BS([stock_price, mk, 0.05, days_to_expire], putPrice= mprice)
                p = mibian.BS([stock_price, mk, 0.05, days_to_expire], volatility= p.impliedVolatility)
                sd = p.putDelta            
                logger.debug('%s k %.2f days %d op %.2f' %(strategy, mk, days_to_expire, mprice))
            if math.isnan(cmprice):
                sd = np.nan
            else:
                c = mibian.BS([stock_price, mk, 0.05, days_to_expire], callPrice= cmprice)
                c = mibian.BS([stock_price, mk, 0.05, days_to_expire], volatility= c.impliedVolatility)
                csd = c.putDelta              
                if abs(csd) > entry_crit.max_delta_for_short:                   
                    logger.debug('call delta %.2f greater than crit.max_delta_for_short %.2f' % (sd, entry_crit.max_delta_for_short))                                           
                    return np.nan             
           
        #logger.debug('%s k %.2f days %d op %.2f delta %.2f' %(strategy, mk, days_to_expire, mprice, sd))
        
        if strategy == st.CREDIT_CALL_BUTTERFLY or\
                strategy ==  st.CREDIT_PUT_BUTTERFLY or\
                strategy == st.REVERSE_IRON_BUTTERFLY:           
            if abs(sd) > entry_crit.max_delta_for_short:                   
                logger.debug('%s delta %.2f greater than crit.max_delta_for_short %.2f' % 
                            (strategy, sd, entry_crit.max_delta_for_short))                                           
                return np.nan           
        else:
             if abs(sd) < entry_crit.min_delta_for_long:                   
                logger.debug('%s delta %.2f less than crit.min_delta_for_long %.2f' % 
                            (strategy, sd, entry_crit.min_delta_for_long))                                           
                return np.nan             

                                        
        self.np.INIT_DELTA = sd
        
        return sd    


    def set_max_profit(self, spread, lk, hk):
        
        strategy = self.np.STRATEGY
        open_price = self.np.OPEN_PRICE        
        predList = self.predList
        entry_crit = self.entry_crit        
        
        if strategy == st.CREDIT_CALL_BUTTERFLY or\
            strategy ==  st.CREDIT_PUT_BUTTERFLY:        
            max_loss = spread-open_price
            max_profit = open_price   
            breakeven_l = lk + max_loss
            breakeven_h = hk - max_loss      
            win_prob = 100-calc_prob_between(predList, lk, hk)               
        elif strategy == st.DEBIT_CALL_BUTTERFLY or\
            strategy ==  st.DEBIT_PUT_BUTTERFLY:
            max_loss = open_price             
            max_profit = spread-open_price
            breakeven_l = lk + max_profit
            breakeven_h = hk - max_profit    
            win_prob = calc_prob_between(predList, lk, hk)                 
        elif  strategy == st.IRON_BUTTERFLY:
            max_loss = spread-open_price
            max_profit = open_price     
            breakeven_l = lk + max_loss
            breakeven_h = hk - max_loss      
            win_prob = calc_prob_between(predList, lk, hk)  
        elif  strategy == st.REVERSE_IRON_BUTTERFLY:
            max_loss = open_price
            max_profit = spread-open_price   
            breakeven_l = lk + max_profit
            breakeven_h = hk - max_profit      
            win_prob = 100 - calc_prob_between(predList, lk, hk)  
        else:
            logger.error('Unknown strategy %s' % strategy)
            return np.nan
            
        if max_loss == 0:
            logger.error('max loss == 0')
            return np.nan
            
        pnl = max_profit / max_loss

        if pnl < entry_crit.min_pnl:
            logger.debug('open price %.2f pnl %.2f less than crit.min_pnl %.2f' %
                          (open_price, pnl, entry_crit.min_pnl))                                                               
            return np.nan
                      
        if win_prob < entry_crit.min_chance_of_win:
            logger.debug('open price %.2f, win_prob %.2f less then crit.min_chance_of_win %.2f' %
                     (open_price, win_prob, entry_crit.min_chance_of_win))
            return np.nan   
                            
        self.np.PNL = pnl
        self.np.MAX_PROFIT = max_profit
        self.np.MAX_LOSS = max_loss
        self.np.WIN_PROB = win_prob
        self.np.BREAKEVEN_L = breakeven_l
        self.np.BREAKEVEN_H = breakeven_h
        
        logger.debug('pnl %.2f m profit %.2f m loss %.2f win prob %.2f' %
                    (pnl, max_profit, max_loss, win_prob))

        return max_profit