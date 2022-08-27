from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint

import dateutil.utils
import requests

import config
import services.registers as registers

from services.dto import Weather


class WeatherTemperatureClient(ABC):
    @abstractmethod
    def get_current_temperature(self, lat, long):
        pass


class WeatherTemperatureMockClient(WeatherTemperatureClient):
    def get_current_temperature(self, **kwargs):
        return [Weather('TestData', randint(20, 30), dateutil.utils.today())]


@dataclass
class WeatherTemperatureWebParameters:
    longitude: str
    latitude: str
    api_key: str


class WeatherTemperatureWebClient(WeatherTemperatureClient):
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric";

    def get_current_temperature(self, **kwargs):
        parameters = WeatherTemperatureWebParameters(**kwargs)

        response = requests.get(self.url.format(parameters.latitude, parameters.longitude, parameters.api_key))
        data = response.json()
        main = data['main']

        return Weather(config.LOCATION_NAME, main['temp'], dateutil.utils.today())
