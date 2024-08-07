# 5.1

def show_info():
    print("I'm Utils.Info")

# 5.2

def subtract():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    subtract = number1 - number2
    print("Subtraction: ", subtract)


def average():
    number1 = float(input("Enter 1st number: "))
    number2 = float(input("Enter 2nd number: "))
    number3 = float(input("Enter 3rd number: "))
    avg = (number1 + number2 + number3) / 3
    print("Average is:", '%.1f' %avg)

# 5.3

from consumption import *

def calc_consumption():
    fuel_consumed = (consumption * Distance) / 100
    cost = price * fuel_consumed
    print("Fuel consumed:", '%.2f' %fuel_consumed, "liter")
    print("Cost:", '%.2f' %cost, "€")