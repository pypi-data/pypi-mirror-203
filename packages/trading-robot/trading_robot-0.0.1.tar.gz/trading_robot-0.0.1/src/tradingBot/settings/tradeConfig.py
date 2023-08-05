

class entryCrit(object):
    def __init__(self):  
        #Opportunity
        self.min_pnl = 0.2
        self.min_chance_of_win = 25
        self.min_delta_for_long = 0.7
        self.max_delta_for_short = 0.3  
        self.max_slope = 0.3        
        self.min_slope = 0.9           
        
        self.min_open_interest = 1
        self.min_opt_vol = 1  
        
        self.min_IV_for_short = 0.6       
        self.max_IV_for_long = 0.4       
        
        self.max_rating = 2

        #Stock
        #self.min_days_earning_away = 5
        
        # covred call parameters
        self.covered_call_contract = 1        

        # Iron Condor parameters    
        self.iron_condor_min_theta = 0.5  
        
        # min stock ranking
        #self.max_ranking = 3 

import numpy as np

class exitCrit(object):
    def __init__(self):
        self.days_before_expire = 2
        self.days_before_earning = 2
        self.stop_gain=80 
        self.stop_loss=90
        
class marketCondition(object):
    def __init__(self):
        self.current_vix = np.nan
        self.VIX_low = 20 
        self.VIX_high = 30
        self.IV_Rank_low = 20
        self.IV_Rang_high = 90            

class riskManager(object):
    def __init__(self):     
        self.stop_loss_percent = 80
        self.stop_gain_percent = 90
        self.close_days_before_earning = 1
        self.close_days_before_expire = 1
        self.open_min_days_to_earning = 4        
        self.open_min_days_to_expire = 4
        self.max_option_positions = 10
        self.max_loss_per_position = 1500

class runtimeConfig(object):
    def __init__(self):     
        self.init_balance = 100000           
        self.nweek = 0 
        self.weekday = 0    
        self.trend_window_size = 7        
        self.max_days_to_expire = 30
        self.spreads = [2.5, 5.0, 7.5, 10.0]

        #self.spread = 5
            
# weekday = 0: Monday
# nweek 0..N : number of weeks to expire
# stop_gain - profit taking percent
# stop_loss - stop loss percent

 