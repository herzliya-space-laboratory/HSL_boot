import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("Creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("tutorial").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell

insertRow = ["hello", 5, "red", "blue"]
sheet.insert_row(insertRow, 1, "Raw")

sheet.update_cell(2,2, "CHANGED")  # Update one cell

numRows = sheet.row_count  # Get the number of rows in the sheet