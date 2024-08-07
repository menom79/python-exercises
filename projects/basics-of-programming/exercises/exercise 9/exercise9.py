#Assignment 9.1
list = ["one","two","three","four"]
#list[4] = "five" Commented to stop the code from breaking
#Causes; IndexError: list assignment index out of range
list.append("five")
print(list)

#Assignment 9.2
import os
import errno
list = os.listdir("C:/")
print(list)
#new_file = open("C:/ayho.txt", "x")
#Causes; PermissionError: [Errno 13] Permission denied: 'C:/ayho.txt'
#Solution, use try. Also import errno so we can inform the user what's wrong.
try:
    new_file = open("C:/ayho.txt","x")
    print("File created succesfully.")
    pass
except IOError as err:
    print("File creation failed.")
    if err.errno == errno.EACCES:
        print("Missing permissions.")
    else:
        print(err.errno, ",", err.strerror)

#Assignment 9.3
#If any statement fails in the try-block, execution of it will end.
def isthiszero(num):
    if type(num) != int:
        raise TypeError("Input must be an integer.")
    return num == 0

try:
    print(isthiszero(2))
    print(isthiszero("yes"))
    print(isthiszero(0))
except TypeError as err:
    print(f"Error in input: {str(err)}")
