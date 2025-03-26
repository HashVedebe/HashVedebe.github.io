people = [
    {"name":"Alex", "house":"Ecausinnes"},
    {"name":"Manu", "house":"Lillehammer"}, 
    {"name":"Hilde", "house":"Pajottegem"}, 
    {"name":"Wingo","house":"Hondenhemel"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

#instead of writing the function, use lambda
people.sort(key=lambda person: person["house"])

print(people)