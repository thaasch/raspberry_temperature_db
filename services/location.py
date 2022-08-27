from geopy.geocoders import Nominatim
from dataclasses import dataclass

import geopy.geocoders
import certifi
import config
import ssl


@dataclass
class Location:
    name: str
    longitude: float
    latitude: float

    def __str__(self):
        return f'{self.name} - {self.longitude}:{self.latitude}'


def initialize_location_context():
    ctx = ssl._create_unverified_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx


def get_location_from(location_name):
    try:
        locator = Nominatim(scheme='https', user_agent='Weather')
        code = locator.geocode(location_name)
        return Location(code.address, code.longitude, code.latitude)
    except:
        return Location(config.FALLBACK_ADDRESS, config.FALLBACK_LONGITUDE, config.FALLBACK_LATITUDE)
