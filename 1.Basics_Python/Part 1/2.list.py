#List is mutable. Can be created in 2 ways
my_list = [1, 2, 3, 4, 5, 1]
print(my_list)

my_list2 = list((6, 7, 8, 9, 10))
print(my_list2)

my_list3 = my_list.sort()
print(my_list3)  # This will print None because sort() sorts the list in place and returns None
print(my_list)  # This will print the sorted list