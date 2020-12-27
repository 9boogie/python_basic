# List []

# Subway
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["Tom", "Ebbie", "Paul"]
print(subway)

print(subway.index('Paul'))

# Add to the end
subway.append("Mike")
print(subway)

# Add based on index
subway.insert(1, "Marie")
print(subway)

# Remove from the back
print(subway.pop())
print(subway)

# Check the count
subway.append("Tom")
print(subway.count("Tom"))

# Sort and reverse sort
num_list = [5, 4, 7, 3, 1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

# Delete
num_list.clear()
print(num_list)

# Various data type can be used
mix_list = ["Joe", 30, True]
print(mix_list)

# Merge lists
subway.extend(mix_list)
print(subway)
