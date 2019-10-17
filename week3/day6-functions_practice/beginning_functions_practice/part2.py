# The solution for question 1. 
def get_month_season(month, unk_month):
    '''
    Input:  Str - Abbreviation of month
    Output: Str - Season of inputted month
    '''
    season = None
    if month in ('dec', 'jan', 'feb'):
        season = 'Winter'
    elif month in ('mar', 'apr', 'may'):
        season = 'Spring'
    elif month in ('jun', 'jul', 'aug'):
        season = 'Summer'
    elif month in ('jun', 'jul', 'aug'):
        season = 'Summer'
    else:
        season = unk_month
    return season

def month_info(month, category):
    '''
    Input:  Str - Abbreviation of month, Str - information category to get for month
    Output: Str - category information for the specified month

    Categories supported: 'full name'   ex: month_info('jan', 'full_name') -----> 'January'
                          'num_month'   ex: month_info('may', 'num_month') ----->  5
                          'birth_stone' ex: month_info('jul', 'birth_stone') ---> 'Ruby' 
                          'season'      ex: month_info('oct', 'season') --------> 'Fall'
    '''
    full_names = {'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
                  'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
                  'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}

    month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 
                  'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

    birth_stones = {'jan': 'Garnet', 'feb': 'Amethyst', 'mar': 'Aquamarine', 'apr': 'Diamond',
                    'may': 'Emerald', 'jun': 'Pearl', 'jul': 'Ruby', 'aug': 'Peridot',
                    'sep': 'Sapphire', 'oct': 'Opal', 'nov': 'Topaz', 'dec': 'Turquoise'}
    
    unk_month = 'Unknown month'
    # Note that we are using the unk_month here so that we can gracefully handle the scenario 
    # where the caller of our function inputs an unknown month. The alternative would be to not 
    # do this, and instead have our program break if a user inputs an unknown month. It's better
    # practice to do the former, and try to give callers some useful information if they use 
    # the function we have built in a way we weren't intending (i.e. passing in an unknown month). 
    if category == 'full_name':
        return full_names.get(month, unk_month)
    elif category == 'num_month':
        return month_nums.get(month, unk_month)
    elif category == 'birth_stone':
        return birth_stones.get(month, unk_month)
    elif category == 'season':
        return get_month_season(month, unk_month)
    else:
        return 'Unknown category'

# This is the solution for question 2. 

def perfect_square(num):
    '''
    Input:  Int
    Output: Bool

    Return True if num is a perfect square, e.g. 9 = 3 x 3. Return False if num is not
    a perfect square, 8 isn't any integer multiplied by itself.
    '''
    sqrt_num = num ** 0.5
    return sqrt_num == int(sqrt_num)

def next_perfect_square(num):
    '''
    Input:  Int
    Output: Int

    Ex: next_perfect_square(10) --> -1
        next_perfect_square(9) ---> 16
        next_perfect_square(25) --> 36
        next_perfect_square(37) --> -1

    Returns the next perfect square (a number that is the square of an integer e.g. 81 = 9 x 9)
    greater than the inputted number. If the inputted number is not a perfect square, return -1.
    (i.e. the inputted number must also be a perfect square).
    '''
    if not perfect_square(num):
        return -1

    i = num + 1
    while True:
        if perfect_square(i):
            break
        i += 1
    return i

# This is the solution for question 3. 
import random

def flip_coin():
    '''
    Input:  None
    Output: Str - 'H' for head or 'T' for tail

    Perform an "experiment" using random.random(), return 'H' if result is above .5, 'T' otherwise.
    '''
    test_num = random.random()
    # This is what is known as the ternary operator. It is just a one line shorthand for an if-else block, 
    # similar to how list and dictionary comprehensions are shorthand for creating lists and dictionaries. 
    result = 'H' if test_num > 0.5 else 'T'
    return result

def roll_die():
    '''
    Input:  None
    Output: Int - Between 1 and 6

    Using random.randint(), perform a die roll and return the number that "comes up".
    '''
    return random.randint(1, 6)

def flip_coin_roll_die(n_times):
    '''
    Input:  Int - number of times to flip a coin and roll a die
    Output: List - of tuples with the outcomes 
       of the flips and rolls from each time
    '''
    # We mentioned why we use the `_` in scenarios like this in the `part1.py` solutions
    # file ... do you remember why?
    return [(flip_coin(), roll_die()) for _ in range(n_times)]
