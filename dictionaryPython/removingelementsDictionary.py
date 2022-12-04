# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
print(squares.pop(4))
print(squares)

# remove all items
squares.clear()
print(squares)

# delete the dictionary itself
del squares
# Throws Error
print(squares)