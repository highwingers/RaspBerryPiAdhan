from lib.PrayerPy import PrayerData
from lib.Dal import Dal
from datetime import datetime

data = Dal().GetSettings(1)
speaker = data[1]
lat = data[2]
lng = data[3]
method = data[4]
asr = data[5]

prayTimes = PrayerData(lat, lng, 'Karachi', asr, 5).getTimes()


#-------------------------- Test Code --------------------------

# sample code to run in standalone mode only
if __name__ == "__main__":
    from datetime import date



    times = prayTimes


    print(times)

