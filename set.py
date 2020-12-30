# No repetition and no sequence
my_set = {1, 1, 2, 3, 3, 3}
print(my_set)

java = {"Tom", "Marie", "John", "Steve"}
python = set(["Marie", "William", "Paul", "John"])

# Intersection
print(java & python)
print(java.intersection(python))

# Union
print(java | python)
print(java.union(python))

# Diffenece
print(java - python)
print(java.difference(python))

# 
python.add("Tom")
print(python)

java.remove("Steve")
print(java)