my_list = ['a', 's', 'h', 'u', 't', 'o', 's', 'h']

# first item
print(my_list[0])  # a

# third item
print(my_list[2])  # s

# fifth item
print(my_list[4])  # u

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

# Error Only integer can be used for indexing
print(my_list[4.0])