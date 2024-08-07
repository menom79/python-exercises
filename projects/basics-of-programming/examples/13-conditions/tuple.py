# declare tuple of names and print
nametuple = ("Joe", "Sally", "Liam", "Robert", "Emma", "Isabella")
print("Contents of nametuple is:", nametuple)

print("Tuple element at index 1:", nametuple[1])
print("Tuple element at index -1:", nametuple[-1])
print("Tuple element at index 2:5:", nametuple[2:5])

# tuple can be converted to list
namelist = list(nametuple)
namelist[1] = "Mary"
nametuple = tuple(namelist)
print("Contents of nametuple is:", nametuple)

# tuple with only one item must be declared with trailing comma
nametuple = ("Joe",)
print(type(nametuple))

