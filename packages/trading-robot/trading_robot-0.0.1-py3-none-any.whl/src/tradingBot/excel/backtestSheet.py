from tradingBot.excel import dataSheet
from tradingBot.consts import RGB

class backtestSheet(dataSheet.dataSheet):
    
    SYMBOL = 'A'
    BENCH = 'B' 
    START_DATE = 'AA'
    END_DATE = 'AB'
    DEBUG = 'AC'
    
    strategy_header = []
    
    def __init__(self, wb, sheet_name, strategy_list):
        self.sheet_name = sheet_name
        self.strategy_list = strategy_list
        try:
            self.sheet = wb.sheets[sheet_name]
            self.sheet.clear()            
        except Exception as e:
            self.sheet = wb.sheets.add(sheet_name)  
            
        super().__init__(self.sheet)     
        self.__init_sheet_header()  
        
    def __init_sheet_header(self):        
        sheet = self.sheet
        sheet.range(self.SYMBOL+'1').value = 'Symbol'
        sheet.range(self.START_DATE+'1').value = 'Start Date'
        sheet.range(self.END_DATE+'1').value = 'End Date'
        sheet.range(self.BENCH+'1').value = 'Benchmark'    
        
        for strategy in self.strategy_list:  
            gain_col =   chr(ord(self.BENCH)+1+(self.strategy_list.index(strategy)))+'1'                               
            sheet.range(gain_col).value = strategy.get_name()+'\nGain' 
            
        self.DEBUG = chr(ord(self.BENCH)+len(self.strategy_list)+1)          
        sheet.range(self.DEBUG+'1').value = 'Debug'                                  
        sheet.range(self.SYMBOL+'1:'+self.DEBUG+'1').color = RGB.YELLOW         

