from random import *

def step():
    print("Inside 'step' function")
    print("All done here, exiting step function")

def step_with_params(param1, param2):
    if param1 > param2:
        print("param1 is larger than param2")
    else:
        print("param1 is smaller or equal to param2")

    param1 += param2
    param2 += param1

    step()
    print("All done here, exiting step_with_params functions")


number1 = 10
number2 = randint(0, 100)

print("value of number1 is", number1)
print("value of number2 is", number2)

# I want to swap the values of number1 and number2
# How to do it?
temp = number1
number1 = number2
number2 = temp

print("value of number1 is", number1)
print("value of number2 is", number2)

step()
step_with_params(number1, number2)

print("debugger.py, all done, exiting.")

