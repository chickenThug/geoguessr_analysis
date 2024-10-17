from geopy.geocoders import Nominatim
from geopy.exc import GeopyError
import logging
import time

class Location:
    def __init__(self, latitude: str, longitude: str):
        time.sleep(1)
        try:
            geolocator = Nominatim(user_agent="geoapiExercises", timeout=10)
            self.location = geolocator.reverse(f"{latitude},{longitude}", exactly_one=True, language='en').raw['address']
        except GeopyError as e:
            logging.error("no location found", str(e))
            self.localtion = None
        except Exception as e:
            logging.error("no location found", str(e))
            self.localtion = None

    def get_country_name(self):
        return self.location.get('country', None) if self.location else None
    
    def get_country_code(self):
        return self.location.get('country_code', None) if self.location else None

    def get_state(self):
        return self.location.get('state', None) if self.location else None