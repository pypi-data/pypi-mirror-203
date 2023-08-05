        
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

#logger = logging.getLogger('iron_condor')        
logger = logging.getLogger('iron_condor')      

class iron_condor_position(core.core):
    
    def __init__(self, symbol, entry_crit=entryCrit(), runtime_config=runtimeConfig()):                
        super().__init__(symbol, entry_crit, runtime_config)             
          
    def get_positions(self, strategy_list):   

        if len(strategy_list) == 0:
            return self.df

        trend = self.trend.trend
        slope = self.trend.slope    
        max_days_to_expire = self.runtime_config.max_days_to_expire         
        spreads = self.runtime_config.spreads
        exp_date_list = self._get_exp_date_list(max_days_to_expire)        
        entry_crit = self.entry_crit
                
        for strategy in strategy_list:        
            
            '''
            if strategy ==  st.CREDIT_IRON_CONDOR:            
                if abs(slope) > entry_crit.max_slope:
                    logger.debug('Skip credit iron condor as slope %.2f large than max_slope %.2f' % (slope, entry_crit.max_slope))
                    continue
            elif strategy ==  st.DEBIT_IRON_CONDOR:            
                if abs(slope) < entry_crit.min_slope:
                    logger.debug('Skip debit iron condor as slope %.2f smaller than min_slope %.2f' % (slope, entry_crit.min_slope))
                    continue
            '''     
            s = 0
            for exp_date in exp_date_list:           
                #logger.info('Processing exp date %s' % exp_date.strftime("%Y-%m-%d"))                
                try:
                    call_opt = self.option_chain(exp_date.strftime("%Y-%m-%d")).calls        
                    put_opt = self.option_chain(exp_date.strftime("%Y-%m-%d")).puts  
                except:
                    logger.error('Cannot get option table for expiration date %s' % exp_date.strftime("%Y-%m-%d"))
                    continue                
                    
                self.predList = predicted_list(self.symbol, self.data, exp_date) 
                    
                for spread in spreads:
                    #logger.info('Processing spread %.2f' % spread)                       
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
                    
                    psk, plk, csk, clk = self.set_strike()
                    if math.isnan(psk):
                        continue
                    
                    ps_price, pl_price, cs_price, cl_price = self.set_open_price(call_opt, put_opt)
                    if math.isnan(ps_price):
                        continue

                    self.np.P1SP = ps_price
                    self.np.P1ST = at.PUT 
                    self.np.P1LP = pl_price
                    self.np.P1LT = at.PUT
                    self.np.P2SP = cs_price
                    self.np.P2ST = at.CALL 
                    self.np.P2LP = cl_price
                    self.np.P2LT = at.CALL                                                                                      
                    
                    delta = self.set_delta(ps_price, pl_price, cs_price, cl_price)
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
        sigma = self.sigma
        spread = self.np.SPREAD
        entry_crit = self.entry_crit        

        if strategy ==  st.CREDIT_IRON_CONDOR:
            psk = BSPutStrikeFromDelta(stock_price, 
                                              trade_date, 
                                              exp_date, 
                                              sigma=sigma, 
                                              delta=self.entry_crit.max_delta_for_short)                                                                            
            csk = BSCallStrikeFromDelta(stock_price, 
                                               trade_date, 
                                               exp_date, 
                                               sigma=sigma, 
                                               delta=self.entry_crit.max_delta_for_short)                                                                                 
            psk = psk - (psk%5) 
            plk = psk - spread            
            csk = csk + (5-csk%5)                    
            clk = csk + spread                        
        elif strategy ==  st.DEBIT_IRON_CONDOR:            
            plk = BSPutStrikeFromDelta(stock_price, 
                                              trade_date, 
                                              exp_date, 
                                              sigma=sigma, 
                                              delta=self.entry_crit.min_delta_for_long)                                                                    
            clk = BSCallStrikeFromDelta(stock_price, 
                                               trade_date, 
                                               exp_date, 
                                               sigma=sigma, 
                                               delta=self.entry_crit.min_delta_for_long)                                                                             
            plk = plk - (plk%5) 
            clk = clk + (5-clk%5)                 
            csk = clk + spread               
            psk = plk - spread            
        else:
            logger.error('Unknown strategy %s' % strategy)
            return [np.nan, np.nan, np.nan, np.nan]
                           
        self.np.P1LK = plk
        self.np.P1SK = psk
        self.np.P2LK = clk
        self.np.P2SK = csk

        #logger.info('P1LK %.2f P1SK %.2f P2LK %.2f P2SK %.2f' % (plk, psk, clk, csk))
        
        return [psk, plk, csk, clk]
        
    
    def set_open_price(self, call_opt, put_opt):
        
        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL        
        spread = self.np.SPREAD
        psk = self.np.P1SK
        plk = self.np.P1LK
        csk = self.np.P2SK
        clk = self.np.P2LK
        entry_crit = self.entry_crit
        
        cso = call_opt.loc[call_opt['strike']==csk]
        clo = call_opt.loc[call_opt['strike']==clk]
        pso = put_opt.loc[put_opt['strike']==psk]
        plo = put_opt.loc[put_opt['strike']==plk]
        
        if strategy ==  st.CREDIT_IRON_CONDOR:
            op = pso             
        elif strategy ==  st.DEBIT_IRON_CONDOR:            
            op = plo
        else:
            logger.error('Unknown strategy %s' % strategy)
            return [np.nan, np.nan, np.nan, np.nan]        

        #logger.debug('%s spread %.2f psk %.2f plk %.2f  csk %.2f clk %.2f stock %.2f' % 
        #          (strategy, spread, psk, plk, csk, clk, stock_price))
                                          
        if len(cso) == 0 or len(clo) == 0 or len(pso) == 0 or len(plo) == 0:                    
            logger.debug('Cannot quote option pso %d plo %d cso %d clo %d' %
                     (len(pso), len(plo), len(cso), len(clo)))         
            return [np.nan, np.nan, np.nan, np.nan]  

        if float(pso.volume) < entry_crit.min_opt_vol or \
            float(plo.volume) < entry_crit.min_opt_vol or \
            float(cso.volume) < entry_crit.min_opt_vol or \
            float(cso.volume) < entry_crit.min_opt_vol:                                                                  
            logger.debug('Volumn less than crit.min_return min_opt_vol %d pso %.0f plo %.0f cso %.0f clo %.0f ' %
                     (entry_crit.min_opt_vo, float(pso.volume), float(plo.volume),float(cso.volume), float(clo.volume)))                
            
            return [np.nan, np.nan, np.nan, np.nan]  
            
        if math.isnan(pso.bid) or float(pso.bid) == 0 or math.isnan(pso.ask) or float(pso.ask) == 0:              
            ps_price = float(pso.lastPrice)
        else:    
            ps_price = (float(pso.bid)+float(pso.ask))/2
      
        if math.isnan(plo.bid) or float(plo.bid) == 0 or math.isnan(plo.ask) or float(plo.ask) == 0:                         
            pl_price = float(plo.lastPrice)
        else:    
            pl_price = (float(plo.bid)+float(plo.ask))/2
                 
        if math.isnan(cso.bid) or float(cso.bid) == 0 or math.isnan(cso.ask) or float(cso.ask) == 0:                                                  
            cs_price = float(cso.lastPrice)
        else:    
            cs_price = (float(cso.bid)+float(cso.ask))/2
      
        if math.isnan(clo.bid) or float(clo.bid) == 0 or math.isnan(clo.ask) or float(clo.ask) == 0 :                                
            cl_price = float(clo.lastPrice)
        else:    
            cl_price = (float(clo.bid)+float(clo.ask))/2
            
        open_price = abs(cl_price-cs_price) + abs(pl_price-ps_price)
                        
        self.np.OPEN_PRICE = open_price
        self.np.INIT_impliedVolatility = float(op.impliedVolatility)
        self.np.INIT_volume = float(op.volume)       
        self.np.INIT_openInterest = float(op.openInterest)       
        if strategy ==  st.CREDIT_IRON_CONDOR:
            self.np.MARGIN = spread           
        else:           
            op = plo        
        
        return ps_price, pl_price, cs_price, cl_price    
    
    def set_delta(self, ps_price, pl_price, cs_price, cl_price ):

        strategy = self.np.STRATEGY
        stock_price = self.np.TRADE_STOCK_PRICE
        exp_date = self.np.EXP_DATE
        trade_date = self.np.TRADE_DATE
        symbol = self.np.SYMBOL
        open_price = self.np.OPEN_PRICE
        psk = self.np.P1SK
        plk = self.np.P1LK
        csk = self.np.P2SK
        clk = self.np.P2LK
        entry_crit = self.entry_crit
        
        days_to_expire = (exp_date-trade_date.tz_localize(None)).days             

        if strategy ==  st.CREDIT_IRON_CONDOR:
    
            if math.isnan(cs_price):
                logger.debug('nan cs_price')    
                return np.nan    
            
            c = mibian.BS([stock_price, csk, 0.05, days_to_expire], callPrice=cs_price)
            c = mibian.BS([stock_price, csk, 0.05, days_to_expire], volatility = c.impliedVolatility)
            sd = c.callDelta                    
                
            if math.isnan(ps_price):
                logger.debug('nan ps_price')                   
                return np.nan  
                
            p = mibian.BS([stock_price, psk, 0.05, days_to_expire], putPrice= ps_price)
            p = mibian.BS([stock_price, psk, 0.05, days_to_expire], volatility= p.impliedVolatility)
            psd = p.putDelta   

            logger.debug('csd %.2f psd %.2f max_delta_for_short %.2f' % (sd, psd, entry_crit.max_delta_for_short))
            
            if sd > entry_crit.max_delta_for_short:                   
                logger.debug('Call delta %.2f greater than crit.max_delta_for_short %.2f' % (sd, entry_crit.max_delta_for_short))                                           
                return np.nan                                  
            
            if psd > entry_crit.max_delta_for_short:                   
                logger.debug('Put delta %.2f greater than crit.max_delta_for_short %.2f' % (psd, entry_crit.max_delta_for_short))                                           
                return np.nan                                  
            
        elif strategy ==  st.DEBIT_IRON_CONDOR:            
        
            if math.isnan(cl_price):
                 return np.nan
                
            c = mibian.BS([stock_price, clk, 0.05, days_to_expire], callPrice=cl_price)
            c = mibian.BS([stock_price, clk, 0.05, days_to_expire], volatility = c.impliedVolatility)
            sd = c.callDelta                    
                         
            if math.isnan(pl_price):
                 return np.nan  
            p = mibian.BS([stock_price, plk, 0.05, days_to_expire], putPrice= pl_price)
            p = mibian.BS([stock_price, plk, 0.05, days_to_expire], volatility= p.impliedVolatility)
            psd = p.putDelta         
            
            logger.debug('csd %.2f psd %.2f min_delta_for_long %.2f' % (sd, psd, entry_crit.min_delta_for_long))

            if abs(sd) < entry_crit.min_delta_for_long:                   
                logger.debug('Call delta %.2f less than crit.min_delta_for_long %.2f' % (sd, entry_crit.max_delta_for_short))                                           
                return np.nan  
            
            if abs(psd) > entry_crit.min_delta_for_long:                   
                logger.debug('Put delta %.2f less than crit.min_delta_for_long %.2f' % (psd, entry_crit.max_delta_for_short))                                           
                return np.nan         
        else:
            logger.error('Unknown strategy %s' % strategy)
            return [np.nan, np.nan, np.nan, np.nan]
                                        
        self.np.INIT_DELTA = psd

        return psd   


    def set_max_profit(self):
        
        strategy = self.np.STRATEGY
        open_price = self.np.OPEN_PRICE        
        spread = self.np.SPREAD
        psk = self.np.P1SK
        plk = self.np.P1LK
        csk = self.np.P2SK
        clk = self.np.P2LK
        predList = self.predList
        entry_crit = self.entry_crit
        
        if strategy ==  st.CREDIT_IRON_CONDOR:
            max_loss = spread-open_price                
            max_profit = open_price          
            breakeven_l = psk+max_profit
            breakeven_h = csk-max_profit 
            win_prob = calc_prob_between(predList, breakeven_l, breakeven_h)                  
        elif strategy ==  st.DEBIT_IRON_CONDOR:            
            max_loss = open_price                
            max_profit = spread-open_price     
            breakeven_l = plk+max_loss
            breakeven_h = clk-max_loss                        
            win_prob = 100-calc_prob_between(predList, breakeven_l, breakeven_h)             
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
            logger.debug('open price %.2f, break even low %.2f break even h %.2f win_prob %.2f less then crit.min_chance_of_win %.2f' % (open_price, breakeven_l, breakeven_h, win_prob, entry_crit.min_chance_of_win))
            return np.nan    
                        
        if win_prob < entry_crit.min_chance_of_win:                    
            logger.debug('open price %.2f win_prob %.2f less than crit.min_chance_of_win %.2f' %
                     (open_price, win_prob, entry_crit.min_chance_of_win))                    
            return np.nan                                            
        
        self.np.PNL = pnl
        self.np.MAX_PROFIT = max_profit
        self.np.MAX_LOSS = max_loss
        self.np.WIN_PROB = win_prob
        self.np.BREAKEVEN_L = breakeven_l
        self.np.BREAKEVEN_H = breakeven_h        

        return max_profit