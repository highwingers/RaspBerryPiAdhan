from geopy.geocoders import Nominatim

class GeoData:

    def __init__(self,address,agent):
        self.address = address
        self.agent = agent

    def getCoords(self):
        geolocator = Nominatim(user_agent=self.agent)
        location = geolocator.geocode(self.address)
        self.lat = location.latitude
        self.lng = location.longitude
        self.address = location.address