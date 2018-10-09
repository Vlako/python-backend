from abc import ABC, abstractmethod


class Competition(ABC):
    def __init__(self, distance):
        self._distance = distance

    @abstractmethod
    def _get_competitor_time(self, competitor, weather):
        pass

    def start(self, competitors, weather):
        for competitor in competitors:
            competitor_time = self._get_competitor_time(competitor, weather)
            print(f"Car {competitor.name} result: {competitor_time}")


class RacingCompetition(Competition):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, distance):
        super().__init__(distance)

    def _get_competitor_time(self, competitor, weather):
        competitor_time = 0

        for distance in range(self._distance):
            _wind_speed = weather.wind_speed

            if competitor_time == 0:
                _speed = 1
            else:
                _speed = (competitor_time / competitor.time_to_max) * competitor.max_speed
                if _speed > _wind_speed:
                    _speed -= (competitor.drag_coef * _wind_speed)

            competitor_time += float(1) / _speed
        return competitor_time
