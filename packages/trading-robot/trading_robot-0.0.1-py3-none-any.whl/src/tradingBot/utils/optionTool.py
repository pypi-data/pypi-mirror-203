
from scipy.stats import norm
import numpy as np

def BSPutStrikeFromDelta(S, trade_date, exp_date, sigma, delta, r=0.03):
    T = time_to_maturity_in_year(trade_date, exp_date)
    N = norm.cdf        
    return S * np.exp(-N(delta * np.exp((r)*T) ) * sigma * np.sqrt(T) + ((sigma**2)/2) * T)

def BSCallStrikeFromDelta(S, trade_date, exp_date, sigma, delta, r=0.03):
    T = time_to_maturity_in_year(trade_date, exp_date)
    N = norm.cdf        
    return S * np.exp(N(delta* np.exp((r)*T) ) * sigma * np.sqrt(T) + ((sigma**2)/2) * T)

    
#https://www.codearmo.com/python-tutorial/options-trading-black-scholes-model

#S = 100 #stock price S_{0}
#K = 110 # strike
#T = 1/2 # time to maturity in year
#r = 0.05 # risk free risk in annual %
#q = 0.02 # annual dividend rate
#sigma = 0.25 # annual volatility in %
#    call_delta =math.exp(-q*t)*norm.cdf(d1)
#   put_delta =math.exp(-q*t)*(norm.cdf(d1)-1)
         
def d1(S, K, T, r, sigma):
    return (np.log(S/K) + (r + sigma**2/2)*T) / sigma*np.sqrt(T)
    
def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma* np.sqrt(T)

def delta_call(S, K, T, sigma=0.25, r=0.05):
    N = norm.cdf
    return N(d1(S, K, T, r, sigma))

   
def delta_fdm_call(S, K, T, r, sigma, ds = 1e-5, method='central'):
    method = method.lower() 
    if method =='central':
        return (BS_CALL(S+ds, K, T, r, sigma) -BS_CALL(S-ds, K, T, r, sigma))/\
                        (2*ds)
    elif method == 'forward':
        return (BS_CALL(S+ds, K, T, r, sigma) - BS_CALL(S, K, T, r, sigma))/ds
    elif method == 'backward':
        return (BS_CALL(S, K, T, r, sigma) - BS_CALL(S-ds, K, T, r, sigma))/ds

def delta_put(S, K, T, sigma=0.25, r=0.05):
    N = norm.cdf        
    return - N(-d1(S, K, T, r, sigma))

def delta_fdm_put(S, K, T, r, sigma, ds = 1e-5, method='central'):
    method = method.lower() 
    if method =='central':
        return (BS_PUT(S+ds, K, T, r, sigma) -BS_PUT(S-ds, K, T, r, sigma))/\
                        (2*ds)
    elif method == 'forward':
        return (BS_PUT(S+ds, K, T, r, sigma) - BS_PUT(S, K, T, r, sigma))/ds
    elif method == 'backward':
        return (BS_PUT(S, K, T, r, sigma) - BS_PUT(S-ds, K, T, r, sigma))/ds

def BS_CALL(S, K, T, sigma, q=0, r=0.03):
#    try:
    N = norm.cdf    
    d1 = (np.log(S/K) + (r - q + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return S*np.exp(-q*T) * N(d1) - K * np.exp(-r*T)* N(d2)
#    except Exception as e:
#        print('BA_CALL'+str(e))            
#        print('S %.2f K %.2f sigma %.2f')            

def BS_PUT(S, K, T, sigma, q=0, r=0.03):
#    try:
        #print(S)
        #print(K)
        #print(T)
        #print(sigma)
    N = norm.cdf        
    d1 = (np.log(S/K) + (r - q + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*np.exp(-q*T)*N(-d1)
#    except Exception as e:
#        print('BA_PUT'+str(e))            
#        print('S %.2f K %.2f sigma %.2f')    

#T = 1/2 # time to maturity in year
def time_to_maturity_in_year(start_date, exp_date):
    return (exp_date.tz_localize(None)-start_date.tz_localize(None)).days/365
                 
class Oleg(object):
    def __init__(self, otype, strike, exp_date):
        self.Type = otype
        self.Strike = strike             
        self.Exp_Date = exp_date
        self.Contract = None       
        self.Status = None
        self.Open_Price = None
        self.Profit_Per_Contract = None
        self.Open_Date = None
        self.Close_Date = None
        self.Long = None           
        self.Margin_Required_Per_Contract = 0            

    @property
    def params(self):
        return {'Type': self.Type, 
                'Long': self.Long, 
                'Strike': self.Strike, 
                'Exp_Date':self.Exp_Date,
                'Contract': self.Contract,
                'Status':self.Status,
                'Open_Price':self.Open_Price,
                'Profit_Per_Contract':self.Profit_Per_Contract,
                'Open_Date': self.Open_Date,
                'Close_Date': self.Close_Date,
                'Open_Price': self.Open_Price,
                'Close_Price': self.Open_Price,                    
                'Status':self.Status}
    
    def already_expired(self, date):
        if time_to_maturity_in_year(date, self.Exp_Date) > 0:
            return False
        else:
            return True

    def buy_to_open(self, stock_price, date, max_fund, sigma, q=0, r=0.03):
        self.Long = True
        self.__open(stock_price, date, max_fund, sigma, q, r)
            
    def sell_to_open(self, stock_price, date, max_fund, sigma, q=0, r=0.03):
        self.Long = False
        self.__open(stock_price, date, max_fund, sigma, q, r)      
    
    def __open(self, stock_price, date, max_fund, sigma, q=0, r=0.03):
        self.Status = 'Opened'            
        self.Open_Date = date
        self.Open_Price = stock_price            
        T = time_to_maturity_in_year(date, self.Exp_Date)
        if self.Type == 'Call':
            self.Open_Price = BS_CALL(stock_price, self.Strike, T, sigma, q, r)
        elif self.Type == 'Put':
            self.Open_Price = BS_PUT(stock_price, self.Strike, T, sigma, q, r)                             
        else:
            print('Unknown option type ' + self.Type)
            # throw exception
        if self.Long == False: # short position
            self.Contract = 1
            self.Margin_Required_Per_Contract = stock_price - self.Open_Price
            return
        
        if max_fund > 0 and self.Open_Price > max_fund:
            self.Contract = 0
        else:
            self.Contract = 1       
                                    
    def sell_to_close(self, stock_price, date, sigma=0, q=0, r=0.03):           
        if self.Long == False:
            print('cannot sell to close short option')
            return
        self.__close(stock_price, date, sigma, q, r)
        
    def buy_to_close(self, stock_price, date, sigma=0, q=0, r=0.03):            
        if self.Long:
            print('cannot buy to close long option')
            return
        self.__close(stock_price, date, sigma, q, r)  
                        
    def __close(self, stock_price, date, sigma=0, q=0, r=0.03):
        if self.Status != 'Opened':
            print('Cannot close non-opened option position')
            return
        
        self.Status = 'Closed'
        self.Close_Date =  date
        
        T = time_to_maturity_in_year(date, self.Exp_Date)                
        if self.Type == 'Call':      
            if T > 0: # not yet expired  
                close_price = BS_CALL(stock_price, self.Strike, T, sigma, q, r)                    
            elif T == 0: #expired
                if stock_price > self.Strike:
                    close_price = stock_price - self.Strike
                else:
                    close_price = 0                         
        elif self.Type == 'Put':
            if T > 0:
                close_price = BS_PUT(stock_price, self.Strike, T, sigma, q, r)
            elif T == 0:
                if stock_price < self.Strike:
                    close_price = self.Strike - stock_price
                else:
                    close_price = 0                     
        else:
            print('Incorrect option type '+self.Type)
            #Throw exception

        if self.Long:
            self.Profit_Per_Contract = close_price - self.Open_Price
        else:
            self.Profit_Per_Contract = self.Open_Price - close_price      
        
        self.Close_Price = stock_price
        
    def current_price_per_contract(self, stock_price, date, sigma, q=0, r=0.03):
        T = time_to_maturity_in_year(date, self.Exp_Date)
        if self.Type == 'Call':
            return BS_CALL(stock_price, self.Strike, T, sigma, q, r)
        elif self.Type == 'Put':
            return BS_PUT(stock_price, self.Strike, T, sigma, q, r)
        else:
            print('Unknown option type ' + self.Type)
                               
class Call(Oleg):
    def __init__(self, strike, exp_date):
        super().__init__('Call', strike, exp_date)      
                        
class Put(Oleg):
    def __init__(self, strike, exp_date):
        super().__init__('Put', strike, exp_date)     
            
class Spread(object):        
    def __init__(self, otype, exp_date, short_strike, long_strike):
        self.Exp_Date = exp_date
        self.Short_Strike = short_strike
        self.Long_Strike = long_strike
        self.Spread = abs(short_strike-long_strike)
        self.Type = otype
        self.Contract = 0
        self.Status = None
        self.Margin_Per_Contract = 0
        self.Open_Price = 0
        self.Profit_Per_Contract = 0
        self.Short_Leg = None
        self.Long_leg = None
        self.Credit_Spread = False
        if self.Type == 'Call' and long_strike > short_strike:
            self.Credit_Spread = True
        elif self.Type == 'Put' and short_strike > long_strike:
            self.Credit_Spread = True            
    
    @property
    def params(self):
        return {
                'Spread': abs(self.Long_Strike - self.Short_Strike),
                'Open_Date': self.Short_Leg.Open_Date,
                'Open_Price': self.Short_Leg.Open_Price,
                'Close_Date': self.Short_Leg.Open_Date,
                'Close_Price': self.Short_Leg.Open_Price                
                }
            
        
    def Open(self, stock_price, open_date, max_margin, sigma, q=0, r=0.03):         
        if self.Type == 'Call':                
            short_leg = Call(self.Short_Strike, self.Exp_Date)
            long_leg = Call(self.Long_Strike, self.Exp_Date)
        elif self.Type == 'Put':                
            short_leg = Put(self.Short_Strike, self.Exp_Date)
            long_leg = Put(self.Long_Strike, self.Exp_Date)
        else:
            print("Invalid option type: "+ self.Type)
            return
        
        short_leg.sell_to_open(stock_price, open_date, -1, sigma, q, r) 
        
        long_leg.buy_to_open(stock_price, open_date, -1, sigma, q, r) 
        
        #if short_leg.Contract + long_leg.Contract == 2:
        
        if self.Credit_Spread == True:         
            self.Open_Price = short_leg.Open_Price - long_leg.Open_Price                 
            self.Margin_Per_Contract = self.Spread - self.Open_Price
            self.Contract = max_margin // (self.Margin_Per_Contract * 100)
            #print('max margin %.2f m per contract %.2f contract %d' %(max_margin, self.Margin_Per_Contract, self.Contract))
        else:
            self.Open_Price = long_leg.Open_Price - short_leg.Open_Price                                
            if self.Open_Price == 0:
                print('Open_Price == 0 sk %.2f lk %.2f s price %.2f l price %.2f' % 
                        (self.Short_Strike, self.Long_Strike, short_leg.Open_Price, long_leg.Open_Price))
                self.Contract = 1
            else:
                self.Contract = max_margin // abs(self.Open_Price*100)
                
            self.Margin_Per_Contract = 0
            
        self.Open_Date = open_date
        self.Status = 'Opened'
        self.Short_Leg = short_leg
        self.Long_Leg = long_leg
            
    def Close(self, stock_price, close_date,  sigma, q=0, r=0.03):
        if self.Status != 'Opened':
            print('Cannot close non-opened option position')
            return
        
        self.Short_Leg.buy_to_close(stock_price, close_date, sigma, q, r)

        self.Long_Leg.sell_to_close(stock_price, close_date, sigma, q, r)
        
        self.Profit_Per_Contract = self.Short_Leg.Profit_Per_Contract + self.Long_Leg.Profit_Per_Contract      
        
        self.Status = 'Closed'
        
    def current_price_per_contract(self, stock_price, date, sigma, q=0, r=0.03):
        long_price  = self.Long_Leg.current_price_per_contract(stock_price, date, sigma, q, r)
        short_price = self.Short_Leg.current_price_per_contract(stock_price, date, sigma, q, r)
        if self.Credit_Spread == True:   
            return short_price  - long_price
        else:
            return long_price - short_price 
               