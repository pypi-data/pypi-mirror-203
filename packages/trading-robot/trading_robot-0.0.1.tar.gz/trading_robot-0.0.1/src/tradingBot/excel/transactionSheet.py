from tradingBot.excel import dataSheet
from tradingBot.consts import RGB

class transactionSheet(dataSheet.dataSheet):
    TRX_TIME='A'
    SYMBOL = 'B'    
    TYPE = 'C'    
    BUY_SELL='D'
    OPEN_CLOSE='E'
    STRIKE = 'F'
    EXP_DATE= 'G'
    QUANTITY = 'H'
    PRICE = 'I'
    COMMISSION = 'J'
    FEE = 'K'
    AMOUNT = 'L'                
    DEBUG = 'M'    
    
    TRX_TIME_t='Trx Time'
    BUY_SELL_t='Buy/Sell'
    OPEN_CLOSE_t='Open/Close'
    SYMBOL_t = 'Symbol'
    TYPE_t = 'Type'
    STRIKE_t = 'Strike'
    EXP_DATE_t = 'Exp Date'
    QUANTITY_t = 'Quantity'
    PRICE_t = 'Price'
    COMMISSION_t = 'Commission'
    FEE_t = 'Fee'
    AMOUNT_t  = 'Amount'      
    DEBUG_t = 'Debug'                 

    OPEN = 'open'
    CLOSE = 'close'
    BUY = 'buy'
    SELL = 'sell'          
                              
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

        sheet.range(self.TRX_TIME+'1').value = transactionSheet.TRX_TIME_t
        sheet.range(self.BUY_SELL+'1').value = transactionSheet.BUY_SELL_t  
        sheet.range(self.OPEN_CLOSE+'1').value = transactionSheet.OPEN_CLOSE_t 
        sheet.range(self.SYMBOL+'1').value = transactionSheet.SYMBOL_t       
        sheet.range(self.TYPE+'1').value = transactionSheet.TYPE_t 
        sheet.range(self.STRIKE +'1').value = transactionSheet.STRIKE_t    
        sheet.range(self.EXP_DATE+'1').value = transactionSheet.EXP_DATE_t
        sheet.range(self.QUANTITY+'1').value = transactionSheet.QUANTITY_t      
        sheet.range(self.PRICE+'1').value = transactionSheet.PRICE_t
        sheet.range(self.COMMISSION+'1').value = transactionSheet.COMMISSION_t        
        sheet.range(self.FEE+'1').value = transactionSheet.FEE_t  
        sheet.range(self.AMOUNT+'1').value = transactionSheet.AMOUNT_t     
        sheet.range(self.DEBUG+'1').value = transactionSheet.DEBUG_t             
        sheet.range(self.TRX_TIME+'1:'+self.DEBUG+'1').color = RGB.YELLOW  