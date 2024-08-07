bookdict = {
    12345678: "Book 1",
    12345679: "Book 2",
    12345680: "Book 3",
    12345681: "Book 4",
    12345682: "Book 5",
}

print("Contents of the bookdict is:", bookdict)

# access dictionary items with brackets and key (or ' get' function)
bookname = bookdict[12345680]
# bookname = bokkdict.get(12345680)
print("Book is:", bookname)

# print all the keys in dictionary
for isbn in bookdict:
    print(isbn)

# print all the values in dictionary
for bookname in bookdict.values():
    print(bookname)

    # print keys and values in the dictionary
    for isbn, bookname in bookdict.items():
        print(isbn, bookname)

# check if specific key is found from dictionary
if 12345682 in bookdict:
    print("12345682 found in bookdict")

# add item to dictionary
bookdict[422344] = "New book"
print("Contents of the bookdict after adding a new item is:", bookdict)

# remove with pop
removebook = bookdict.pop(12345678)
print("Contents of the bookdict after pop is:", bookdict)

