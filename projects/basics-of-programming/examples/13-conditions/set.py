# declare a set of names and print
nameset = {"Joe", 'Sally', "Liam", "Robert", "Emma", "Isabella"}
print("Contents of nameset is:", nameset)

for name in nameset:
    print(name)

print("Length of the set is:", len(nameset))

name = "Sally"
print(name + " is in set:", name in nameset)

nameset.add("Bella")
print("Contents of nameset after add is:", nameset)

nameset.update({"Harry", "Elisa", "Pocahontas"})
print("Contents of nameset after update is:", nameset)

nameset.remove("Liam")
nameset.discard("Liam2")
print("Contents of nameset after remove is:", nameset)

