# 3.1

age = int(input("Tell me your age: "))

if age < 13:
    print("child")
elif age >= 13 and age <= 19:
    print("teen")
elif age >= 20 and age <= 65:
    print("adult")
else:
    print("senior")

# 3.2

num1 = int(input("Input integer: "))
num2 = int(input("Input another integer: "))
num3 = int(input("One more: "))

if num1 >= num2 and num1 >= num3:
   largest = num1
elif num2 >= num1 and num2 >= num3:
   largest = num2
else:
   largest = num3

print("Max value:", largest)

# 3.3

points = float(input("Insert your points: "))

if points <= 1:
    print("Grade: 0")
elif points >= 2 and points <= 3:
    print("Grade: 1")
elif points >= 4 and points <= 5:
    print("Grade: 2")
elif points >= 6 and points <= 7:
    print("Grade: 3")
elif points >= 8 and points <= 9:
    print("Grade: 4")
elif points >= 10 and points <= 12:
    print("Grade: 5")
else:
    print("Invalid input!")

# 3.4

num1 = int(input("Input number: "))
num2 = int(input("Input number: "))
num3 = int(input("Input number: "))
num4 = int(input("Input number: "))
num5 = int(input("Input number: "))

if num1 < 0:
    num1 = 0
if num2 < 0:
    num2 = 0
if num3 < 0:
    num3 = 0
if num4 < 0:
    num4 = 0
if num5 < 0:
    num5 = 0

sum = num1 + num2 + num3 + num4 + num5

print("Sum is", sum)

