from pyorbital import orbital
import urllib3

from datetime import date, time, datetime, timedelta
from pprint import pprint
from exceptions import SatelliteNotFound

#return a TLE of Duchifat-3 from 'tleFile_URL' in a list with 2 cells
#example: ['1 44854U 19089C   20031.47769533  .00000208  00000-0  23303-4 0  9997', '2 44854  36.9659 193.6942 0008882  14.3632 345.7372 14.98957921  7580']
def get_update_TLE(tleFile_URL, satellite_name):
    http = urllib3.PoolManager()
    r = http.request('GET', tleFile_URL)
    data_str = (str)(r.data)
    if satellite_name in data_str:
        data_str = data_str[data_str.find(satellite_name):]
        ret = []
        ret.append(data_str[data_str.find("\\r\\n1")+4:data_str.find("\\r\\n2")])
        ret.append(data_str[data_str.find("\\r\\n2")+4:-5])
        return ret
    else:
        raise SatelliteNotFound("Satellite not found in file")



def get_passes(ground_cor, alt, satellite_name, start_time, length, min_angle):
    satellite = orbital.Orbital(satellite_name)
    passes = satellite.get_next_passes(start_time + timedelta(seconds=1), length, ground_cor[1], ground_cor[0], alt)
    ret = []
    for line in passes:
        angle = (satellite.get_observer_look(line[2], ground_cor[1], ground_cor[0], alt))[1]
        if (angle >= (float)(min_angle)):
            p = [line[0], line[1] - line[0]]
            p.append(angle)
            ret.append(p)
    return ret


def convert_passes_str(passes):
    for line in passes:
        string = str(line[0])
        line[0] = str(string[0:string.find(".")])
        string = str(line[1])
        line[1] = str(string[0:string.find(".")])
        string = str(line[2])
        line[2] = string[string.find(":")+1:7]
        string = str(line[3])
        line[3] = string[0:6]
    return passes


def get_location_time(satellite_name, unix_UTC_time):
    satellite = orbital.Orbital(satellite_name)
    return satellite.get_position(datetime.utcfromtimestamp(unix_UTC_time))
