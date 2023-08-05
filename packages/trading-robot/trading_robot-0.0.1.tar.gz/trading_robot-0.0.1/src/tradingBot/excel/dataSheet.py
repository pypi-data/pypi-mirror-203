import pandas as pd

class dataSheet(object):
    def __init__(self, sheet):
        self.sheet = sheet       
        
    def to_df(self):
        return self.sheet.range('A1').options(pd.DataFrame, 
                                        header=1,
                                        index=False, 
                                        expand='table').value    
    
    def update_cell(self, column_name, row_num, value=None, link_address=None, font_color=None, font_bold=False):            
        cell = column_name+str(row_num)
        if link_address != None:
            self.sheet.range(cell).add_hyperlink(link_address, screen_tip='Click to see picture')        
        if value != None:
            self.sheet.range(cell).value = value
        if font_color != None:
            self.sheet.range(cell).font.color = font_color

        if font_bold == True:
            self.sheet.range(cell).font.bold = font_bold   

    def update_range(self, start, end, value=None, link_address=None, font_color=None, font_bold=False):            
        cell_range = start+':'+end
        if value != None:
            self.sheet.range(cell_range).value = value
        if  font_color != None:
            self.sheet.range(cell_range).font.color = font_color
        self.sheet.range(cell_range).font.bold = font_bold   
        if link_address != None:
            self.sheet.range(cell_range).add_hyperlink(link_address, screen_tip='Click to see picture')

            