# This our class car
class Car:
    # attributes
    # variables inside a class/object
    model = None
    brand = None
    fuel = None
        
    ## Constructor
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def start(self):
        print(f"My {self.fuel} engine just started ...")

    def honk(self):
        print(f"My {self.brand} {self.model} just honked ...")

    def __repr__(self):
        return f"Car brand:{self.brand} model:{self.model} fuel:{self.fuel}"