from datetime import date
from engine_battery.capulet_engine import CapuletEngine
from engine_battery.willoughby_engine import WilloughbyEngine
from engine_battery.sternman_engine import SternmanEngine
from engine_battery.nubbin_battery import NubbinBattery
from engine_battery.spindler_battery import SpindlerBattery
from car import Car
class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        #cuplet engine and spindler battery
        engine = CapuletEngine()  
        battery = SpindlerBattery() 
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine()  
        battery = SpindlerBattery() 
        
       
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine() 
        battery = SpindlerBattery() 
        
        
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine()  
        battery = NubbinBattery()  
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine() 
        battery = NubbinBattery()  
        car = Car(engine, battery)
        return car