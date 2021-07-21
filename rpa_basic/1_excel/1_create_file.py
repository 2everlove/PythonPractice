""" terminal // $ pip install openpyxl """
from openpyxl import Workbook
wb = Workbook() # Create a new workbook
ws = wb.active # Imported the currently active sheet
ws.title = "RpaSheet" # Change name of sheet
wb.save("sample.xlsx")
wb.close()