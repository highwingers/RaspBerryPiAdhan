from datetime import date
from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD


class PrayerData:

    def __init__(self,lat, lng, timezone_offset=0):	
        self.timezone_offset = timezone_offset
        self.lat = lat
        self.lng = lng


    def getTimes(self):

        try:
            params = {}
            params.update(ISNA)
            params.update(ASR_STANDARD)

            adhan_times = adhan(
                day=date.today(),
                location=(self.lat,self.lng),
                parameters=params,
                timezone_offset=self.timezone_offset
                )
            return adhan_times

        except :
            return None


