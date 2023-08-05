import xlwings as xw
import pandas as pd
import pandas_ta as ta
import pymannkendall as mk
import json
import numpy as np


from tradingBot.settings.tradeConfig import entryCrit
from tradingBot.settings.tradeConfig import exitCrit
from tradingBot.settings.tradeConfig import runtimeConfig
from tradingBot.settings.tradeConfig import marketCondition
from tradingBot.settings.tradeConfig import riskManager

from tradingBot.excel import backtestSheet as bt

from tradingBot.utils.dataGetter import get_price_history
from tradingBot.utils.dataGetter import get_last_dividend

from tradingBot.consts import RGB

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('backtestBook')

class backtestBook():
    
    def __init__(self, backtest_file_path):        
        self.backtest_file_path = backtest_file_path
        self.wb = xw.Book(backtest_file_path)   
                        
    def backtest(self, 
                 test_name, 
                 watch_list, 
                 strategy_list=[],                     
                 period="1y",
                 interval="1d", 
                 start=None, 
                 end=None,
                 runtime_config = runtimeConfig(),
                 market_condition = marketCondition(),
                 risk_mgr = riskManager(),
                 entry_crit = entryCrit(),
                 exit_crit = exitCrit()):                        
            
        if len(strategy_list) == 0:
            logger.error('Empty Strategy List')
            return
            
        sheet = bt.backtestSheet(self.wb, sheet_name=test_name, strategy_list=strategy_list)

        BBStrategy = ta.Strategy(
            name="Momo and Volatility",
            description="BBANDS",
            ta=[
                {"kind": "bbands", "length": 20},      
            ]
        )   
                
        uid = 2
        
        for symbol in watch_list:        
            
            logger.info(symbol)
            
            sheet.update_cell(sheet.SYMBOL, uid, value=symbol, font_bold=True)
            
            data = get_price_history(symbol, period, interval, start, end) 
            
            data.ta.cores = 2 
            data.ta.strategy(BBStrategy)
            data.dropna(subset=["BBM_20_2.0"])
            data['change'] = data['Close'].pct_change()
            data['rolling_sigma'] = data['change'].rolling(20).std() * np.sqrt(255)    

            for strategy in strategy_list:
                strategy.init_backtest(data)

            dividend = get_last_dividend(symbol)

            s = strategy_list[0].runtime_config.trend_window_size # sample size for Mann-Kendall Trend Test
            gfg_data = [0] * s 

            start_id = None
            
            for i in range(len(data)):
                # skip inital nan values
                if i <  s or pd.isna(data['BBM_20_2.0'][i-s+1] or pd.isna(data['rolling_sigma'][i])):               
                    continue    

                if start_id == None:
                    start_id = i

                for j in range(s):        
                    gfg_data[j] = data['BBM_20_2.0'][i-s+1+j]   

                x = mk.original_test(gfg_data)

                for strategy in strategy_list:
                    strategy.check_exit(i, dividend)                                                     
                    strategy.check_entry(i, dividend, x)                           
            
            bench = 100 * ((data['Close'][-1] - data['Close'][start_id]) / data['Close'][start_id])

            sheet.update_cell(sheet.BENCH, uid, value='%.2f' % bench)
            for strategy in strategy_list:  
                gain_col = chr(ord(sheet.BENCH)+1+(strategy_list.index(strategy)))
                gain = strategy.get_gain()
                if gain > 0 and gain > bench:
                    sheet.update_cell(gain_col, uid, font_color = RGB.SEA_GREEN, font_bold = True, value='%.2f' % strategy.get_gain())                
                else:    
                    sheet.update_cell(gain_col, uid, value='%.2f' % strategy.get_gain())                
                    
            uid += 1

        sheet.update_cell('A', uid+3, font_bold = True, value='Start Date')           
        sheet.update_cell('B', uid+3, font_bold = True, value='%s' % data.index[start_id].strftime('%Y-%m-%d'))
        sheet.update_cell('D', uid+3, font_bold = True, value='End Date')           
        sheet.update_cell('E', uid+3, font_bold = True, value='%s' % data.index[-1].strftime('%Y-%m-%d'))                                  
        
        sheet.update_cell('A', uid+5, font_bold = True, value='Entry Crit')           
        sheet.update_cell('B', uid+5, font_bold = True, value='%s' % json.dumps(vars(entry_crit)))            
        
        sheet.update_cell('A', uid+7, font_bold = True, value='Exit Crit')           
        sheet.update_cell('B', uid+7, font_bold = True, value='%s' % json.dumps(vars(exit_crit))) 
        
        sheet.update_cell('A', uid+9, font_bold = True, value='Runtime Config')           
        sheet.update_cell('B', uid+9, font_bold = True, value='%s' % json.dumps(vars(runtime_config))) 

        sheet.update_cell('A', uid+11, font_bold = True, value='Market Condition')           
        sheet.update_cell('B', uid+11, font_bold = True, value='%s' % json.dumps(vars(market_condition))) 
        