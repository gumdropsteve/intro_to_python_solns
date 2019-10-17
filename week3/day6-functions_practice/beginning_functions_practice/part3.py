# This is how we would use our own functions that we have written - store
# them in a module (a `.py` file), and then import them.
from part2 import roll_die

def model_player_rolls(num_die):
    '''
    Input:  Int - number of times to roll a die
    Output: Int - Sum of nums 1 - 6 for modeled die rolls
    '''
    return sum(roll_die() for _ in range(num_die))

def model_dice_rolls(player1_die, player2_die):
    '''
    Input:  Int - number of die for player 1,
            Int - number of die for player 2
    Output: Tuple - (Int, Int): sum of rolls for player 1
            and player 2 respectively
    '''
    player1_rolls_sum = model_player_rolls(player1_die)
    player2_rolls_sum = model_player_rolls(player2_die)
    if player1_rolls_sum > player2_rolls_sum:
        print('Player 1 wins!')
    elif player1_rolls_sum < player2_rolls_sum:
        print('Player 2 wins!')
    else:
        print('There was a tie!')
    return player1_rolls_sum, player2_rolls_sum

# This is the answer for question 2.
def percentage_amount(total, percentage):
    '''
    Input:  Float, Float
    Output: Float
    '''
    return total * percentage

def calc_total_bill(charge_amount, tax_rate, tip_percentage):
    '''
    Input:  Numeric, Float, Float
    Output: Float
    '''
    bill_with_tax = charge_amount + percentage_amount(charge_amount, tax_rate)
    bill_with_tip = bill_with_tax + percentage_amount(bill_with_tax, tip_percentage)
    return bill_with_tax, bill_with_tip
