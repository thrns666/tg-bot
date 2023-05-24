import yaweather
import json
import config_bot


class Weather:
    def __init__(self, coordinates):
        self.coordinates: tuple
        self.__api_key: str = config_bot.YANDEX_KEY
        self.__yandex_weather_obj = yaweather.YaWeather(api_key=self.__api_key)
        self.result = self.__yandex_weather_obj.informers(coordinates=coordinates, lang='ru_RU').json()
        self.res = json.loads(self.result)
        self.temp_fact: float = self.res['fact']['temp']
        self.temp_feel: float = self.res['fact']['feels_like']
        self.condition: str = self.res['fact']['condition']
        self.wind_direction: str = self.res['fact']['wind_dir']
        self.wind_gust_speed: str = self.res['fact']['wind_gust']
        self.wind_speed: str = self.res['fact']['wind_speed']
        self.humidity: float = self.res['fact']['humidity']
        self.pressure: int = self.res['fact']['pressure_mm']
        self.sunset: str = self.res['forecast']['sunset']
        self.sunrise: str = self.res['forecast']['sunrise']
