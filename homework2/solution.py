from homework2.car import CarFactory
from homework2.competition import RacingCompetition
from homework2.weather import Weather, RandomWeather

car_factory = CarFactory()
competitors_name = ['ferrary', 'bugatti', 'toyota', 'lada', 'sx4']
competitors = [car_factory.create(name) for name in competitors_name]

weather = RandomWeather(Weather(20))
RacingCompetition(distance=10000).start(competitors, weather)
