# # student id was 1 2 4 ..., but change it to 101, 102, 103, 104 ...

# studnets = [1,2,3,4,5]
# print(studnets)
# studnets = [i+100 for i in studnets]
# print(studnets)

# # convert name into length
# users = ["Tommy", "I am groot", "Thor", "MJ"]
# users = [len(i) for i in users]
# print(users)

# # convert name into uppercase
# roommates = ["Tommy", "I am groot", "Thor", "MJ"]
# roommates = [i.upper() for i in roommates]
# print(roommates)

#Quiz
from random import *

total = 0
for customer in range(1, 51):
  time = randrange(5, 51)
  if 5 <= time <= 15:
    print("[O] Client #: {0} (Take {1} mins)".format(customer, time))
    total += 1
  else:
    print("[ ] Client #: {0} (Take {1} mins)".format(customer, time))

print("Total clients used COCOA service Today: {0}".format(total))