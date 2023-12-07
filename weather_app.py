from os import getenv
from dotenv import load_dotenv
from requests import get
import json


class WeatherApp:

    def __init__(self, city) -> None:
        load_dotenv()
        self.weather_api = getenv("WEATHER_APP_KEY", default=None)
        self.city = city

    def get_weather_city(self):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={
            self.city}&appid={self.weather_api}&lang=fr'
        response = get(url)
        response.encoding = 'ISO-8859-1'
        return response.json()

    @staticmethod
    def write_json(data):
        with open("file.json", "w") as file:
            json.dump(data, file)


vix = WeatherApp('vix')
data = vix.get_weather_city()
vix.write_json(data)
