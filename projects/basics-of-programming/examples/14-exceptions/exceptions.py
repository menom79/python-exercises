try:
    number1 = 100
    numbre2 = 0
    result = number1 / numbre2
    print("Result is", result)
except ZeroDivisionError:
    print("Can't divide by zero!")

print("Continuing...")

try:
    number = int(input("Gimme a number: "))
    print("You entered: ", number)
except ValueError:
    print("Unable to convert text to number")
except:
    print("Something else went wrong :(")

try:
    numbers = [1, 2, 3, 4, 5]
    print("Last number is", numbers[4])
except IndexError:
    print("Wrong index used in accessing list")

finally:
    print("Finally!")

def safe_division(x, y):
    if y == 0:
        raise Exception("Exception from safe_division")
    return x / y

try:
    result = safe_division(100, 0)
except:
    print("safe_division raised an exeption")

def someday_something_here():
    raise NotImplementedError("This function is not currently implemented")

someday_something_here()    

print("all done!")

