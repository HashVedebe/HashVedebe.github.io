#Define a list of names
names = ["Alex", "Manu", "Hilde", "Wingo"]

print(names)

print(names[0])

names.append("Poens")
names.sort()
print(names)

# create an empty set: unique values, not the value 3 twice
s = set()

#Add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

s.add(3)
s.remove(2)
print(s)

print(f"There are {len(s)} elements in the list")

geef_input = input("Geef een zin in: ")
print(f"Uw zin bevat {len(geef_input)} lettertekens")