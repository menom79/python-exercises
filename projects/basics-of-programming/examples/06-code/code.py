# import the datetime to show current date and time
import datetime

def my_function(x):
    """purpose of this function is to increase given parameter by one
        
    parameters
    ----------
    x: int
        a numeric value that will be increased by one
    
    Returns
    -------
    int
        increaases parameter 'x' by one and returns result from the function
    """

    return x + 1


# print current date and time
print(datetime.datetime.now())

# declare varriable 'name' and assign some test into it
name = "Menom Haque"

# print contents of varriable 'name'
print(name)

# call the function
value = my_function(100)
print(value)
