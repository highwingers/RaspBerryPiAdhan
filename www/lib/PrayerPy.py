from datetime import date
from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD
from GeoPy import GeoData


class PrayerData:

	def __init__(self,address,agent, timezone_offset):	
		self.address = address
		self.agent = agent
		self.timezone_offset = timezone_offset

		self.getTimes()

	def getTimes(self):
		
		geo = GeoData(self.address,self.agent)
		params = {}
		params.update(ISNA)
		params.update(ASR_STANDARD)

		adhan_times = adhan(day=date.today(),
							location=(geo.lat,geo.lng),
							parameters=params,
							timezone_offset=self.timezone_offset
							)
		return adhan_times

