from datetime import date
from datetime import datetime
from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD,MUSLIM_WORLD_LEAGUE ,EGYPT ,MAKKAH ,KARACHI ,TEHRAN ,SHIA ,ASR_HANAFI
from .PrayTimes import PrayTimes

class PrayerData:

    def __init__(self,lat, lng, method,asr, timezone_offset=0):	
        self.timezone_offset = timezone_offset
        self.lat = lat
        self.lng = lng
        self.method = method
        self.asr = asr


    def _getTimes(self):

        try:
            params = {}
            params.update(eval(self.method))
            params.update(eval(self.asr))         


            adhan_times = adhan(
                day=date.today(),
                location=(self.lat,self.lng),
                parameters=params,
                timezone_offset=self.timezone_offset
                )
            return adhan_times

        except Exception as e: 
            return str(e)

    def getTimes(self):
        try:
            prayTimes = PrayTimes()
            prayTimes.setMethod(self.method)
            prayTimes.adjust({'asr': self.asr})
            times = prayTimes.getTimes(date.today(), (self.lat,self.lng), self.timezone_offset);
        
            _times={}
            for i in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
                _times[i.lower()] = datetime.strptime(str(datetime.now().date()) + ' ' + times[i.lower()], '%Y-%m-%d %H:%M')
                print(i.lower() + ":" + times[i.lower()])
            return _times
        except :
            print(str(e))
            return str(e)





   