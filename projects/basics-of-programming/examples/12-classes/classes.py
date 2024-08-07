# importthe Vehicle class from another source file
from vehicle import Vehicle

# text = "something"
# number = 1
#accountBalance = 100.53

# declare an object 'datsun' from 'Vehicle' class
datsun = Vehicle("Datsun", "100A", 998, 12)
toyota = Vehicle("Toyota", "Celica", 1588, 43)

# print cars
print(datsun)
print(toyota)

print("datsun horsepower is: ", datsun.horsepower(), "hp")
print("toyota horsepower is: ", toyota.horsepower(), "hp")


