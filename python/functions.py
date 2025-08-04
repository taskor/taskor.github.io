def square(x):
    return x * x

print("--------------------------------------------------------------")
print("Object-Oriented Programming (added from main.py)")
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