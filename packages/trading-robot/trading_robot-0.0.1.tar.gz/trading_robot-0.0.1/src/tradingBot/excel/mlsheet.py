from tradingBot.excel import dataSheet
from tradingBot.consts import RGB

class mlSheet(dataSheet.dataSheet):
    SYMBOL = 'A'    
    STRATEGY = 'B'
    OPEN_DATE
    
    P1SK = 'C'
    P1LK = 'D' 
    P2SK = 'E'
    P2LK = 'F'
    SPREAD = 'G'     
    
    OPEN_PRICE = 'H' 
    LAST_PRICE = 'I'       
    EXP_PRICE = 'J'
    PL = 'K'    
    
    MAX_PROFIT = 'L'     
    MAX_LOSS = 'M'
    PNL='N'
    WIN_PROB = 'O'   
    
    EXP_DATE = 'P'    
    EARNING_DATE = 'Q' 
    GAIN = 'R' 
    
    BREAKEVEN_L = 'S'
    BREAKEVEN_H = 'T'

    TRADE_DATE = 'U'   
    LAST_QUOTE_DATE = 'V'
      
    TRADE_STOCK_PRICE = 'W'    
    LAST_STOCK_PRICE = 'X'
    EXP_STOCK_PRICE = 'Y'       
        
    INIT_TREND = 'Z'
    LAST_TREND = 'AA'    
    INIT_SLOPE = 'AB'
    LAST_SLOPE = 'AC'    
    INIT_delta = 'AD'         
    LAST_delta = 'AE'      
    INIT_impliedVolatility = 'AF'
    LAST_impliedVolatility = 'AG'     
    INIT_volume = 'AH'    
    LAST_volume = 'AI'       
    INIT_openInterest = 'AJ' 
    LAST_openInterest  = 'AK'              

    DEBUG = 'AL'    
    
    SYMBOL_t = 'Symbol'
    STRATEGY_t = 'Strategy' 
    
    P1SK_t  = 'p1 short K' 
    P1LK_t  = 'p1 long K'       
    P2SK_t  = 'p2 short K' 
    P2LK_t  = 'p2 long K'    
        
    SPREAD_t = 'Spread' 
        
    OPEN_PRICE_t  = 'Open Price'
    LAST_PRICE_t  = 'Last Price'        
    EXP_PRICE_t = 'Exp Price'
    PL_t = 'Profit/Loss'
    GAIN_t  = 'Gain %'  
    BREAKEVEN_L_t  = 'Breakeven l'
    BREAKEVEN_H_t  = 'Breakeven h'        
            
    MAX_PROFIT_t  = 'Max Profit'  
    MAX_LOSS_t = 'Max Loss' 
    PNL_t = 'PNL'         
    WIN_PROB_t  = 'Win Prob %'         
        
    TRADE_DATE_t  = 'Trade Date'           
    LAST_QUOTE_DATE_t  = 'Last Quote Date'
    EXP_DATE_t  = 'Exp Date'   
    EARNING_DATE_t  = 'Earning Date'        
                  
    TRADE_STOCK_PRICE_t  = 'Trade Stock Price'
    LAST_STOCK_PRICE_t  = 'Last Stock Price'
    EXP_STOCK_PRICE_t  = 'Exp Stock Price'        
    
    INIT_TREND_t  = 'Init Trend'
    INIT_SLOPE_t  = 'Init Slope'
    INIT_delta_t  = 'Init Delta'   
    INIT_impliedVolatility_t  = 'Init IV'  
    INIT_volume_t  = 'Init Volumn'               
    INIT_openInterest_t  = 'Init Open Interest'
        
    LAST_TREND_t  = 'Last Trend'
    LAST_SLOPE_t  = 'Last Slope'        
    LAST_delta_t  = 'Last Delta'     
    LAST_impliedVolatility_t  = 'Last IV'          
    LAST_volume_t = 'Last Volumn'         
    LAST_openInterest_t  = 'Last Open Interest'  

    PL_t = 'Profit or Loss'    
    DEBUG_t = 'Debug'              
    
    def save_crit(self, entry_crit=False, exit_crit=False, market_condition=False, risk_manager=False):
        sheet = self.sheet        
        if entry_crit != False:         
            sheet.range(self.ENTRY_CRIT+'2').value = json.dumps(vars(entry_crit))           
        if exit_crit != False:         
            sheet.range(self.EXIT_CRIT+'2').value = json.dumps(vars(exit_crit))             
        if market_condition != False:  
            sheet.range(self.MARKET_CONFITIONT+'2').value = json.dumps(vars(market_condition))             
        if risk_manager != False:   
            sheet.range(self.RISK_MANAGER+'2').value = json.dumps(vars(risk_manager))               
                              
    def __init__(self, wb, sheet_name, create=True):

        try:
            self.sheet = wb.sheets[sheet_name]     
            if create:
                self.sheet.clear()
        except:
            if create == True:
                self.sheet = wb.sheets.add(sheet_name)
            else:
                print('%s not found' % sheet_name)
                return
            
        super().__init__(self.sheet)     
        self.__init_sheet_header()  
        
    def __init_sheet_header(self):    
        sheet = self.sheet
            
        sheet.range(self.SYMBOL+'1').value = positionSheet.SYMBOL_t
        sheet.range(self.STRATEGY+'1').value = positionSheet.STRATEGY_t  
        sheet.range(self.P1SK+'1').value = positionSheet.P1SK_t 
        sheet.range(self.P1LK+'1').value = positionSheet.P1LK_t       
        sheet.range(self.P2SK+'1').value = positionSheet.P2SK_t 
        sheet.range(self.P2LK+'1').value = positionSheet.P2LK_t    
        
        sheet.range(self.SPREAD+'1').value = positionSheet.SPREAD_t 
        
        sheet.range(self.OPEN_PRICE+'1').value = positionSheet.OPEN_PRICE_t
        sheet.range(self.LAST_PRICE+'1').value = positionSheet.LAST_PRICE_t      
        sheet.range(self.EXP_PRICE+'1').value = positionSheet.EXP_PRICE_t
        sheet.range(self.PL+'1').value = positionSheet.PL_t        
        sheet.range(self.GAIN+'1').value = positionSheet.GAIN_t  
        sheet.range(self.BREAKEVEN_L+'1').value = positionSheet.BREAKEVEN_L_t
        sheet.range(self.BREAKEVEN_H+'1').value = positionSheet.BREAKEVEN_H_t        
            
        sheet.range(self.MAX_PROFIT+'1').value = positionSheet.MAX_PROFIT_t  
        sheet.range(self.MAX_LOSS+'1').value = positionSheet.MAX_LOSS_t 
        sheet.range(self.PNL+'1').value = positionSheet.PNL_t        
        sheet.range(self.WIN_PROB+'1').value = positionSheet.WIN_PROB_t         
        
        sheet.range(self.TRADE_DATE+'1').value = positionSheet.TRADE_DATE_t           
        sheet.range(self.LAST_QUOTE_DATE+'1').value = positionSheet.LAST_QUOTE_DATE_t
        sheet.range(self.EXP_DATE+'1').value = positionSheet.EXP_DATE_t    
        sheet.range(self.EARNING_DATE+'1').value = positionSheet.EARNING_DATE_t    
                  
        sheet.range(self.TRADE_STOCK_PRICE+'1').value = positionSheet.TRADE_STOCK_PRICE_t
        sheet.range(self.LAST_STOCK_PRICE+'1').value = positionSheet.LAST_STOCK_PRICE_t
        sheet.range(self.EXP_STOCK_PRICE+'1').value = positionSheet.EXP_STOCK_PRICE_t        
    
        sheet.range(self.INIT_TREND+'1').value = positionSheet.INIT_TREND_t
        sheet.range(self.INIT_SLOPE+'1').value = positionSheet.INIT_SLOPE_t
        sheet.range(self.INIT_delta+'1').value = positionSheet.INIT_delta_t  
        sheet.range(self.INIT_impliedVolatility+'1').value = positionSheet.INIT_impliedVolatility_t 
        sheet.range(self.INIT_volume+'1').value = positionSheet.INIT_volume_t               
        sheet.range(self.INIT_openInterest+'1').value = positionSheet.INIT_openInterest_t
        
        sheet.range(self.LAST_TREND+'1').value = positionSheet.LAST_TREND_t
        sheet.range(self.LAST_SLOPE+'1').value = positionSheet.LAST_SLOPE_t        
        sheet.range(self.LAST_delta+'1').value = positionSheet.LAST_delta_t     
        sheet.range(self.LAST_impliedVolatility+'1').value = positionSheet.LAST_impliedVolatility_t         
        sheet.range(self.LAST_volume+'1').value = positionSheet.LAST_volume_t        
        sheet.range(self.LAST_openInterest+'1').value = positionSheet.LAST_openInterest_t  
            
        sheet.range(self.DEBUG+'1').value = positionSheet.DEBUG_t             
        
        sheet.range(self.SYMBOL+'1:'+self.DEBUG+'1').color = RGB.YELLOW  