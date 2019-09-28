user_str = input('Please input a string to look for a letter in: ').lower()
user_letter = input('Please input a letter to look for: ').lower()

# To practice with for loops, we can do this.
found = False
for char in user_str:
    if char == user_letter:
        found = True
        break

# To practice with string methods, we can do this.
if user_str.count(user_letter):
    found = True

if found:
    print('Character found!')
else:
    print('Character not found!')
