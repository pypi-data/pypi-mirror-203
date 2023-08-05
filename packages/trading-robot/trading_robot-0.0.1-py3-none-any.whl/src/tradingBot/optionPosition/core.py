

import pandas as pd
import pandas_ta as ta
import pytz
import pymannkendall as mk
import math
import numpy as np


from tradingBot.settings.tradeConfig import entryCrit
from tradingBot.settings.tradeConfig import runtimeConfig
from tradingBot.utils.dataGetter import get_price_history
from tradingBot.utils.dataGetter import get_option_chain
from tradingBot.utils.dataGetter import get_option_exp_date

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('core')

class core(object):
    def __init__(self, symbol, entry_crit=entryCrit(), runtime_config=runtimeConfig()):  
        columns = ['SYMBOL','STRATEGY',\
                   'P1SK','P1SP', 'P1ST', 'P1LK', 'P1LP', 'P1LT',\
                   'P2SK', 'P2SP', 'P2ST',  'P2LK', 'P2LP', 'P2LT',\
                   'SPREAD', 'EXP_DATE', 'OPEN_PRICE','LAS_PRICE', 'EXP_PRICE',\
                   'GAIN', 'MAX_PROFIT', 'MAX_LOSS', 'MARGIN', 'PNL', 'WIN_PROB',\
                   'BREAKEVEN_L', 'BREAKEVEN_H', 'TRADE_DATE', 'LAST_QUOTE_DATE', 'TRADE_STOCK_PRICE',\
                   'LAST_STOCK_PRICE', 'EXP_STOCK_PRICE', 'INIT_TREND', 'LAST_TREND', 'INIT_SLOPE', 'LAST_SLOPE',\
                   'INIT_DELTA', 'LAST_DELTA', 'INIT_impliedVolatility', 'LAST_impliedVolatility',\
                   'INIT_volume', 'LAST_volume', 'INIT_openInterest', 'LAST_openInterest']    

        self.symbol = symbol
        
        self.entry_crit = entry_crit
        
        self.runtime_config = runtime_config
        
        self.df = pd.DataFrame(columns=columns)        
    
        self._init_data()
     
        
    def _init_data(self):

        BBStrategy = ta.Strategy(
            name="Momo and Volatility",
            description="BBANDS",
            ta=[
                {"kind": "bbands", "length": 20},      
            ]
        )     
        
        data = get_price_history(self.symbol, period='2mo')
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

        self.data = data        
        self.trend= mk.original_test(gfg_data)
        
        self.option_chain = get_option_chain(self.symbol)                
        self.stock_price = data['Close'][-1]
        self.trade_date = data.index[-1]
        self.sigma = data['rolling_sigma'][-1]           

    def _get_exp_date_list(self, max_days_to_expire):
        
        exp_date_list = []
        exp_tbl = get_option_exp_date(self.symbol)        
        
        for exp_date in exp_tbl:    
            exp_date = pd.Timestamp(exp_date)
            days_to_expire = (exp_date.tz_localize(tz=pytz.UTC)-self.trade_date.tz_convert(tz=pytz.UTC)).days 

            if days_to_expire <= 0:
                continue
                
            if days_to_expire > max_days_to_expire:
                break
                            
            exp_date_list.append(exp_date)
                
        return exp_date_list 