def is_prime(n): 
    """Check whether an inputted number is prime.

    Args:
        n: Integer
    """

    prime = True

    for num in range(2, int(n ** 0.5) + 2):
        if n % num == 0:
            prime = False
            break

    if prime:
        print('The number you inputted is a prime number.')
    else:
        print('The number you inputted is not a prime number.')


is_prime(20)
is_prime(10)
is_prime(13)
is_prime(7)
is_prime(25)
