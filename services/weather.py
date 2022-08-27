import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint

import datetime
import requests
from dotenv import load_dotenv

from services.dto import Measurement

load_dotenv()


class WeatherTemperatureClient(ABC):
    @abstractmethod
    def get_current_temperature(self, lat, long):
        pass


class WeatherTemperatureMockClient(WeatherTemperatureClient):
    def get_current_temperature(self, **kwargs):
        return [Measurement('TestData', randint(20, 30), datetime.datetime.now())]


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

        return Measurement(os.getenv('LOCATION_NAME'), main['temp'], datetime.datetime.now())
