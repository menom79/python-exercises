# 7.1

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return 'Name: ' + self.name + ', Age: ' + str(self.age)
        
human_A = Human('Adam', 18)
human_E = Human('Eva', 18)

print(human_A)
print(human_E)

# 7.2

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def __str__(self):
        return self.name + ', Color: ' + self.color
        
    def meow(self):
        print(self.name + ' says: Meoooooow!')
        
kit = Cat('Kit', 'black')
kat = Cat('Kat', 'white')

print(kit)
print(kat)

kit.meow()
kat.meow()

# 7.3

import random

class Car:
    
    def __init__(self, brand = "", model = "", price = ""):
        self.brand = brand
        self.model = model
        self.price = price
             
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)
           
    brand = ""
    model = ""
    price = ""

car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

print("1. brand:", car1)
print("2. brand:", car2)
print("3. brand:", car3)
print("Total price of your cars is:", car1.price + car2.price + car3.price)

car1 = Car("Audi", "XV22", random.randint(1000, 10000))
car2 = Car("BMW", "XV8", random.randint(1000, 10000))
car3 = Car("Ford", "XV88",random.randint(1000, 10000))
car4 = Car("Opel", "XV104", random.randint(1000, 10000))
car5 = Car("Skoda", "XV8-05", random.randint(1000, 10000))

print("car1:", car1)
print("car2:", car2)
print("car3:", car3)
print("car4:", car4)
print("car5:", car5)

