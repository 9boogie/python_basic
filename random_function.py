from random import *

print(random()) # pick the random number between 0.0 ~ 1.0 
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1) 

# # lotto number picker
# print(int((random()) * 45) + 1)
# print(int((random()) * 45) + 1)
# print(int((random()) * 45) + 1)
# print(int((random()) * 45) + 1)
# print(int((random()) * 45) + 1)
# print(int((random()) * 45) + 1)

print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))


print(randint(1, 45)) # pick the random number between 1 ~ 45

#Quiz
selectedOffline1 = randint(4, 28)
selectedOffline2 = randint(4, 28)
selectedOffline3 = randint(4, 28)
selectedOnline = randint(4, 28)
print('Every month of ', selectedOffline1, ' , ', selectedOffline2, ' , ', selectedOffline3, ' , ', selectedOnline, ' would be the study date' )