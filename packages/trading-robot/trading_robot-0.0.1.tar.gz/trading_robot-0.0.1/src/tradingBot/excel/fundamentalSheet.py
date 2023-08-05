from tradingBot.excel import dataSheet
from tradingBot.consts import RGB

class fundamentalSheet(dataSheet.dataSheet):
    
    SYMBOL = 'A'
    LAST_PRICE = 'B'
    SUPPORT = 'C'
    RESISTENCE = 'D'
    RATING = 'E'
    TREND = 'F'
    SLOPE = 'G'
    
    BB_POS = 'H'
    RSI = 'I'
    MACD = 'J'
    MFI = 'K'

    EARNING = 'L'

    DAY_RANGE_POS = 'M'
    FIFTY_WEEKS_RANGE_POS = 'N'
    VOLUME_RANGE_POS = 'O'
    FORWARD_PE = 'P'
    HV = 'Q'
    IV1 = 'R'
    DELTA1 = 'S'    
    IV2 = 'T'
    DELTA2 = 'U'    
    IV3 = 'V'
    DELTA3 = 'W'    
    IV4 = 'X'
    DELTA4 = 'Y'
    QUOTE_TIME ='Z'
    DEBUG = 'AA'
    
    SYMBOL_t = 'Symbol'
    LAST_PRICE_t = 'Last Price'
    SUPPORT_t = 'Support'
    RESISTENCE_t = 'Resistence'
    RATING_t = 'Rating'
    TREND_t = 'Trend'
    SLOPE_t = 'Slope'

    BB_POS_t = 'BB Pos'
    RSI_t = 'RSI'
    MACD_t = 'MACD'
    MFI_t = 'MCI'

    EARNING_t = 'Earning'

    DAY_RANGE_POS_t = 'Day Range Pos'
    FIFTY_WEEKS_RANGE_POS_t = '52e Range Pos'
    VOLUME_RANGE_POS_t = '3M Volume pos'
    FORWARD_PE_t = 'Forward PE'
    HV_t = 'HV'
    IV1_t = 'IV1'
    DELTA1_t = 'Delta1'    
    IV2_t = 'IV2'
    DELTA2_t = 'Delta2'    
    IV3_t = 'IV3'
    DELTA3_t = 'Delta3'    
    IV4_t = 'IV4'
    DELTA4_t = 'Delta4'
    QUOTE_TIME_T = 'Quote Time'
    DEBUG_t = 'Debug'    
    
    def __init__(self, sheet):
        super().__init__(sheet)     
        self.__init_sheet_header()  
        
    def __init_sheet_header(self):        
        sheet = self.sheet
        sheet.range(self.SYMBOL+'1').value = fundamentalSheet.SYMBOL_t
        sheet.range(self.LAST_PRICE+'1').value = fundamentalSheet.LAST_PRICE_t
        sheet.range(self.SUPPORT+'1').value = fundamentalSheet.SUPPORT_t
        sheet.range(self.RESISTENCE+'1').value = fundamentalSheet.RESISTENCE_t        
        sheet.range(self.RATING+'1').value = fundamentalSheet.RATING_t                
        sheet.range(self.TREND+'1').value = fundamentalSheet.TREND_t     
        sheet.range(self.SLOPE+'1').value = fundamentalSheet.SLOPE_t             
        sheet.range(self.BB_POS+'1').value = fundamentalSheet.BB_POS_t
        sheet.range(self.RSI+'1').value = fundamentalSheet.RSI_t    
        sheet.range(self.MACD+'1').value = fundamentalSheet.MACD_t
        sheet.range(self.MFI+'1').value = fundamentalSheet.MFI_t
        sheet.range(self.EARNING+'1').value = fundamentalSheet.EARNING_t
        sheet.range(self.HV+'1').value = fundamentalSheet.HV_t
        sheet.range(self.IV1+'1').value = fundamentalSheet.IV1_t
        sheet.range(self.IV2+'1').value = fundamentalSheet.IV2_t
        sheet.range(self.IV3+'1').value = fundamentalSheet.IV3_t
        sheet.range(self.IV4+'1').value = fundamentalSheet.IV4_t        
        sheet.range(self.DAY_RANGE_POS+'1').value = fundamentalSheet.DAY_RANGE_POS_t 
        sheet.range(self.FIFTY_WEEKS_RANGE_POS+'1').value = fundamentalSheet.FIFTY_WEEKS_RANGE_POS_t
        sheet.range(self.VOLUME_RANGE_POS+'1').value = fundamentalSheet.VOLUME_RANGE_POS_t
        sheet.range(self.FORWARD_PE+'1').value = fundamentalSheet.FORWARD_PE_t
        sheet.range(self.DELTA1+'1').value = fundamentalSheet.DELTA1_t    
        sheet.range(self.DELTA2+'1').value = fundamentalSheet.DELTA2_t 
        sheet.range(self.DELTA3+'1').value = fundamentalSheet.DELTA3_t  
        sheet.range(self.DELTA4+'1').value = fundamentalSheet.DELTA4_t  
        sheet.range(self.QUOTE_TIME+'1').value = fundamentalSheet.QUOTE_TIME_T                       
        sheet.range(self.DEBUG+'1').value = fundamentalSheet.DEBUG_t    

        sheet.range('A1:'+self.DEBUG+'1').color = RGB.YELLOW          