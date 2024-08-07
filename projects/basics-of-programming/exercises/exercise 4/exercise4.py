# 4.1

fname = input("Enter first name: ")
lname = input("Enter last name: ")

for character in fname:
    print(fname[0], end = "")

print("", lname[::-1])

# 4.2

import random

numbers = int(input("How many sets of lottery numbers to generate: "))

def lottery(numbers):
    for numbers in range(numbers):
        lottery_numbers = random.sample(range(1,41), 7)
        print(lottery_numbers)

lottery(numbers)

