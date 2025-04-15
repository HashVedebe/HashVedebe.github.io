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

#instead of writing the function, use lambda, sorted by house
people.sort(key=lambda kip: kip["house"])

print(people)