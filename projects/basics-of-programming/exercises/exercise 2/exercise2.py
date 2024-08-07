# 2.1

height = 165

print("Height of a person: " + str(height) + " " + "centimeters")

# 2.2

number1 = input("Enter a number: ")
number2 = input("Enter another number: ")

sum = int(number1) + int(number2)
sub = int(number1) - int(number2)
multi = int(number1) * int(number2)
div = int(number1) / int(number2)

print("Sum:", sum)
print("Subtraction:", sub)
print("Multiplication:", multi)
print("Division:", div)

# 2.3

balance = 2000

print("Bank account balance: " + str(balance) + " " + "€")

new_add = input("How many euros will be added to the balance? ")
add_cents = input("How many cents will be added to the balance? ")

cents = int(add_cents) / int(100)
newBalance = float(int(balance) + int(new_add) + cents)
 
print("Bank account balance: " + str(newBalance) + " " + "€")

