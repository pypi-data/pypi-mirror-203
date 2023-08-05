import pandas as pd
import numpy as np
from scipy.stats import norm
from datetime import time, date, datetime, timedelta
from pytz import timezone

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

from tradingBot.consts import asset as at

import logging

logger = logging.getLogger(__name__)

def highest_price_with_prob_low_than(predList, current_price, prob):

    target_price = current_price
    prob = prob/100
    while True:
        over = [i for i in predList if i > target_price]            
        less = [i for i in predList if i <= target_price]
        if len(less)/(len(less)+len(over)) > prob:
            target_price -= 0.5
        else:
            return target_price


def calc_prob_higher_than(predList, target_price):

    over = [i for i in predList if i >= target_price]
    less = [i for i in predList if i < target_price]      
    prob = (len(over)/(len(over)+len(less))) * 100
    #logger.debug("calc_prob_higher_than %d %f", target_price, prob)        
    return round(prob,2)    
               
def calc_prob_lower_than(predList, target_price):
    over = [i for i in predList if i >= target_price]
    less = [i for i in predList if i < target_price]      
    prob = (len(less)/(len(over)+len(less))) * 100    
    #logger.debug("calc_prob_lower_than %d %f", target_price, prob)           
    return round(prob,2)

def calc_prob_between(predList, target_price_1, target_price_2):
    #logger.debug("calc_prob_between %f %f", target_price_1, target_price_2)
    if target_price_1 > target_price_2:           
        target_price_LOW = target_price_2
        target_price_HIGH = target_price_1
    else:
        target_price_LOW = target_price_1
        target_price_HIGH = target_price_2
        
    between = [i for i in predList if i >= target_price_LOW and i <= target_price_HIGH]
    outside = [i for i in predList if i < target_price_LOW or i > target_price_HIGH] 

    prob = (len(between)/(len(between)+len(outside)))*100
        
    return round(prob,2)

def predicted_list(symbol, quote, target_date, iterations=1000):
    data = pd.DataFrame()
    data[symbol] = quote['Close']

    #logger.debug("predicted_list %s", symbol)
    """
        This function calculated the probability of a stock being above a certain threshhold, which can be defined as a value (final stock price) or return rate (percentage change)
        Input: 
        1. symbol: specific ticker to compute probability fo
        2. target_date: some future date
        Output:
        simulated predicted list

    """
    def log_returns(data):
        #logger.debug("log_returns")
        return (np.log(1+data.pct_change()))

    def simple_returns(data):
        #logger.debug("simple_returns")            
        return ((data/data.shift(1))-1)

    def drift_calc(data, return_type='log'):
        #logger.debug("drift_calc")    
        if return_type=='log':
            lr = log_returns(data)
        elif return_type=='simple':
            lr = simple_returns(data)
        u = lr.mean()
        var = lr.var()
        drift = u-(0.5*var)
        try:
            return drift.values
        except:
            return drift

    def daily_returns(data, days, iterations, return_type='log'):
        #logger.debug("daily_returns")  
        ft = drift_calc(data, return_type)
        if return_type == 'log':
            try:
                stv = log_returns(data).std().values
            except:
                stv = log_returns(data).std()
        elif return_type=='simple':
            try:
                stv = simple_returns(data).std().values
            except:
                stv = simple_returns(data).std()    
            #Oftentimes, we find that the distribution of returns is a variation of the normal distribution where it has a fat tail
            # This distribution is called cauchy distribution
        dr = np.exp(ft + stv * norm.ppf(np.random.rand(days, iterations)))
        return dr



    def num_of_trade_days(end_date):
        today = datetime.now(timezone(at.TIMEZONE))
        us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
        d = pd.date_range(start=today,end=end_date.tz_localize(timezone(at.TIMEZONE)), freq=us_bd)
        return len(d)

    trade_days = num_of_trade_days(target_date)

    # Generate daily returns
    returns = daily_returns(data, trade_days, iterations)
    # Create empty matrix
    price_list = np.zeros_like(returns)
    # Put the last actual price in the first row of matrix. 
    try:
        price_list[0] = data.iloc[-1]
    except:
        print(target_date)
        print(returns)
        
    # Calculate the price of each day
    for t in range(1,trade_days):
        price_list[t] = price_list[t-1]*returns[t]

    predicted = pd.DataFrame(price_list)
    predicted = predicted.iloc[-1]
    predList = list(predicted)

    return predList
    
