
bmw = {
    "model": "s1",
    "brand": "bmw",
    "fuel": "diesel"
}

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

# golf = Car()
# golf.brand = "Volkswagen"
# golf.model = "Golf"
# golf.fuel = "Diesel"

# print("golf =", golf)
# print("type(golf) =", type(golf))

# ibiza = Car()
# ibiza.brand = "Seat"
# ibiza.model = "Ibiza"
# ibiza.fuel = "Diesel"

# print("golf.brand =", golf.brand)
# print("ibiza.brand =", ibiza.brand)

# Object instances
tesla = Car("Tesla", "S", "Eletric")
print("tesla.brand =", tesla.brand)

# Object instances
seat = Car("Seat", "Leon", "Diesel")

print("seat.model =", seat.model)
print("seat.brand =", seat.brand)
print("seat.fuel =", seat.fuel)

tesla.start()
seat.start()

seat.honk()

print("tesla =", tesla)

class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model, "eletric")

    def charge(self):
        print(f"{self} is charging ...")

class DieselCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model, "diesel")

renault = ElectricCar("renault", "zoe")
opel = DieselCar("opel", "astra")


print("renault =", renault)
print("opel =", opel)

renault.honk()

renault.charge()

# Cannot to that
# Undefined method in class DieselCar
# opel.charge()