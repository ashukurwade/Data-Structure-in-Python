A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
print(A | B)

# use union function
A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8}

# use union function on B
B.union(A)
{1, 2, 3, 4, 5, 6, 7, 8}