user_str = ''
while not user_str.isdigit():
    user_str = input('Please input a number to see if it is prime: ')
potential_prime = int(user_str)


prime = True

for num in range(2, int(potential_prime ** 0.5) + 2):
    if potential_prime % num == 0:
        prime = False
        break

if prime:
    print('The number you inputted is a prime number.')
else:
    print('The number you inputted is not a prime number.')
