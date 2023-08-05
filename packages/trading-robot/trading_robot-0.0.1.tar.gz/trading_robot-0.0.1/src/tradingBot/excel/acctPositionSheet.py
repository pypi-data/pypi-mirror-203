from tradingBot.excel import dataSheet
from tradingBot.consts import RGB

class acctPositionSheet(dataSheet.dataSheet):
    SYMBOL = 'A'    
    TYPE = 'B'
    QUANTITY = 'C'
    STRIKE = 'D' 
    EXP_DATE = 'E'
    LAST_PRICE = 'F'
    CURRENT_VALUE = 'G'     
    TOTAL_GAIN_LOSS = 'H' 
    TOTAL_GAIN_LOSS_PERCENT = 'I'
    TOTAL_COST_BASIS = 'J'      
    AVERAGE_COST_BASIS = 'K'        
    STATUS='L'
    UUID = 'M'            

    DEBUG = 'N'    

    INIT_BALANCE = 'P'

    SYMBOL_t = 'Symbol'
    TYPE_t = 'Type'     
    QUANTITY_t  = 'Quantity' 
    STRIKE_t  = 'Strike'       
    EXP_DATE_t  = 'Exp Date' 
    LAST_PRICE_t  = 'Last Price'            
    CURRENT_VALUE_t = 'Current Value'         
    TOTAL_GAIN_LOSS_t  = 'Total Gain/Loss Dollar'
    TOTAL_GAIN_LOSS_PERCENT_t  = 'Total Gain/Loss Percent'        
    TOTAL_COST_BASIS_t = 'Total Cost Basis'
    AVERAGE_COST_BASIS_t = 'Average Cost Basis'
    INIT_BALANCE_t = 'Initial Balance'
    STATUS_t = 'Status'    
    UUID_t = 'op UUID'

    # asset types
    CALL = 'call'
    PUT = 'put'
    STOCK = 'stock'
    CASH = 'cash'

    # operations
    BUY = 'buy'
    SELL = 'sell'
    OPEN = 'open'
    CLOSE = 'close'
             
    DEBUG_t = 'Debug'                        
                              
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
            
        sheet.range(self.SYMBOL+'1').value =  acctPositionSheet.SYMBOL_t
        sheet.range(self.TYPE+'1').value =  acctPositionSheet.TYPE_t  
        sheet.range(self.QUANTITY+'1').value =  acctPositionSheet.QUANTITY_t 
        sheet.range(self.STRIKE+'1').value =  acctPositionSheet.STRIKE_t       
        sheet.range(self.EXP_DATE+'1').value =  acctPositionSheet.EXP_DATE_t           
        sheet.range(self.LAST_PRICE+'1').value =  acctPositionSheet.LAST_PRICE_t 
        sheet.range(self.CURRENT_VALUE+'1').value =  acctPositionSheet.CURRENT_VALUE_t    
        
        sheet.range(self.TOTAL_GAIN_LOSS+'1').value =  acctPositionSheet.TOTAL_GAIN_LOSS_t 
        
        sheet.range(self.TOTAL_GAIN_LOSS_PERCENT+'1').value =  acctPositionSheet.TOTAL_GAIN_LOSS_PERCENT_t
        sheet.range(self.TOTAL_COST_BASIS+'1').value =  acctPositionSheet.TOTAL_COST_BASIS_t      
        sheet.range(self.AVERAGE_COST_BASIS+'1').value =  acctPositionSheet.AVERAGE_COST_BASIS_t
            
        sheet.range(self.DEBUG+'1').value =  acctPositionSheet.DEBUG_t             
        sheet.range(self.SYMBOL+'1:'+self.DEBUG+'1').color = RGB.YELLOW  
        sheet.range(self.INIT_BALANCE+'1').value = acctPositionSheet.INIT_BALANCE_t  
        sheet.range(self.STATUS+'1').value = acctPositionSheet.STATUS_t              
        sheet.range(self.UUID+'1').value = acctPositionSheet.UUID_t  

        sheet.range(self.INIT_BALANCE+'1:'+self.INIT_BALANCE+'1').color = RGB.GREEN            