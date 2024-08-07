number = 5
accountbalance = 110.54
print(number)
print(accountbalance)

number = 55
number2 = number + 2
#value of number2 is now 57
print("number2 is", number2)

# print("number2 is" + str(number2))

number = number * number2
print("number2 is", number)

number += 10
number = number + 10
print("number2 is", number)

print("Type of variable number is", type(number))
print("Type of variable number is", type(accountbalance))


# strings
# initialize a string from text
name = "Mahmudul"
lastName = "Haque"

#initialize string from another variable
fullName = name

# add strings
fullName = name + " " + lastName
print(fullName)

#use Format function
age = 26
fullName = "First name: {}. Last name: {}. Age: {}".format(name, lastName, age)
print(fullName)

#fullName = "First name: " + name + ". Last name: " + lastName + ". Age: " + str(age)
#print(fullName)

# access characters in a string
text = "ABC"
a = text[0]
b = text[1]
c = text[2]
print(f"Second char is " + b)

print("Text length is " + str(len(text)) + " characters.")


#compare strings
text2 = "ABD"
if text == text2:
    print("Texts are identical.")
else:
    print("Texts are different")


# read text from console
line = input("Enter a line of text: ")
print("You entered: " + line)

line = input("Enter a number: ")
number = int(line)
print("Number is ", number)

