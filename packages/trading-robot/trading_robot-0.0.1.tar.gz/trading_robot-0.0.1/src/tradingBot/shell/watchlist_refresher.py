import xlwings as xw
from tradingBot.excel import watchListBook as wb

acc_file_path = r'C:\Users\jimhu\option_trader\assets\static\assets\data\jihuang.xlsm' 

watchBook = wb.watchListBook(acc_file_path)

watchBook.refresh_all_watch_list(update_TD=True)