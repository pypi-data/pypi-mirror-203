import os
import xlwings as xw
import pandas as pd
import pandas_ta as ta
from yahoo_fin import stock_info as si

from datetime import time, date, datetime, timedelta
from pytz import timezone

import pymannkendall as mk
import math
import numpy as np
import mibian

from tradingBot.excel import fundamentalSheet as fs
from tradingBot.consts import RGB
from tradingBot.consts import asset as at
from tradingBot.utils.dataGetter import get_price_history
from tradingBot.utils.dataGetter import get_next_earning_date
from tradingBot.utils.dataGetter import get_support_resistence_levels
from tradingBot.utils.dataGetter import get_last_dividend
from tradingBot.utils.dataGetter import get_option_exp_date
from tradingBot.utils.dataGetter import get_option_chain

from tradingBot.backtest.stock.bollingerBands import BB_strategy, plot_BB
from tradingBot.backtest.stock.macd import MACD_strategy, plot_MACD
from tradingBot.backtest.stock.mfi import MFI_strategy, plot_MFI
from tradingBot.backtest.stock.rsi import RSI_strategy, plot_RSI

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('watchListBook')

import warnings
warnings.filterwarnings( "ignore", module = "matplotlib\..*" )

class watchListBook():
    
    def __init__(self, acct_file_path):
        self.file_path = acct_file_path
        self.wb = xw.Book(self.file_path)
        self.workingDir = os.getcwd()  

    def get_all_watch_list(self):
        df = []
        for sh in self.wb.sheets:            
            sheet = fs.fundamentalSheet(sh)
            df.append(sheet.to_df())        
    
        return pd.concat(df)
    
    def get_watch_list(self, watch_list_name, Filter=[]):
        sheet = fs.fundamentalSheet(self.wb.sheets[watch_list_name])
        df = sheet.to_df()        
        if len(Filter) > 0:
            df = df.loc[df[sheet.SYMBOL_t].isin(Filter)]
            return df
        
        return df    
    
    def refresh_all_watch_list(self, update_TD=False):
        for watch_list in self.wb.sheets:
            self.refresh_one_watch_list(watch_list.name, Filter=[], update_TD=update_TD)
            
    def refresh_one_watch_list(self, watch_list_name, Filter=[], update_TD=False):   
        logger.info('refresh watch list %s' % watch_list_name)
        sheet = fs.fundamentalSheet(self.wb.sheets[watch_list_name])         
        o_list_df = sheet.to_df()
        if len(Filter) > 0:
            list_df = o_list_df.loc[o_list_df[sheet.SYMBOL_t].isin(Filter)]
        else:
            list_df = o_list_df

        #for row in list_df.iterrows():
        for rid in list_df.index: 
            row = o_list_df.iloc[rid]
            uid = rid+2           
            self.refresh_asset_info(sheet, row, uid, update_TD)
    
    def refresh_asset_info(self, sheet, row, uid, update_TD):
        
        CustomStrategy = ta.Strategy(
            name="Momo and Volatility",
            description="BBANDS, RSI, MACD, MFI, TREND",
            ta=[
                {"kind": "bbands", "length": 20},      
                {"kind": "rsi"},
                {"kind": "macd", "fast": 12, "slow": 26},
                {"kind": "mfi", "period": 14}     
            ]
        )              
            
        symbol = row['Symbol']

        data = get_price_history(symbol)
        data.ta.cores = 2
        data.ta.strategy(CustomStrategy)
        data.dropna(subset=["BBL_20_2.0"])
        
        logger.info('refresh asset %s' % symbol)
        
        sheet.update_cell(sheet.SYMBOL, uid, value=symbol, font_bold=True)

        self.refresh_asset_basic_info(symbol, data, sheet, uid)        

        sheet.update_cell(sheet.QUOTE_TIME, uid, value=datetime.now(timezone(at.TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S %Z") , font_bold=False)

        if update_TD:
            self.refresh_BB(symbol, data, sheet, uid)
            self.refresh_RSI(symbol, data, sheet, uid)        
            self.refresh_MFI(symbol, data, sheet, uid)        
            self.refresh_MACD(symbol, data, sheet, uid)
        
    def refresh_asset_basic_info(self, symbol, data, sheet, uid, window_size=7):        
        
        #sheet = WatchListBook.load_fundamentalSheet(MonitorLists[0])
        
        q = si.get_quote_data(symbol)  

        last_price = float(q['regularMarketPrice']) 
        day_high =float(q['regularMarketDayHigh']) 
        day_low = float(q['regularMarketDayLow']) 
        if day_high-day_low > 0:
            day_range_pos = ((last_price - day_low)/(day_high-day_low)) * 100
        else:
            day_range_pos = np.nan

        fifty_two_weeks_low = float(q['fiftyTwoWeekLow'])
        fifty_two_weeks_high = float(q['fiftyTwoWeekHigh'])
        fifty_two_weeks_range_pos = ((last_price - fifty_two_weeks_low)/(fifty_two_weeks_high-fifty_two_weeks_low))*100
        volume =float(q['regularMarketVolume'])
        avg_volume_3m = float(q['averageDailyVolume3Month'])
        if avg_volume_3m > 0:
            volume_range_pos = (volume/avg_volume_3m)*100  
        else:
            volume_range_pos = np.nan

        # some symbol not stock so no forward PE            
        if 'forwardPE' in q:
            sheet.update_cell(sheet.FORWARD_PE, uid, value = "{:.2f}".format(q['forwardPE']))  
        else:
            sheet.update_cell(sheet.FORWARD_PE, uid, value = np.nan)

        report_date = get_next_earning_date(symbol)
        if report_date == None:
            sheet.update_cell(sheet.EARNING, uid, value='')
        else:
            days_to_report = report_date-pd.Timestamp.now(report_date.tz)
            if timedelta(days = 0) <= days_to_report<= timedelta(days = 5):
                font_color = RGB.RED
            else:
                font_color = RGB.BLACK
                
            sheet.update_cell(sheet.EARNING, uid, value = report_date.strftime('%m-%d-%Y'), font_color=font_color)                                    

        sheet.update_cell(sheet.LAST_PRICE, uid, value = "{:.2f}".format(q['regularMarketPrice']))            
        sheet.update_cell(sheet.DAY_RANGE_POS, uid, value = "{:.2f}".format(day_range_pos))           
        sheet.update_cell(sheet.FIFTY_WEEKS_RANGE_POS, uid, value = "{:.2f}".format(fifty_two_weeks_range_pos))           
        sheet.update_cell(sheet.VOLUME_RANGE_POS, uid, value = "{:.2f}".format(volume_range_pos))                      
        support, resistence = get_support_resistence_levels(symbol, data)
        if support != None:
            if last_price < support:
                font_color = RGB.RED
            else:
                font_color = RGB.BLACK

            sheet.update_cell(sheet.SUPPORT, uid, value = "{:.2f}".format(support), font_bold=False, font_color=font_color)  
        else:
            sheet.update_cell(sheet.SUPPORT, uid, value = np.nan, font_color=font_color, font_bold=False)  
            
        if resistence != None:
            if last_price > resistence:             
                font_color = RGB.SEA_GREEN                
                font_bold = True
            else:
                font_color = RGB.BLACK
                font_bold = False

            sheet.update_cell(sheet.RESISTENCE, uid, value = "{:.2f}".format(resistence), font_color=font_color, font_bold=False)    
        else:
            sheet.update_cell(sheet.RESISTENCE, uid, value = np.nan, font_color=font_color, font_bold=False)  
                              
        s = window_size # sample size for Mann-Kendall Trend Test
        gfg_data = [0] * s

        # perform Mann-Kendall Trend Test   
        last_date_index = len(data.index)-1        
        for j in range(s):        
            gfg_data[j] = data['BBM_20_2.0'][last_date_index-s+1+j]    

        x = mk.original_test(gfg_data)
        if x.trend == 'increasing':
            font_color = RGB.SEA_GREEN 
        elif x.trend == 'decreasing':
            font_color = RGB.RED  
        else:
            font_color = RGB.BLUE                

        sheet.update_cell(sheet.TREND, uid, value = x.trend, font_color = font_color) 
        sheet.update_cell(sheet.SLOPE, uid, value = "{:.2f}".format(x.slope))                      
        
        TRADING_DAYS =252
        returns = np.log(data['Close']/data['Close'].shift(1))
        returns.fillna(0, inplace=True)
        volatility = returns.rolling(window=20).std()*np.sqrt(TRADING_DAYS)
        hv = round(volatility[-1],2)
    
        sheet.update_cell(sheet.HV, uid, value = "{:.2f}".format(hv*100)) 
      
        def get_iv_list(symbol, data, count):

            trade_date = data.index[-1]
            stock_price = data['Close'][-1]
            exp_tbl = get_option_exp_date(symbol)               
            option_chain = get_option_chain(symbol)
            strike = stock_price - stock_price % 5.0

            if len(exp_tbl) == 0:
                return [np.nan] * count, [np.nan] * count
            
            iv = []
            delta=[]

            for exp_date in exp_tbl:    
                exp_date = pd.Timestamp(exp_date)    
                days_to_expire = (exp_date-trade_date.tz_localize(None)).days
                if days_to_expire < 1:                    
                    continue

                call_opt = option_chain(exp_date.strftime("%Y-%m-%d")).calls    
                op = call_opt.loc[call_opt['strike']==strike]    

                if op.empty:
                    iv.append(np.nan)
                    delta.append(np.nan)
                else:    
                    if len(op.impliedVolatility) == 0:
                        iv.append(np.nan)
                    else:
                        iv.append(float(op.impliedVolatility))

                    if len(op.lastPrice) == 0:
                        delta.append(np.nan)
                    else:
                        last_price = float(op.lastPrice)
                        if math.isnan(last_price) == False:
                            c = mibian.BS([stock_price, strike, 0.05, days_to_expire], callPrice=last_price)
                            c = mibian.BS([stock_price, strike, 0.05, days_to_expire], volatility = c.impliedVolatility)            
                            delta.append(c.callDelta)
                        else:
                            delta.append(np.nan)
                count -= 1
                if count == 0:
                    return iv, delta

            return iv, delta 
 
        
        iv, delta = get_iv_list(symbol, data, 4)
        
        logger.debug(iv)
    
        if len(iv) > 0:
            if math.isnan(iv[0]) == False and iv[0] / hv > 1.2:
                font_color = RGB.RED
            elif math.isnan(iv[0]) == False and iv[0] / hv < 0.8:
                font_color = RGB.SEA_GREEN
            else:
                font_color = RGB.BLACK
            
            sheet.update_cell(sheet.IV1, uid, font_color=font_color, value = "{:.2f}".format(iv[0]*100))            
            sheet.update_cell(sheet.DELTA1, uid, value = "{:.2f}".format(delta[0]))    

        if len(iv) > 1:            
            if math.isnan(iv[1])== False and iv[1] / hv > 1.2:
                font_color = RGB.RED
            elif math.isnan(iv[1])==False and iv[1] / hv < 0.8:
                font_color = RGB.SEA_GREEN
            else:
                font_color = RGB.BLACK
                
            sheet.update_cell(sheet.IV2, uid, font_color=font_color, value = "{:.2f}".format(iv[1]*100))
            sheet.update_cell(sheet.DELTA2, uid, value = "{:.2f}".format(delta[1]))   

        if len(iv) > 2:              
            if math.isnan(iv[2])==False and iv[2] / hv > 1.2:
                font_color = RGB.RED
            elif math.isnan(iv[2])==False and iv[2] / hv < 0.8:
                font_color = RGB.SEA_GREEN
            else:
                font_color = RGB.BLACK       

            sheet.update_cell(sheet.IV3, uid, font_color=font_color, value = "{:.2f}".format(iv[2]*100))
            sheet.update_cell(sheet.DELTA3, uid, value = "{:.2f}".format(delta[2]))
     
        if len(iv) > 3:
            if math.isnan(iv[3])==False and iv[3] / hv > 1.2:
                font_color = RGB.RED
            elif math.isnan(iv[3])==False and iv[3] / hv < 0.8:
                font_color = RGB.SEA_GREEN
            else:
                font_color = RGB.BLACK
            
            sheet.update_cell(sheet.IV4, uid, font_color=font_color, value = "{:.2f}".format(iv[3]*100))       
            sheet.update_cell(sheet.DELTA4, uid, value = "{:.2f}".format(delta[3]))
            
        if 'averageAnalystRating' in q:    
            rating = float(q['averageAnalystRating'].split(" - ")[0])
            if rating < 2:
                font_color=RGB.SEA_GREEN
            elif rating < 3:
                font_color = RGB.BLACK
            else:
                font_color = RGB.RED               
                
            sheet.update_cell(sheet.RATING, uid, font_color=font_color, value = "{:.1f}".format(rating))
       
    def refresh_BB(self, symbol, data, sheet, uid):
                
        bb_pos = data['BBP_20_2.0'][-1]        
        last_action, last_action_price, recent, total_profit = BB_strategy(data)  

        if last_action != '' and recent:
            BB_display = last_action + " {:.2f}".format(last_action_price)            
        else:
            BB_display =  "{:.2f}".format(bb_pos)        

        address = self.workingDir + '\\' + symbol + '_BB.png'

        if recent and last_action == 'Sell':
            font_color = RGB.RED
            font_bold = False
        elif recent and last_action == 'Buy':
            font_color = RGB.SEA_GREEN  
            font_bold = True 
        else:
            font_color = RGB.BLACK
            font_bold = False  

        sheet.update_cell(sheet.BB_POS, 
                     uid, 
                     font_color=font_color, 
                     font_bold=font_bold, 
                     value = BB_display,
                     link_address = address) 

        plot_BB(symbol, data)
        
    def refresh_RSI(self, symbol, data, sheet, uid):
        
        #RSI
        last_action, last_action_price, recent, total_profit = RSI_strategy(data)          
        rsi = data['RSI_14'][-1]
        if recent and last_action != '':
            RSI_display = last_action + " {:.2f}".format(last_action_price)            
        else:
            RSI_display = "{:.2f}".format(rsi)  

        address = self.workingDir + '\\' + symbol + '_RSI.png'      

        if recent and last_action == 'Sell':
            font_color = RGB.RED
            font_bold = False
        elif recent and last_action == 'Buy':
            font_color = RGB.SEA_GREEN  
            font_bold = True 
        else:
            font_color = RGB.BLACK
            font_bold = False                 

        try:
            sheet.update_cell(sheet.RSI, 
                     uid, 
                     value = RSI_display,                          
                     font_color=font_color, 
                     font_bold=font_bold, 
                     link_address = address) 

        except Exception as e:            
            print(str(e))
            
        plot_RSI(symbol, data)
        
    def refresh_MFI(self, symbol, data, sheet, uid):         

        last_action, last_action_price, recent, total_profit = MFI_strategy(data)  
        mfi = data['MFI_14'][-1]
        address = self.workingDir + '\\' + symbol + '_MFI.png'
        if recent and last_action != '':
            MFI_display = last_action + " {:.2f}".format(last_action_price)            
        else:
            MFI_display = "{:.2f}".format(mfi)     

        if recent and last_action == 'Sell':
            font_color = RGB.RED
            font_bold = False
        elif recent and last_action == 'Buy':
            font_color = RGB.SEA_GREEN  
            font_bold = True 
        else:
            font_color = RGB.BLACK
            font_bold = False  

        sheet.update_cell(sheet.MFI, 
                     uid, 
                     value = MFI_display,                          
                     font_color=font_color, 
                     font_bold=font_bold, 
                     link_address = address) 

        plot_MFI(symbol, data)               
        
    def refresh_MACD(self, symbol, data, sheet, uid):        
        # MACD
            
        last_action, last_action_price, recent, total_profit = MACD_strategy(data)  
        macd = data['MACD_12_26_9'][-1]
        address = self.workingDir + '\\' + symbol + '_MACD.png'
        if recent and last_action != '':
            MACD_display = last_action + " {:.2f}".format(last_action_price)            
        else:
            MACD_display = "{:.2f}".format(macd)            

        if recent and last_action == 'Sell':
            font_color = RGB.RED
            font_bold = False
        elif recent and last_action == 'Buy':
            font_color = RGB.SEA_GREEN  
            font_bold = True 
        else:
            font_color = RGB.BLACK
            font_bold = False     

        sheet.update_cell(sheet.MACD, 
                     uid, 
                     value = MACD_display,                          
                     font_color=font_color, 
                     font_bold=font_bold, 
                     link_address = address)                 

        plot_MACD(symbol, data)         
        
    def plot_TA(self, Filter=[], period="1y", interval="1d", start=None, end=None):
        sheet = self.sheet
        df = sheet.range('A1').options(pd.DataFrame, header=1,index=False, expand='table').value 

        if len(Filter) > 0:
            df = df.loc[df['Symbol'].isin(Filter)]
          
        companies = df['Symbol'].tolist()


        CustomStrategy = ta.Strategy(
            name="Momo and Volatility",
            description="BBANDS, RSI, MACD, MFI, TREND",
            ta=[
                {"kind": "bbands", "length": 20},      
                {"kind": "rsi"},
                {"kind": "macd", "fast": 12, "slow": 26},
                {"kind": "mfi", "period": 14}     
            ]
        )  
            
        logger.info(companies)
        
        for symbol in companies:

            try:
                data = get_price_history(symbol, period, interval, start, end)
                data.ta.cores = 2
                data.ta.strategy(CustomStrategy)
            
                plot_MFI(symbol, data)

                plot_MACD(symbol, data)

                plot_BB(symbol, data)
                
                plot_RSI(symbol, data)   
                
                
            except:
                print('skip '+symbol)
                
    def plot_Trend(self, Filter=[], period="1y", interval="1d", start=None, end=None):
        sheet = self.sheet
        df = sheet.range('A1').options(pd.DataFrame, header=1, index=False, expand='table').value 

        if len(Filter) > 0:
            df = df.loc[df['Symbol'].isin(Filter)]
          
        companies = df['Symbol'].tolist()

        print(companies)
        
        for symbol in companies:
            data = get_price_history(symbol, period, interval, start, end)
            data.ta.cores = 2
            data.ta.strategy(CustomStrategy)

            plot_Trend(symbol, data)                 
