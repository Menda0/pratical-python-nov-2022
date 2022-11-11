# 1. Create a class that defines an athlete
# 2. Athlete have the following attributes
# energy -> int value that contais the athlete energy
# name -> string with name of the athlete
# 3. Athlete must have the following methods:
# run -> when the athlete runs it must decrease one point of energy
# eat(int) -> when the athlete eats it must restore n points of energy
# constructor -> the athlete must have 4 points of energy
# 4. Create/Define a new __repr__ function that prints the athlete name and energy points
# 5. Try to run and eat something with the athlete, print the athlete whenever your preform an action

### Provided by Fernando Pina ###
class Atleta:
    # atributos
    # variaveis da classe/objeto
    energy = 0
    name = None

    def __init__(self, name) :  # construtor para inicializar atributos da classe
        self.energy = 4
        self.name = name

    def run(self):                          
        self.energy -= 1
        self.eat(2)             # ADD ON: corre e come sempre para recuperar 2 pontos de energia

    def eat(self, food):                         
        self.energy =self.energy + food

    def __repr__(self):
        return f"Atleta: {self.name}, com {self.energy} de energia"

fernando = Atleta("Fernando")
print(fernando)

fernando.run()
fernando.run()

print(fernando)

fernando.eat(4)

print(fernando)

fernando.eat(2)

print(fernando)

### Provided by Fernando Paz ### 

class Athlete():
    energy = None
    name = None

    def init(self, energy, name):
        self.energy = 4
        self.name = "Pepe rápido"
    
    def eat(self):
        self.energy = self.energy + 1
    
    def run(self):
        self.energy = self.energy - 1


runner = Athlete(4, "Pepe Rápido")

sair = False

while not sair:
    option = input("Select Run (1), Eat (2) ou Quit (3): ")
    print("\n")

    if option == "1":
        if runner.energy > 4:
            runner.run()
            print(f"{runner.name} ran like hell and his energy is down to {runner.energy}!")
        else:
            print(f"{runner.name} is too tired. Must eat before it can run again!")
    if option == "2":
        runner.eat()
        print(f"{runner.name}'s energy is up to {runner.energy}! Roarrrr!!")
    if option == "3": 
        sair = True

    print("\n")

# 1. Create a class Animal with attributes:
# type -> mamal, bird, reptil, etc
# name -> Bear, Dog, Cat, Parrot
# noise -> noise that the animal makes
# 2. Create a method called speak. That prints the noise of the animal
# (Example: Miau, Auaua, Pipiu)
# 3. Create a subclass that represents a type of animal
# (Example: Bird, Mamal, Reptil)
# 4. Create 6 animals instances of multiple types
# (Example: mamal_dog, reptil_cobra, bird_eagle)
# 5. Make everyone speak

