number = 10
while number >= 0 and number < 100:
    print(number)
    number -= 1

for i in range(10):
    print("Looping range(10): ", i)

for i in range(5, 10):
    print("Looping range(5, 10): ", i)

for i in range(0, 10, 2):
    print("Looping range(0, 10, 2): ", i)

text = "Basics of programming with Python"
for character in text:
    print(character)

names = ["jani", "John", "Mamun", "Menom"]
for name in names:
    print(name)

# use of break and continue
print("Running a while loop with break and continue")
number = 0
while True:
    number = int(input("Enter a number (0 to exit, 100 ignored): "))
    if number == 0:
        break
    elif number == 100:
        print("Ignored")
        continue

    print("You entered: ", number)

print("All done, exiting app")
