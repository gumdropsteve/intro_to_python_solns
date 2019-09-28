user_str = ''
while not user_str.isdigit():
    user_str = input('Please input a number to see if it is prime: ')
potential_prime = int(user_str)


idx = 2
prime = True

while idx <= potential_prime ** 0.5:
    if potential_prime % idx == 0:
        prime = False
        break
    idx += 1

if prime:
    print('The number you inputted is a prime number.')
else:
    print('The number you inputted is not a prime number.')
