#from module_example.math import fib, fact

from module_example import fib, fact

# module_example -> module
# domain -> folder inside module_example
# module_example.domain.EletricCar -> ElectricCar.py
# import ElectricCar -> Class ElecticCar(Car)
from module_example.domain.EletricCar import ElectricCar

# from module_example import circle_area
import module_example

# pip install requests
import requests

print("fib(24) =", fib(24))
print("fact(24) =", fact(24))

tesla = ElectricCar("Tesla", "Model S")

print(tesla)

print("circle_area(10) =", module_example.circle_area(10))

url = "https://dog-api.kinduff.com/api/facts?number=10"

result = {
    "facts":[
        "A Russian dog named Laika was the first animal in space, traveling around Earth in 1957.","Most vets recommend that female dogs don’t get pregnant until the third estrus.",
        "A dog’s mouth exerts 150–200 pounds of pressure per square inch with some dogs exerting up to 450 pounds per square inch.",
        "Zorba, an English mastiff, is the biggest dog ever recorded. He weighed 343 pounds and measured 8’ 3\" from his nose to his tail.",
        "Female dogs can get pregnant when their bodies undergo changes which make them receptive to male dogs. This is called being on heat or in estrus.",
        "Dogs normally have between one to sixteen or even more puppies.","Dogs can count up to five and can perform simple mathematical calculations.",
        "In 2002 alone, more people in the U.S. were killed by dogs than by sharks in the past 100 years.","A dog’s pregnancy lasts for approximately 60 days."
    ],
    "success":True
}

response = requests.get(url)
dog_facts = response.json()

for fact in dog_facts["facts"]:
    print(fact)