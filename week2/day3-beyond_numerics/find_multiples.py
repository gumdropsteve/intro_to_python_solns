user_num1 = ''
user_num2 = ''

while not user_num1.isdigit() and not user_num2.isdigit():
    user_num1 = input('Please enter a digit to to get multiples of: ')
    user_num2 = input('Please enter a digit to go up to for our search: ')

user_num1 = int(user_num1)
user_num2 = int(user_num2)

# Using a for loop.
multiples = []
for num in range(1, user_num2 // user_num1):
    multiples.append(num * user_num1)

# Using a list comp.
multiples = [num * user_num1 for num in range(1, user_num2 // user_num1)]
print(multiples)
