user_str = input('Please input a string for us to play with: ')

# One way to do this.
empty_lst = []
for idx, char in enumerate(user_str):
    if idx % 2 != 0:
        empty_lst.append(char.upper())
    else:
        empty_lst.append(char.lower())

output_str = ''.join(empty_lst)

# A comprehension way to do this.
output_str = ''.join(char.upper() if idx % 2 != 0 else char.lower()
                     for idx, char in enumerate(user_str))

print(output_str)
