import TLE_cal
from sheets import SheetCon
from pytz import timezone
from datetime import date, time, datetime, timedelta
from time import sleep
from pprint import pprint

satellite_name = "DUCHIFAT-3"
tleFile_URL = "https://www.celestrak.com/NORAD/elements/amateur.txt"
HSL_cordinates = [32.1624, 34.8447]
geoid = 19.2080
#delay = 60*60*12
delay = 60*60
countErros = 0

def get_currentDST():
    IsraelTimeZone = timezone("Israel")
    IsraelTime = datetime.now(IsraelTimeZone)
    return IsraelTime.dst()

#gets passes for the next 24 hours
def add_next_passes(start_time, sheet):
    #duchifat_3_TLE = TLE_cal.get_update_TLE(tleFile_URL, satellite_name)
    v = TLE_cal.get_passes(HSL_cordinates, geoid, satellite_name, start_time, 24, 5)
    for pass_ in v:
        pass_[0] = pass_[0] + timedelta(hours=2) + get_currentDST()
    v = TLE_cal.convert_passes_str(v)
    for line in v:
        sheet.add_pass(line)
        string = ""
        for cell in line:
            string += cell + ", "
        print(string)

while (True):
    sheet = SheetCon()
    try:
        countErros = 0
        time = sheet.find_last_pass()
        if (time < datetime.utcnow()):
            time = datetime.utcnow()
        if (datetime.utcnow() + timedelta(days = 2) > time):
            add_next_passes(time, sheet)
        print("\nstart delay")
        sleep(delay)
        print("end delay\n")
    except:
        if countErros > 10:
            break
            print("Learn to code bitch")
            sleep(60*60*24)
        else:
            print("Exception trying to get creds")
            sheet.createCreds()
            countErros += 1
            sleep(10)

#sheet.add_operators(["Yotam", "Yotam"], datetime.strptime("2020-02-24 01:59:24", "%Y-%m-%d %H:%M:%S"))
