# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])