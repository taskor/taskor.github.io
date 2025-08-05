# square function
def square(x):
    return x * x

# Point class
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)

# Flight class
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

# Decorators
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
# Lambda Functions
people = [
    {"name": "Maiia", "house": "Gryfinndor"},
    {"name": "Taisiia", "house": "Ravenclaw"},
    {"name": "Tatiana", "house": "Hufflepuff"},
    {"name": "Vladimir", "house": "Slytherin"}
]
people.sort(key=lambda person: person["name"])

print(people)