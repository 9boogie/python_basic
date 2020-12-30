cabinet = {3: 'Tei', 100: 'Jay'}

print(cabinet[3])
print(cabinet.get(100))

#print(cabinet[5]) error message because 5 is not existed
print(cabinet.get(5))
print(cabinet.get(5, "Usable"))


print(3 in cabinet)
print(5 in cabinet)

cabinet[3] = 'Max'
cabinet[7] = 'Nina'

print(cabinet)

del cabinet[7]
print(cabinet)

# Print only key
print(cabinet.keys())

# Print only value
print(cabinet.values())

# Print key and value
print(cabinet.items())

# Remove object
cabinet.clear()
print(cabinet)
