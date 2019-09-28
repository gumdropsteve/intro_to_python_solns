# List Warmup #2
my_list = [1, 'hello', 2, 'there', 3, 'list']

# i
print(my_list[1])   # 'hello'
print(my_list[0])   # 1

# ii
print(my_list[1::2])

# iii
my_list = [1, 'hello', 2, 'there', 3, 'list']
my_list.append(4)
print(my_list)

# iv
print(my_list[::2])

# v
my_list = [1, 'hello', 2, 'there', 3, 'list']
my_list.append(4)
my_list.remove('list')
print(my_list)

# vi
print(my_list[1::2])

# vii
my_list = [1, 'hello', 2, 'there', 3, 'list']
user_input = input('Add the number 4 to mylist (y/n)? \n')
if user_input == 'y':
    my_list.append(4)
print(my_list)

# viii
my_list = [1, 'hello', 2, 'there', 3, 'list']
user_input = input('Type a string to add to the list: \n')
if len(user_input) < 8:
    my_list.append(user_input)
else:
    my_list.append(4)
print(my_list)
