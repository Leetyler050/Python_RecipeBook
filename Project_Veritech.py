##cd /Users/tylerlee/Documents/Personal_Projects/Veritech

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import datetime
from datetime import datetime
##from time import gmtime, strftime
##strftime("%Y-%m-%d %H:%M:%S", gmtime())
datetime.now().strftime('%Y-%m-%d %H:%M:%S')


dfi = pd.read_excel('Veritech_Workbook_1.0.xlsx', sheetname='Ingredients')
dfe = pd.read_excel('Veritech_Workbook_1.0.xlsx', sheetname='Equipment')
dfe = pd.read_excel('Veritech_Workbook_1.0.xlsx', sheetname='Directions')
dfn = pd.read_excel('Veritech_Workbook_1.0.xlsx', sheetname='Notes')

print("Column headings:")
print(dfi.columns)

dpie = dfi[dfi['Recipe_Name'] == 'Pie Crust']


##This is the next iteration in creating easy to input recipes
##df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['pie','crust'])
