#!/usr/bin/env python3
import random
import time

class Parkinglot():
    """ a parking lot has a finite number of cars waiting to be washed """
    def __init__(self):
        self.serial = random.randint(1000,9999)
        self.list_of_cars = []
    def initialize(self, number_of_cars):
        for index in range(number_of_cars):
            self.list_of_cars.append(random.randint(1000,9999))
        return
    def get_next_car(self):
        return self.list_of_cars.pop()

class Carwashbay():
    """ a car wash bay processes a single car at a time
        the driver is either happy or unhappy with the result """
    def __init__(self):
        self.serial = random.randint(1000,9999)
        self.wash_duration_in_seconds = random.randint(1,3)
    def wash_car(self, car_id):
        time.sleep(self.wash_duration_in_seconds)
        driver_satisfied = random.choice([True, True, True, False])
        return driver_satisfied


class InteriorDetailingStation():
    """ an interior detailing station processes a single car at a time
        the driver is either happy or unhappy with the result """
    def __init__(self):
        self.serial = random.randint(1000,9999)
        self.detailing_duration_in_seconds = random.randint(2,6)
    def detail_car(self, car_id):
        time.sleep(self.detailing_duration_in_seconds)
        driver_satisfied = random.choice([True, True, True, False])
        return driver_satisfied
