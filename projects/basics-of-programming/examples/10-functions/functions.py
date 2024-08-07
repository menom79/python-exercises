from helper import *

def print_info():
    print("Info")

def print_and_return_number():
    print("Info - returning 123")
    return 123

def sum(number1, number2):
    return number1 + number2

def modify_text(text):
    text += ", this text is added by function"
    print(text)    

print("Calling function print_info")
print_info()
print("Call to function print_info done")

number = print_and_return_number()
print("print_and_return number returned ", number)

print("sum returned ", sum(5, number))

text = "About to call modify_text"
modify_text(text)
print(text)

number = sub(5, 11)
print("sub returned ", number)

