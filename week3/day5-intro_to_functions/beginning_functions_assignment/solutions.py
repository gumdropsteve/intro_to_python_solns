def calc_beers_on_the_wall(n=99):
    """Print how many beers remain on the wall.

    Args:
        n: int
            Holds the number of beers that remain on the wall.
    """

    print('{} bottles of beer are left on the wall.'.format(n))

def check_elsa_fan(fan=True):
    """Print a certain phrase depending on the value of fan.

    Args:
        fan: boolean
    """

    if fan:
        print("I love Elsa! She's my favorite!")
    else:
        print("Let It Go, it's not that great.")

def print_name(name):
    """Prints hello to the inputted name.

    Args:
        name: str
    """

    print('Hello {}'.format(name))

def check_if_divisor(n, potential_divisor=2):
    """Check if the inputted number (n) is divisible by the potential divisor.

    Args:
        n: int
        potential_divisor: int
    """

    return n % potential_divisor == 0

### The first version of compute_divisors simply ports the code over from the
### first week of solutions, whereas the second one is written more cleanly and
### more pythonically (i.e. using a for loop).

def compute_divisors(n):
    """Find all of the divisors of a user inputted number.

    Args:
        n: int
    """

    print('Our divisors are: ')

    idx = n

    while idx > 0:
        if n % idx == 0:
            print(idx)
        idx -= 1

def compute_divisors2(n):
    """Find all of the divisors of a user inputted number.

    Args:
        n: int
    """

    print('Our divisors are: ')

    for num in range(1, n + 1):
        if n % num == 0:
            print(num)

def find_least_common_multiple(num1, num2):
    """Find the least common multiple between the two inputted numbers.

    Args:
        num1: int
        num2: int
    """

    print('The least common multiple of these two numbers is: ')

    idx = num1
    if idx > num2:
        idx = num2

    while True:
        if  idx % num1 == 0 and idx % num2 == 0:
            found = True
            print(idx)
            break
        idx += 1

def check_if_beers_left(n):
    """Figure out if we have any beers left on our wall.

    Args:
        n: int
    """

    if n == 0:
        print('No beers left :( ')
    else:
        print('Beers left!')

def check_known_elsa_fans(name):
    """Check if the inputted person is an Elsa fan.

    Args:
        name: str
    """

    # Note how everything is lowercase here. When working with text like this,
    # lowercasing is often a good idea, since we don't want to differentiate
    # between Cary and cary. Both of these are the same to us, and we want the
    # code to reflect this.
    known_elsa_fans = ('sean' , 'cary', 'josh')

    if name.lower() in known_elsa_fans:
        return True
    else:
        return False

def get_sum(input_lst):
    """Find the sum of all numbers in the input list.

    Args:
        input_lst: list
    """

    total = 0

    for num in input_lst:
        total += num

    return total

def get_product(input_lst):
    """Find the product of all the numbers in the input list.

    Args:
        input_lst: list
    """

    total = 1

    for num in input_lst:
        total *= num

    return total

def return_evens(input_lst):
    """Return a list of all the evens in the input list.

    Args:
        input_lst: list
    """
    output_lst = []

    for num in input_lst:
        if num % 2 ==0:
            output_lst.append(num)

    return output_lst

    # List comp. way to do this.
    # output_lst = [num for num in input_lst if not num % 2]
