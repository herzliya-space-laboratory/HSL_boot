import TLE_cal
from sheets import SheetCon
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
    v = TLE_cal.get_passes(HSL_cordinates, geoid, satellite_name, start_time, 24, 5)
    v = TLE_cal.convert_passes_str(v)
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
sheet.add_operators(["Elai", "רועי"], datetime.strptime("2020-02-23 01:58:27", "%Y-%m-%d %H:%M:%S"))
