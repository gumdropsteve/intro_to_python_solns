user_str = input('Please enter a string for us to remove the vowels from: ')

vowels = {'a', 'e', 'i', 'o', 'u'}

# One way to do this.
for vowel in vowels:
    user_str = user_str.replace(vowel, '')

# Probably the most efficient way to do this.
user_str = ''.join(letter for letter in user_str if letter not in vowels)

print(user_str)
