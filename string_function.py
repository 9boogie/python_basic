python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "JavaScript"))

index = python.index("n") #Find first "n"
print(index)
index = python.index("n", index + 1) # Find second "n"
print(index)

print(python.find("n"))
print(python.find("u")) # If letter is not exist, give the '-1' as result
#print(python.index("u")) # If not exist, error caused

print(python.count("n"))