#!/usr/bin/env python3

import inventory

if __name__ == "__main__": # https://stackoverflow.com/a/419185/1164295

    myitems = {}
    myitems['parking lot'] = inventory.Parkinglot()
    myitems['car wash bay'] = inventory.Carwashbay()

    myitems['parking lot'].initialize(number_of_cars=5)

    while len(myitems['parking lot'].list_of_cars)>0:
        car_id  = myitems['parking lot'].get_next_car()
        print('car ID =', car_id)
        driver_happy = myitems['car wash bay'].wash_car(car_id)
        print("driver happy:", driver_happy)
        if not driver_happy:
            myitems['parking lot'].list_of_cars = [car_id] + myitems['parking lot'].list_of_cars
