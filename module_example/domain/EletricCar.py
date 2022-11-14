# . -> actual folder(module)
# Car -> file Car.py
# import Car -> Class inside Car.py file
from .Car import Car

class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model, "eletric")

    def charge(self):
        print(f"{self} is charging ...")