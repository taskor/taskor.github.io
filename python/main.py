'''print("Hello World!")

print("--------------------------------------------------------------")
print("Comments")
print("A one line commment would start with a # symbol.")
print("A multi-line comment can be enclosed in triple quotes.")
print("Feel free to comment out any segment you don't want to run.")

print("--------------------------------------------------------------")
print("Your name")
name = input("Name: ")
print(f"Hello, {name}!")

print("--------------------------------------------------------------")
print("Your Country")
country = input("Country: ")
print("You are from: " + country)

print("--------------------------------------------------------------")
print("Your number")
n = int(input("Enter a number: "))
if n > 0:
    print("Your number is positive.")
elif n < 0:
    print("Your number is negative.")
else:
    print("Your number is zero.")

    print("--------------------------------------------------------------")
print("Names")
names = ["Vladimir", "Maiia", "Taisiia", "Tatiana"]
print("The first name is: " + names[0])
print("The second name is: " + names[1])
print("The third name is: " + names[2])
print("The fourth name is: " + names[3])

print("--------------------------------------------------------------")
print("The alphabet")
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("The first letter is: " + alphabet[0])
print("The second letter is: " + alphabet[1])
print("The third letter is: " + alphabet[2])
print("The fourth letter is: " + alphabet[3])
print("The fifth letter is: " + alphabet[4])
print("The sixth letter is: " + alphabet[5])
print("The seventh letter is: " + alphabet[6])
print("The eighth letter is: " + alphabet[7])
print("The ninth letter is: " + alphabet[8])
print("The tenth letter is: " + alphabet[9])
print("The eleventh letter is: " + alphabet[10])
print("The twelfth letter is: " + alphabet[11])
print("The thirteenth letter is: " + alphabet[12])
print("The fourteenth letter is: " + alphabet[13])
print("The fifteenth letter is: " + alphabet[14])
print("The sixteenth letter is: " + alphabet[15])
print("The seventeenth letter is: " + alphabet[16])
print("The eighteenth letter is: " + alphabet[17])
print("The nineteenth letter is: " + alphabet[18])
print("The twentieth letter is: " + alphabet[19])
print("The twenty-first letter is: " + alphabet[20])
print("The twenty-second letter is: " + alphabet[21])
print("The twenty-third letter is: " + alphabet[22])
print("The twenty-fourth letter is: " + alphabet[23])
print("The twenty-fifth letter is: " + alphabet[24])
print("The twenty-sixth letter is: " + alphabet[25])

print("--------------------------------------------------------------")
print("Coordinates")
coordinates = (10, 20)
print("The first coordinate is: " + str(coordinates[0]))
print("The second coordinate is: " + str(coordinates[1]))

print("--------------------------------------------------------------")
print("Names appended and sorted in alphabetical order")
names.append("Masha")
names.sort()
print(names)

print("--------------------------------------------------------------")
print("Sets")
firstSet = set()
print("We have created an empty set.")
firstSet.add("mew")
firstSet.add("meow")
firstSet.add("meow mew")
firstSet.add("mew meow")
print("We have added some elements to the set:")
print(firstSet)
firstSet.add("mew")
print("We have wrote 'mew' again, but it is not added again because sets do not allow duplicates:")
print(firstSet)
print("We can also remove an element from the set:")
firstSet.remove("meow")
print(firstSet)
print("We can see the length of the set:")
print(f"Our set has {len(firstSet)} elements.")          

print("--------------------------------------------------------------")
print("Loops")
for i in range(15):
    print (i)
for name in names:
    print(name)

print("--------------------------------------------------------------")
print("Dictionaries")
people = {"46yr": "Vladimir", "45yr" : "Tatiana", "21yr" : "Maiia"}
print(people["46yr"])
print(people["45yr"])
print(people["21yr"])
print("The oldest person is: " + people["46yr"])
print("The youngest person is: " + people["21yr"])
people["11yr"] = "Taisiia"
print(f"The new youngest person is: {people['11yr']}")

print("--------------------------------------------------------------")
print("Object-Oriented Programming")
print("--------------------------------------------------------------")
print("Classes")
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)

class Flight():
    def __init__ (self, capaicty):
        self.capacity = capaicty
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Maiia", "Taisiia", "Tatiana", "Vladimir"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"{person} has been added to the flight.")
    else:
        print(f"{person} could not be added to the flight due to no available seats.")

print("--------------------------------------------------------------")
print("Decorators")
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Function has been run.")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()

print("--------------------------------------------------------------")
print("Lambda Functions")
people = [
    {"name": "Maiia", "house": "Gryfinndor"},
    {"name": "Taisiia", "house": "Ravenclaw"},
    {"name": "Tatiana", "house": "Hufflepuff"},
    {"name": "Vladimir", "house": "Slytherin"}
]
people.sort(key=lambda person: person["name"])

print(people)
'''
print("--------------------------------------------------------------")
print("Exceptions")
import sys
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
    sys.exit(1)

print(f"The quotient of {x} divided by {y} is: {result}")