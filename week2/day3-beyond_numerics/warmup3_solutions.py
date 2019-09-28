# Loop Warmup #3
# i
my_list = ['hello', 'there', 'python', list('list'), '!']
for element in my_list:
    print(element)

# > hello
# > there
# > python
# > ['l', 'i', 's', 't']
# > !

# ii
my_list = ['hello', 'there', 'python', list('list'), '!']
for i, element in enumerate(my_list):
    print(i, element)

# iii
my_list = ['hello', 'there', 'python', list('list'), '!']
for i, element in enumerate(my_list):
    if i % 2 != 0:
        print(i, element)

# iv
my_list = ['hello', 'there', 'python', list('list'), '!']
for i, element in enumerate(my_list):
    if len(element) > 4:
        print(i, element)

# v
longer_elements = []
my_list = ['hello', 'there', 'python', list('list'), '!']
for i, element in enumerate(my_list):
    if len(element) > 4:
        longer_elements.append(element)
print(longer_elements)

# vi
longer_elements = []
my_list = ['hello', 'there', 'python', list('list'), '!']
for i, element in enumerate(my_list):
    if len(element) > 4:
        longer_elements.append(element)
    print(longer_elements)

# vii
user_number = int(input('Min length to be printed: \n'))
longer_elements = []
my_list = ['hello', 'there', 'python', list('list'), '!']
for i, element in enumerate(my_list):
    if len(element) > user_number:
        longer_elements.append(element)
    print(longer_elements)
