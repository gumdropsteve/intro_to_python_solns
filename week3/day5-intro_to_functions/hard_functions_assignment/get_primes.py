def get_primes(n):
    """Find all primes up to the inputted number.

    Args:
        n: Integer
    """

    primes = []
    for num in range(n):
        if is_prime(num):
            primes.append(num)

    ''' List comprehension way to do this.

    primes = [num for num in range(n) if is_prime(num)]

    '''

    return primes

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

    return prime

print(get_primes(5))
print(get_primes(9))
print(get_primes(27))
print(get_primes(225))
print(get_primes(100))
