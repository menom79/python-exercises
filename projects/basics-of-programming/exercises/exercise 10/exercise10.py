#Assignment 10.1
lastnames = []
name = input("Input a lastname (leave empty to end): ")
while name != "":
    lastnames.append(name)
    name = input("Input a lastname (leave empty to end): ")

file = open("lastnames.txt","w")
file.write("\n".join(lastnames))
file.close()
print("Inputted lastnames have been written to lastnames.txt")

#Assignment 10.2
try:
    file = open("names.txt", "r")
    txt = file.readlines()
    txt = list(map(str.strip, txt))
    txt.sort()

    check = []
    duplicates = 0
    for x in txt:
        if x in check:
            duplicates = duplicates + 1
        else:
            check.append(x)

    print(f"""Amount of names on the names.txt file: {len(txt)}
Names: {', '.join(txt)}
Amount of duplicate names: {duplicates}""")
except IOError as err:
    print(str(err))

#Assignment 10.3
t_input = input("Please enter a number to be saved externally: ")
ints_to_be_saved = []
floats_to_be_saved = []

def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

while t_input != "":
    if isint(t_input):
        ints_to_be_saved.append(t_input)
        t_input = input("Please enter a number to be saved externally: ")
    elif isfloat(t_input):
        floats_to_be_saved.append(t_input)
        t_input = input("Please enter a number to be saved externally: ")
    else:
        print("Input is not a number, saving inputs.")
        t_input = ""

int_file = open("ints.txt","w")
int_file.write("\n".join(ints_to_be_saved))
int_file.close()
float_file = open("floats.txt","w")
float_file.write("\n".join(floats_to_be_saved))
float_file.close()
print("Inputted numbers have been written to ints.txt and floats.txt respectively.")
