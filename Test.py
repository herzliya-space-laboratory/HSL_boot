from datetime import datetime
from pytz import timezone

def get_currentDST():
    return datetime.now(timezone("Israel")).dst()

tz = timezone('Israel')
now = datetime.now(tz)
print(now.dst())
print(get_currentDST())