# 6.1

def time():
    number = int(input("Please enter seconds: "))
    hours = number // 3600
    minutes = (number % 3600) // 60
    seconds = (number % 3600) % 60
    print(hours,":",minutes,":",seconds)
    
time()

# 6.2

def celToFah():
    celcius = float(input("Enter temperature in celsius:"))
    fahrenheit = ((celcius * (9/5)) + 32)
    print("%.1f" %fahrenheit)

celToFah()

def fahToCel():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celcius = ((fahrenheit -32) * (5/9))
    print("%.1f" %celcius)

fahToCel()

# 6.3

names = []
while True:
    name = input('Enter student name:')
    if name == '':
        break
    else:
        names.append(name)

print("Student count:", len(names))
print(*names, sep=', ')

# 6.4

points = []
for i in range(1, 6):
    prompt = 'Give points for judge ' + str(i) + ':'
    point = input(prompt)
    points.append(int(point))

total = sum(points) - min(points) - max(points)
print("Total points are:", total)

