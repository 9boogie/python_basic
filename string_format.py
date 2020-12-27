# print("a" + "b")

# print("c","d")

#Method 1
print('I am %d years old.' % 20)
print("I like %s very much" %"python")
print("Apple starts with %c." %"A" )

print("I am %s years old." %20)

print("I like color %s and color %s so much." % ("Blue", "Red"))

# Method 2
print("I am {} years old" .format(30))
print("I love {} dish and {} dish" .format("Pasta", "Sushi"))

print("I love {1} dish and {0} dish" .format("Pasta", "Sushi"))

# Method 3
print("I am {age} years old, I like color {color} very much." .format(age = 20, color="Red"))

# Method 4 (Python v3.6 ~)
age = 20
color = 'Red'
print(f"I am {age} years old, I like color {color} very much.")