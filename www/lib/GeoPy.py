from geopy.geocoders import Nominatim

class GeoData:

    def __init__(self,address,agent):
        self.address = address
        self.agent = agent

    def getCoords(self):
        try:
            geolocator = Nominatim(user_agent=self.agent)
            location = geolocator.geocode(self.address)
            self.lat = location.latitude
            self.lng = location.longitude
            self.address = location.address
            self.status=1
        except Exception as e:
            self.lat = 0
            self.lng = 0
            self.address = ""
            self.status=0
