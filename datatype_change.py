menu = {"coffee", "milk", "juice"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#Quiz
from random import *
people = range(1, 21)
people = list(people)
shuffle(people)
print(people)
winner = sample(people, 4)
print(winner)
shuffle(winner)
chicken = winner[0]
coffee = winner[1:]
print(chicken)
print(coffee)