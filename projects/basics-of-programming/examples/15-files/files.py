import os.path
import pickle
from vehicle import Vehicle

path = os.path.expanduser("~/files-example")
if not os.path.exists(path): os.makedirs(path)

print(path)
path += "/"
print(path)

filename = "files-example.txt"
file = open(path + filename, "w")
file.write("Files example, writing file to users home folder")
file.close()

filename = "multiline-text.txt"
lines = ["First line\n", "Second line\n", "Third line\n"]
try:
    file = open(path + filename, "w")
    file.writelines(lines)
except Exception as e:
    print("Failed to write file: " + filename)
finally:
    file.close()

lines = [""]
try:
    file = open(path + filename, "r")
    lines = file.readlines()
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

print(lines)


#declare a list of vehicles
vehicles = []
vehicles.append(Vehicle("Datsun", "Sunny", 1197, 29))
vehicles.append(Vehicle("BMW", "M5", 4899, 294))
vehicles.append(Vehicle("Toyota", "Supra", 2999, 200))
vehicles.append(Vehicle("Plymouth", "Cuda", 6399, 700))

for vehicle in vehicles:
    print(vehicle)

# dump vehicles into a binary file
filename = "vehicles.dat"
try:
    file = open(path + filename, "wb")
    pickle.dump(vehicles, file, pickle.HIGHEST_PROTOCOL)
except:
    print("Failed to write file:" + filename)
finally:
    file.close()

# read vehicles back from the file
vehicles.clear()

try:
    file = open(path + filename, "rb")
    vehicles = pickle.load(file)
except:
    print("Failed fo read file:" + filename)
finally:
    file.close()

# print the loaded vehicles
print("\n")
for vehicle in vehicles:
    print(vehicle)

print("All done, good job!")

