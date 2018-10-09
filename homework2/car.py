class Car:
    def __init__(self, name, max_speed, drag_coef, time_to_max):
        self._name = name
        self._max_speed = max_speed
        self._drag_coef = drag_coef
        self._time_to_max = time_to_max
        
    @property
    def name(self):
        return self._name
        
    @property
    def max_speed(self):
        return self._max_speed
    
    @property
    def drag_coef(self):
        return self._drag_coef
    
    @property
    def time_to_max(self):
        return self._time_to_max


class CarFactory:
    def __init__(self):
        self._cars = {
            'ferrary': lambda: Car(name='ferrary', max_speed=340, drag_coef=0.324, time_to_max=26),
            'bugatti': lambda: Car(name='bugatti', max_speed=407, drag_coef=0.39, time_to_max=32),
            'toyota': lambda: Car(name='toyota', max_speed=180, drag_coef=0.25, time_to_max=40),
            'lada': lambda: Car(name='lada', max_speed=180, drag_coef=0.32, time_to_max=56),
            'sx4': lambda: Car(name='sx4', max_speed=180, drag_coef=0.33, time_to_max=44),
        }

    def create(self, name):
        return self._cars[name]()
