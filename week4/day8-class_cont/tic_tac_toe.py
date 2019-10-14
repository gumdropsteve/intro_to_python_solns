class Board():
    """This docstring will describe how to interact with the tic-tac-toe
    Board class.

    This class will keep track of the state of a tic-tac-toe board as
    players interact with the game. It will have methods for initializing
    the board, checking whether or not certain spots are already filled,
    filling a spot when a player plays on it, and printing the board
    so that we can vizualize what it looks like.

    Attributes:
    ----------
    board: List of lists
        This will hold the current state of the board - i.e. what each player
        has played, and where.
    board_size: int
        This holds the number of rows and number of columns in the board (its
        square, so this is the same number).
    """

    def __init__(self, board_size):
        self.board_size = board_size
        self._initialize_board()

    def _initialize_board(self):
        """
        Input:  None
        Output: board_size * board_size list of lists with the coordinate
                location in each position
        """

        self.board = [[(i, j) for i in range(self.board_size)]
                      for j in range(self.board_size)]

    def _check_coord(self, coord):
        """
        Input:  tuple
        Output: bool

        Check whether the board spot that the player wants to fill
        is a valid spot, and whether or not it is already filled.
        """

        x, y = int(coord[0]), int(coord[1])
        if x > self.board_size -1 or x < 0  or \
           y > self.board_size - 1 or y < 0:
            print('Illegal coordinate. Try again')
            return (False,)
        if self.board[y][x] in [' X ', ' O ']:
            print('That square has already been played in. Try again.')
            return (False,)
        return x, y, True

    def fill_coord(self, game_check, coord, player_symbol):
        """
        Input:  bool, tuple, str
        Output: bool

        Check whether the inputted coorinate is okay (with self._check_coord),
        and then fill that coordinate on the board with the inputted player
        symbol. Output a True of False on whether the board was filled at the
        inputted coord.
        """
        pass

    def check_winner(self, player_symbol):
        """
        Input: str

        Check if there is a winner in the game.
        """
        for i in range(self.board_size):
            if all([j == player_symbol for j in self.board[i]]):
                return True
        for i in range(self.board_size):
            if all([self.board[j][i] == player_symbol for j in range(self.board_size)]):
                return True
        if all([self.board[i][i] == player_symbol for i in range(self.board_size)]):
            return True
        if all([self.board[i][self.board_size-1-i] == player_symbol
                for i in range(self.board_size)]):
            return True
        return False

    def __repr__(self):
        """
        Print the board in a pretty format.
        """
        pass

class Player():
    """This docstring will describe the player class and how to interact
    with it.

    Each player will have three attributes, and then methods for actually
    playing a game of tic-tac-toe.

    Attributes:
    ----------
    name: str
        Holds the name of the player.
    symbol: str
        Holds the symbol that the player will use (either ' X ' or ' O ').
    num_wins: int
        Holds the number of wins a player has.
    """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.num_wins = 0

    def __repr__(self):
        return self.name

class Game():
    """This docstring will describe how to interact with the Game class.

    Each game class will be initialized by prompting for two Players, each
    of which require a name and symbol. It will then prompt for what size
    board they want to play from, and initialize that board. From there,
    it will go ahead and allow the players to play the game, allowing them
    to specify where they want to make their moves. The game class will perform
    some basic checks to make sure that the players enter valid moves, and then
    the board object is built in such a way that it will perform some additional
    checks.

    Attributes:
    ----------
    players: list
        This will hold the Players that are playing the game.
    board: Board object
        This will be the board that the Players are playing on.
    round: int
        This will hold the round of the game that the Players are on.
    """

    def __init__(self):
        print("Let's play some tic-tac-toe!")
        self._initialize_board()
        self._initialize_players()
        self.round = 1
        self.turn = 0
        print(self.board)
        self._play_game()

    def _initialize_players(self):
        """Prompt for two players, asking for names."""
        pass

    def _initialize_board(self):
       """Initialize Board, prompting players for board size."""

       board_size = int(input("What size board would you like to play on today? "))
       self.board = Board(board_size)

    def _play_game(self):
        """Play the game, prompting players for moves."""
        for turn in range(self.board.board_size ** 2):
            winner, player = self._play_turn()
            print(self.board)
            if winner:
                print('{} wins!!'.format(player))
                player.num_wins += 1
                break
        else:
            print('Game resulted in a tie... like usual.')

        play_again = input('Play again? Enter y/n.').lower()
        if play_again == 'y':
            self._reinitialize()
        else:
            print('{} won {} times, {} won {} times'.format(self.players[0],
                    self.players[0].num_wins, self.players[1],
                    self.players[1].num_wins))
            print('Thanks for playing!')


    def _play_turn(self):
        """Play a single turn."""
        player_idx = self.turn % 2
        player = self.players[player_idx]
        while True:
            res = self._get_good_coord(player)
            if res:
                break
        winner = self.board.check_winner(player.symbol)
        self.turn += 1
        return winner, player

    def _get_good_coord(self, player):
        """Prompt the current player for coordinate to play."""
        pass

    def _check_coord(self, coord):
        '''
        Input:  Tuple, List of Lists
        Output: Bool

        Checks whether or not inputted "coordinates" are well formatted and legal.
        '''
        pass

    def _reinitialize(self):
        """Reinitialize the game in order to play again."""
        pass

if __name__ == '__main__':
    game = Game()
