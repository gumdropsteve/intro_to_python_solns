player_dict = {1: ' X ', 2: ' O '}


def display_starting_message():
    '''
    Displays message for how to interact with this game of tic-tac-toe.
    '''
    starting_message = 'This game of tic-tac-toe will prompt players \nfor coordinates to make their play in the \nformat x, y. When a player wins, it will be \ndeclared, and if no player emerges the victor a \ntie will be declared. Time to play tic-tac-toe!'
    print(starting_message)


def initialize_board():
    '''
    Input:  None
    Output: 3 x 3 list of lists with the coordinate location in each position
    '''
    return [[(i, j) for i in range(3)] for j in range(3)]


def print_board(board):
    '''
    Input:  List of Lists
    Output: None
    '''
    for row in board:
        print(row)


def get_check_coord(coord, board):
    '''
    Input:  Tuple, List of Lists
    Output: Bool

    Checks whether or not inputted "coordinates" are well formatted and legal.
    '''
    if len(coord) != 2:
        print('You need to enter two coordinates. Try again.')
        return (False,)
    x, y = coord
    if x.isdigit() and y.isdigit():
        x, y = int(x), int(y)
    else:
        print('Please enter numbers for coordinates. Try again.')
        return (False,)
    if x > 2 or x < 0 or y > 2 or y < 0:
        print('Illegal coordinate. Try again')
        return (False,)
    if board[y][x] in [' X ', ' O ']:
        print('That square has already been played in. Try again.')
        return (False,)
    return x, y, True


def get_good_coord(player, board):
    '''
    Input:  Int, List of Lists
    Output: Int, Int
    '''
    while True:
        play_prompt = 'Player {} ({}), where will you play? '
        coord = tuple(input(play_prompt.format(player, player_dict[player])).split(', '))
        stuff = get_check_coord(coord, board)
        if stuff[-1]:
            break
    return stuff[0], stuff[1]


def check_winner(board, player):
    '''
    Input:  List of Lists, Int
    Output: Bool

    Returns True if player has three in a row on the board, otherwise False.
    '''
    piece = player_dict[player]
    for i in range(3):
        if all([j == piece for j in board[i]]):
            return True
    for i in range(3):
        if all([board[j][i] == piece for j in range(3)]):
            return True
    if all([board[i][i] == piece for i in range(3)]):
        return True
    if all([board[i][2-i] == piece for i in range(3)]):
        return True
    return False


def play_turn(turn, board):
    '''
    Input:  Int, List of Lists
    Output: Int, Bool

    Prompts next player for play. Checks if play made three in a row.
    If it does that player is declared the winner.
    '''
    player = turn % 2 + 1
    x, y = get_good_coord(player, board)
    board[y][x] = player_dict[player]
    winner = check_winner(board, player)
    return winner, player


def play_tic_tac_toe():
    '''
    Function that allows two players to play tic-tac-toe against one another.
    '''
    display_starting_message()
    board = initialize_board()
    print_board(board)
    for turn in range(9):
        winner, player = play_turn(turn, board)
        print_board(board)
        if winner:
            print('Player {} Wins!!'.format(player))
            break
    else:
        print('Game resulted in a tie...like usual.')


if __name__ == '__main__':
    play_tic_tac_toe()
