"""
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
p = Point(2, 8)

print(p.x)
print(p.y)
"""

#Vliegtuigcapaciteit
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(3)

people = ["Alex", "Manu", "Hilde", "Wingo"]

for person in people:
    succes = flight.add_passenger(person)
    if succes:
        print(f"Added {person} successfully to flight.")
    else:
        print(f"No available seats for {person}.")

