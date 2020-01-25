from datetime import date
from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD,MUSLIM_WORLD_LEAGUE ,EGYPT ,MAKKAH ,KARACHI ,TEHRAN ,SHIA ,ASR_HANAFI


class PrayerData:

    def __init__(self,lat, lng, method, timezone_offset=0):	
        self.timezone_offset = timezone_offset
        self.lat = lat
        self.lng = lng
        self.method = method


    def getTimes(self):

        try:
            params = {}
            params.update(eval(self.method))
            params.update(ASR_STANDARD)         


            adhan_times = adhan(
                day=date.today(),
                location=(self.lat,self.lng),
                parameters=params,
                timezone_offset=self.timezone_offset
                )
            return adhan_times

        except Exception as e: 
            return str(e)



   