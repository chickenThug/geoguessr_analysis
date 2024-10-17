from geopy.geocoders import Nominatim
from geopy.exc import GeopyError
import logging


class Location:
    def __init__(self, latitude: str, longitude: str):
        geolocator = Nominatim(user_agent="geoapiExercises")
        try:
            self.location = geolocator.reverse(f"{latitude},{longitude}", exactly_one=True).raw['address']
        except GeopyError as e:
            logging.error("no location found", str(e))
            self.location = None

    def get_country_name(self):
        return self.location.get('country_name', None) if self.location else None
    
    def get_country_code(self):
        return self.location.get('country_code', None) if self.location else None

    def get_state(self):
        return self.location.get('state', None) if self.location else None