from random import randint


class Weather:
    def __init__(self, wind_speed):
        self._wind_speed = wind_speed
    
    @property
    def wind_speed(self):
        return self._wind_speed


class RandomWeather(Weather):
    def __init__(self, weather):
        self._weather = weather

    @property
    def wind_speed(self):
        return randint(0, self._weather.wind_speed)
