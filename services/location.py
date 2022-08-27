import os
import ssl
from dataclasses import dataclass

import certifi
import geopy.geocoders
from dotenv import load_dotenv
from geopy.geocoders import Nominatim

load_dotenv()


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
        return Location(os.getenv('FALLBACK_ADDRESS'), float(os.getenv('FALLBACK_LONGITUDE')),
                        float(os.getenv('FALLBACK_LATITUDE')))
