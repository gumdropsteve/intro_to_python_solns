user_str = input('Please input a string for us to play with: ')

# Using list indexes.
if user_str[-1] == '!':
    user_str = user_str.upper()
else:
    user_str = user_str.lower()

# Using a specific string method.
if user_str.endswith('!'):
    user_str = user_str.upper()
else:
    user_str = user_str.lower()

print(user_str)
