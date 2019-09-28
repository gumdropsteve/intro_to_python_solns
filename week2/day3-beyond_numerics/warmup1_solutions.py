# String Warmup #1
# i
my_str = 'This String was not Chosen Arbitrarily...'
print("Original String:")
print(my_str)
print(my_str[14])  # 's'

# ii
my_str = "This String wasn't Chosen Arbitrarily..."
print(my_str[14])  # 's'

# iii
print(my_str.lower())

# iv
my_str = 'This String was not Chosen Arbitrarily...'
my_str += "oR wAs it??"
print(my_str.upper())

# v
print(my_str[41:])

# vi
print(my_str[-11:].upper())

# vii
user_input = input('Add "oR wAs it??" (y/n)? \n')
my_str = 'This String was not Chosen Arbitrarily...'

if user_input == 'y':
    my_str += "oR wAs it??"
print(my_str)

# viii
user_input = input('String to add to the end of my_str: \n')
my_str = 'This String was not Chosen Arbitrarily...'

my_str += user_input
print(my_str)

# ix
user_input = input('String to add to the end of my_str: \n')
my_str = 'This String was not Chosen Arbitrarily...'

if len(user_input) < 10:
    my_str += user_input
print(my_str)
