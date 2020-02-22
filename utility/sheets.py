import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import date, datetime
from exceptions import RowNotExists


class SheetCon:
    def __init__(self):
        self.scope = ["https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("Creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("Duchifat-3 table passes").sheet1
        self.row_insert = 3


    def add_pass(self, pass_info):
        self.sheet.insert_row(pass_info, self.row_insert, "RAW")


    def find_last_pass(self):
        info = self.sheet.cell(self.row_insert, 1).value
        if (len(info) == 0):
            return datetime.utcnow()
        else:
            return datetime.strptime(info, "%Y-%m-%d %H:%M:%S")


    def find_first_pass(self):
        info = "\0"
        row_number = self.row_insert

        while len(info) != 0:
            info = self.sheet.cell(row_number, 1).value
            print("line: " + str(row_number) + " value: " + info)
            row_number += 1

        if (row_number == self.row_insert+1 and len(info) == 0):
            return datetime.utcnow()
        
        row_number -= 2
        info = self.sheet.cell(row_number, 1).value
        time = datetime.strptime(info, "%Y-%m-%d %H:%M:%S")
        return time


    def find_row_pass(self, pass_time):
        info = "\0"
        row_number = self.row_insert

        while len(info) != 0:
            info = self.sheet.cell(row_number, 1).value
            time = datetime.strptime(info, "%Y-%m-%d %H:%M:%S")
            if (pass_time == time):
                return row_number
            row_number += 1
        raise RowNotExists("for time, " + str(info) + "I could not find a row")
    

    def add_operators(self, names, pass_time):
        cell_cor = [self.find_row_pass(pass_time), 5]
        cell_value = self.sheet.cell(cell_cor[0], cell_cor[1]).value
        
        for name in names:
            if cell_value.find(name) == -1:
                cell_value += ", " + name
        cell_value = cell_value[2:len(cell_value)]
        self.sheet.update_cell(cell_cor[0], cell_cor[1], cell_value)


    def get_passes(self, start_time, end_time):
        #todo: program function
        return "data"
    