import os

import requests
import json

api_key = os.getenv('API_KEY')
lat = "51.907902"
lon = "8.610630"
url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)


def getCurrentTemperature():
    response = requests.get(url)
    data = json.loads(response.text)
    current = data["main"]["temp"]

    return current
