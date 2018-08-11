import openpyxl

workbook = 'data/data.xlsx'
sheetName = 'data'
sheet = openpyxl.load_workbook(workbook)[sheetName]
total_amount = 0
for line in sheet['E2:I295']:
    total_amount+=line[4].value
