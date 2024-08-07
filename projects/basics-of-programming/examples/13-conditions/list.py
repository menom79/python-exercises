# declare a list of numbers and initialize
list = [5, 10, 15]

# append adds new item to the end of the list
list.append(100)

# insert new item to the somewhere into the list
list.insert(1, 7)

# list items can be accessed by [] operator
print("List element at index 1: ", list[1])
print("List element at index -1: ", list[-1])

# list item can be updated with [] operator
list[1] = 60

# index can also be specified as range
print("List elements at range 2:5", list[2:5])

# remove item from the list
# only a first occurence of the item is removed
list.remove(10)
print("List contents after 10 was removed: ", list)

# pop function allows to remove an item at index
# pop also returns the value at that index before removing it from the list
value = list.pop(1)
print("pop(1) value: ", value)
print("List contents afte pop(1): ", list)

# another way to remove item by index is 'del'
del list[1]
print("List contents after del list[1]: ", list)

# clear contents of the list
list.clear()

# print contents of the list
print("List contents: ", list)


# declare list of names and print
namelist = ["Joe", "Sally", "Liam", "Robert", "Emma", "Issabela"]
print(namelist)

# loop thru the list
for name in namelist:
    print(name)

# use 'len' function to get number of elements in the collection
print("namelist length is: ", len(namelist))

# check if item exists in the list
if "Liam" in namelist:
    print("Yes, 'Liam' is in the name list")

# assignment operator creats a reference to another collection
anothernamelist = namelist
anothernamelist[0] = "Roger"
print(namelist)

# use copy if you really want another copy of the list
anothernamelist = namelist.copy()
anothernamelist[0] = "Harris"
anothernamelist[-1] = "Mary"
print("Contents of namelist: ", namelist)
print("Contents of anothernamelist: ", anothernamelist)

# combine list to another
combinedlist = namelist + anothernamelist
#combinedlist = namelist.copy()
#combinedlist.extend(anothernamelist)
print("Contents of combinedlist:",combinedlist)

 