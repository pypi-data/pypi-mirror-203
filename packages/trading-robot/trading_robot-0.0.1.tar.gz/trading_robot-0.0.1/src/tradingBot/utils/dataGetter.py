import pandas as pd
import yfinance as yf
from datetime import time, date, datetime, timedelta
import pytz, holidays
from pytz import timezone
import numpy as np
from tradingBot.consts import asset as at
import logging

logger = logging.getLogger(__name__)

class Cashe:
    LAST_QUOTE_TIME = {}      
    TICKERS = {}
    INFOS = {}
    OPTION_CHAIN = {}
    OPTION_EXP_DATE = {}
    HV20 = {}
    LAST_QUOTE_DATE = {}
    HISTORY = {}      

    @staticmethod
    def was_updated_recently(symbol):  
        #logger.debug("was_updated_recently")                 
        now = datetime.now(timezone(at.TIMEZONE))  
        if symbol not in Cashe.LAST_QUOTE_TIME:
            Cashe.LAST_QUOTE_TIME[symbol] = now    
            return False
        else:         
            if afterHours() == True:
                return now - timedelta(days=1) <= Cashe.LAST_QUOTE_TIME[symbol] <= now                
            else:
                return now - timedelta(minutes=15) <= Cashe.LAST_QUOTE_TIME[symbol] <= now

    @staticmethod
    def was_updated_today(symbol):  
        #logger.debug("was_updated_today")            
        if symbol not in Cashe.LAST_QUOTE_DATE:
            return False
        else:
            now = datetime.now(timezone(at.TIMEZONE))                  
            return now - timedelta(days=1) <= Cashe.LAST_QUOTE_DATE[symbol] <= now                

def get_price_history(symbol, period="1y", interval="1d", start=None, end=None):
    #logger.debug("get_price_history %s", symbol)        
    if period in ['2y', '3y'] or interval != '1d' or end !=None or start != None: # TODO or end more than 1y earlier
        q = get_ticker(symbol)
        return q.history(period=period, interval=interval, start=start, end=end)

    if symbol not in Cashe.HISTORY:    
        #print('Not found ticker', symbol) 
        q = get_ticker(symbol)       
        Cashe.HISTORY[symbol] = q.history(period=period)        
        Cashe.LAST_QUOTE_TIME[symbol] = datetime.now(timezone(at.TIMEZONE))
    else:
        if Cashe.was_updated_today(symbol) == False:
            q = get_ticker(symbol)       
            Cashe.HISTORY[symbol] = q.history(period=period)        
            Cashe.LAST_QUOTE_TIME[symbol] = datetime.now(timezone(at.TIMEZONE))
        else:
            if Cashe.was_updated_recently(symbol) == False:                 
                Cashe.HISTORY[symbol]['Close'][-1] = Utils.get_last_price(symbol)

    return Cashe.HISTORY[symbol]
            
def get_ticker(symbol):
    #logger.debug("get_ticker %s", symbol)            
    if symbol not in Cashe.TICKERS:    
        #print('Not found ticker', symbol)        
        Cashe.TICKERS[symbol] = yf.Ticker(symbol)          
        Cashe.LAST_QUOTE_TIME[symbol] = datetime.now(timezone(at.TIMEZONE))
    else:
        if Cashe.was_updated_recently(symbol) == False:
            #print('RENEW ticker', symbol)
            Cashe.TICKERS[symbol] = yf.Ticker(symbol)                
            Cashe.LAST_QUOTE_TIME[symbol] = datetime.now(timezone(at.TIMEZONE)) 
        #else:               
            #print('Cached ticker', symbol)
    return Cashe.TICKERS[symbol]
             
def get_last_dividend(symbol):
    stock = get_ticker(symbol)
    ed = stock.get_dividends()
    if len(ed) > 0:
        return ed[-1]
    else:
        return 0.0      

def afterHours(now = None):
    tz = pytz.timezone(at.TIMEZONE)
    us_holidays = holidays.US()        
    if not now:
        now = datetime.now(tz)        
    openTime = time(hour = 9, minute = 30, second = 0)
    closeTime = time(hour = 16, minute = 0, second = 0)
    # If a holiday
    if now.strftime('%Y-%m-%d') in us_holidays:
        return True
    # If before 0930 or after 1600
    if (now.time() < openTime) or (now.time() > closeTime):
        return True
    # If it's a weekend
    if now.date().weekday() > 4:
        return True

    return False       
    
def get_next_earning_date(symbol):
    stock = get_ticker(symbol)
    ed = stock.get_earnings_dates()
    if isinstance(ed, type(None)):
        return None
    
    if ed.empty == False:
        today = pd.Timestamp.now(ed.head(1).index.tz)
        et = ed[ed.index > today]
        if et.empty == False:
            return et.index[-1] #tail(1)
    return None
        
def get_earning_dates(symbol):
    stock = get_ticker(symbol)
    return stock.get_earnings_dates()     

def get_option_chain(symbol):
    #logger.debug("get_option_chain %s", symbol)            
    q = get_ticker(symbol)        
    if symbol not in Cashe.OPTION_CHAIN: 
        try:              
            Cashe.OPTION_CHAIN[symbol] = q.option_chain
        except:
            return None
    else:
        if Cashe.was_updated_recently(symbol) == False:
            Cashe.OPTION_CHAIN[symbol] = q.option_chain 

    return Cashe.OPTION_CHAIN[symbol]

    #https://towardsdatascience.com/detection-of-price-support-and-resistance-levels-in-python-baedc44c34c9
def get_support_resistence_levels(symbol, data=pd.DataFrame()):

    def isSupport(df,i):
        support = df['Low'][i] < df['Low'][i-1]  and df['Low'][i] < df['Low'][i+1] and df['Low'][i+1] < df['Low'][i+2] and df['Low'][i-1] < df['Low'][i-2]
        return support

    def isResistance(df,i):
        resistance = df['High'][i] > df['High'][i-1]  and df['High'][i] > df['High'][i+1] and df['High'][i+1] > df['High'][i+2] and df['High'][i-1] > df['High'][i-2]
        return resistance

    if data.empty:
        df = get_price_history(symbol)
    else:
        df = data

    s =  np.mean(df['High'] - df['Low'])

    def isFarFromLevel(l):
        return np.sum([abs(l-x) < s  for x in levels]) == 0

    SUPPORT = 0
    RESISTANCE = 1
    levels = []
    for i in range(2,df.shape[0]-2):
        if isSupport(df,i):
            l = df['Low'][i]
            if isFarFromLevel(l):
                levels.append((i,l,SUPPORT))
        elif isResistance(df,i):
            l = df['High'][i]
            if isFarFromLevel(l):
                levels.append((i,l,RESISTANCE))        

    l = range( len(levels) - 1, -1, -1)
    support = None
    resistence = None

    for i in l:
        if levels[i][2] == SUPPORT and support == None:
            support = levels[i][1]
        if levels[i][2] == RESISTANCE and resistence == None:
            if support != None and levels[i][1] > support:
                resistence = levels[i][1]

    return support, resistence

def get_option_exp_date(symbol):
    #logger.debug("get_option_exp_date %s", symbol)            
    if symbol not in Cashe.OPTION_EXP_DATE:                
        q = get_ticker(symbol)
        try:
            Cashe.OPTION_EXP_DATE[symbol] = q.options
        except:
            return None
    else:
        if Cashe.was_updated_today(symbol) == False:
            q = get_ticker(symbol)                
            Cashe.OPTION_EXP_DATE[symbol] = q.options            
    return Cashe.OPTION_EXP_DATE[symbol]    





 