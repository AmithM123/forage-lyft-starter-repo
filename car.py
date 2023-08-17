from abc import ABC, abstractmethod
from engine_battery.engines import Engines
from engine_battery.battery import Battery
from datetime import date

class Car(ABC):
    def __init__(self, engine: Engines, battery: Battery):
        self.engine = engine
        self.battery = battery


    @abstractmethod
    def needs_service(self,current_date: date, last_service_date: date):
        return self.engine.needs_service(current_date, last_service_date) or \
               self.battery.needs_service(current_date, last_service_date)
