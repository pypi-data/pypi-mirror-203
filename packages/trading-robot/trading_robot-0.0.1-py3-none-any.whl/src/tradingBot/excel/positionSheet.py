from tradingBot.excel import dataSheet
from tradingBot.consts import RGB

class positionSheet(dataSheet.dataSheet):
    SYMBOL = 'A'    
    STRATEGY = 'B'
    P1ST = 'C'    
    P1SP = 'D'    
    P1SK = 'E'

    P1LT = 'F' 
    P1LP = 'G'
    P1LK = 'H'

    P2ST = 'I' 
    P2SP = 'J'
    P2SK = 'K'

    P2LT = 'L' 
    P2LP = 'M'
    P2LK = 'N'

    SPREAD = 'O'     
    
    OPEN_PRICE = 'P' 
    LAST_PRICE = 'Q'       
    EXP_PRICE = 'R'
    PL = 'S'    
    
    MAX_PROFIT = 'T'     
    MAX_LOSS = 'U'
    MARGIN = 'V'       
    PNL='W'
    WIN_PROB = 'X'   
    
    EXP_DATE = 'Y'    
    EARNING_DATE = 'Z' 
    GAIN = 'AA' 
    
    BREAKEVEN_L = 'AB'
    BREAKEVEN_H = 'AC'

    TRADE_DATE = 'AD'   
    LAST_QUOTE_DATE = 'AE'
      
    TRADE_STOCK_PRICE = 'AF'    
    LAST_STOCK_PRICE = 'AG'
    EXP_STOCK_PRICE = 'AH'       
        
    INIT_TREND = 'AI'
    LAST_TREND = 'AJ'    
    INIT_SLOPE = 'AK'
    LAST_SLOPE = 'AL'    
    INIT_delta = 'AM'         
    LAST_delta = 'AN'      
    INIT_impliedVolatility = 'AO'
    LAST_impliedVolatility = 'AP'     
    INIT_volume = 'AQ'    
    LAST_volume = 'AR'       
    INIT_openInterest = 'AS' 
    LAST_openInterest  = 'AT'           
    QUANTITY = 'AU'    
    STATUS='AV'

    UUID = 'AW'

    DEBUG = 'AX'    

    SYMBOL_t = 'Symbol'
    STRATEGY_t = 'Strategy' 
    
    P1SK_t  = 'p1 short K' 
    P1SP_t  = 'p1 short P' 
    P1ST_t  = 'p1 short T' 

    P1LK_t  = 'p1 long K' 
    P1LP_t  = 'p1 long P' 
    P1LT_t  = 'p1 long T'         

    P2SK_t  = 'p2 short K' 
    P2SP_t  = 'p2 short P' 
    P2ST_t  = 'p2 short T'         

    P2LK_t  = 'p2 long K'    
    P2LP_t  = 'p2 long P'    
    P2LT_t  = 'p2 long T'            
        
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
    MARGIN_t = 'Margin'        
    QUANTITY_t = 'Quantity'
    STATUS_t = 'Status'
    UUID_t = 'UUID'              

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
        if create:
            self.__init_sheet_header()  
        
    def __init_sheet_header(self):    
        sheet = self.sheet
            
        sheet.range(self.SYMBOL+'1').value = positionSheet.SYMBOL_t
        sheet.range(self.STRATEGY+'1').value = positionSheet.STRATEGY_t  

        sheet.range(self.P1SK+'1').value = positionSheet.P1SK_t 
        sheet.range(self.P1LK+'1').value = positionSheet.P1LK_t       
        sheet.range(self.P2SK+'1').value = positionSheet.P2SK_t 
        sheet.range(self.P2LK+'1').value = positionSheet.P2LK_t    

        sheet.range(self.P1SP+'1').value = positionSheet.P1SP_t 
        sheet.range(self.P1LP+'1').value = positionSheet.P1LP_t       
        sheet.range(self.P2SP+'1').value = positionSheet.P2SP_t 
        sheet.range(self.P2LP+'1').value = positionSheet.P2LP_t    

        sheet.range(self.P1ST+'1').value = positionSheet.P1ST_t 
        sheet.range(self.P1LT+'1').value = positionSheet.P1LT_t       
        sheet.range(self.P2ST+'1').value = positionSheet.P2ST_t 
        sheet.range(self.P2LT+'1').value = positionSheet.P2LT_t                    
        
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
        sheet.range(self.MARGIN+'1').value = positionSheet.MARGIN_t         
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

        sheet.range(self.QUANTITY+'1').value = positionSheet.QUANTITY_t            
        sheet.range(self.STATUS+'1').value = positionSheet.STATUS_t                   
        sheet.range(self.UUID+'1').value = positionSheet.UUID_t       
        sheet.range(self.DEBUG+'1').value = positionSheet.DEBUG_t        
        sheet.range(self.SYMBOL+'1:'+self.DEBUG+'1').color = RGB.YELLOW  

