#Tuples are immutable
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0:3])  # Slicing the tuple

my_list = list(my_tuple)  # Converting tuple to list
print(my_list)

#Dictionaries are mutable
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict2 = dict(name='Bob', age=30, city='Los Angeles')  # Another way to create a dictionary
print(my_dict)
print(my_dict2)

#To retrive keys
print(my_dict.keys())

#To retrive values
print(my_dict.values())

#Check values are there in the dictionary

print('name' in my_dict)  # True

#Print value of a key
print(my_dict['name'])  # Alice

'''
Note:
When there is unordered data and no worries about memory allocation - List
    
When there is ordered data and it needs to be memory efficient - Tuple

When there is key-value pair data  used for faster lookups and quick indexing - Dictionary
'''
