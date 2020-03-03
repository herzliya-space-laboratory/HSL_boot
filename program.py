import utility.TLE_cal
from utility.sheets import SheetCon
from datetime import date, time, datetime, timedelta
from pprint import pprint

satellite_name = "DUCHIFAT-3"
tleFile_URL = "https://www.celestrak.com/NORAD/elements/amateur.txt"
HSL_cordinates = [32.1624, 34.8447]
geoid = 19.2080
sheet = SheetCon()

#gets passes for the next 24 hours
def add_next_passes(start_time):
    #duchifat_3_TLE = TLE_cal.get_update_TLE(tleFile_URL, satellite_name)
    v = utility.TLE_cal.get_passes(HSL_cordinates, geoid, satellite_name, start_time, 24, 5)
    for pass_ in v:
        pass_[0] = pass_[0] + timedelta(hours=2)
    v = utility.TLE_cal.convert_passes_str(v)
    for line in v:
        sheet.add_pass(line)
        string = ""
        for cell in line:
            string += cell + ", "
        print(string)

time = sheet.find_last_pass()
if (time < datetime.utcnow()):
    time = datetime.utcnow()
if (datetime.utcnow() + timedelta(days = 2) > time):
    add_next_passes(time)
sheet.add_yotam_passes()
#sheet.add_operators(["Yotam", "Yotam"], datetime.strptime("2020-02-24 01:59:24", "%Y-%m-%d %H:%M:%S"))
