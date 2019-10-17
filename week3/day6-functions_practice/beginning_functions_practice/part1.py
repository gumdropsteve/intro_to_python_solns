# This is the code broken apart for question 1.

def book_update(book, library, new_books):
    '''
    Input: Str - book name,
           Set - book strings,
           List - Previously unknown books
    Helper function to update library with potenially unknown book.
    '''
    if book not in library:
        print('The book, {}, is new!'.format(book))
        new_books.append(book)
    library.add(book)

def update_library(books, library):
    '''
    Input:  List - book names, Set - books already in library
    Output: List - books that weren't in the library
    '''
    new_books = []
    for book in books:
        book_update(book, library, new_books)
    print(library)
    return new_books

# This is the code broken apart for question 2.

def print_winner(player_1, player_2):
    '''
    Input:  Str, Str
    Helper function to determine and print winner of RPS.
    '''
    if player_1 == player_2:
        print("It's a tie!")
    elif player_1 == 'r' and player_2 == 's':
        print('Player 1 wins!')
    elif player_1 == 'r' and player_2 == 'p':
        print('Player 2 wins!')
    elif player_1 == 'p' and player_2 == 'r':
        print('Player 1 wins!')
    elif player_1 == 'p' and player_2 == 's':
        print('Player 2 wins!')
    elif player_1 == 's' and player_2 == 'r':
        print('Player 2 wins!')
    elif player_1 == 's' and player_2 == 'p':
        print('Player 1 wins!')
    else:
        # Note that we put this last else statment here as a catch all.
        # While no other scenario than those above should ever theoretically
        # happen, we don't want our function to not print anything in the case
        # that there wasn't a valid set of plays. Instead, we want to actually
        # give the caller of our function some useful information, which is why we
        # put this print statement here.
        print("Someone didn't play right!")

def play_rock_paper_scissors(n_rounds):
    '''
    Input:  Int - number of rounds to play rock paper scissors for
    '''
    for _ in range(n_rounds):
        player_1 = raw_input('Player 1 play (r/p/s): ')
        player_2 = raw_input('Player 2 play (r/p/s): ')
        print_winner(player_1, player_2)

# This is the code broken apart for question 3.

def find_line(f, line_num):
    '''
    Input:  File object, Int
    Output: Str - line of file
    '''
    for i, file_line in enumerate(f, 1):
        if i == line_num:
            return file_line.strip()

def repeat_list_of_file_line(file_name, line_num, num_copies):
    '''
    Input:  Str - path to file,
            Int - number of line to copy from file,
            Int - number of times to copy line into list
    Output: List - filled with num_copies of line_num in file_name
    '''
    with open(file_name) as f:
        line = find_line(f, line_num)
    if not line:
        copies_of_line = 'There were not {} lines in the document'.format(line_num)
    else:
        # Note that the `_` character in the line below is used just to denote that
        # we aren't doing anything with the numbers that are being created in the
        # range call (e.g. we're storing each number from the `range(num_copies)`
        # call in `_`, but then not using that at all). The `_` is a special way to
        # explicitly note that we're not doing anything with what's coming out of the range.
        copies_of_line = [line for _ in range(num_copies)]
    return copies_of_line

# This is the code broken apart for question 4.

import this

def decode_from_dict(decoder, coded_text):
    decoded_chars = []
    for char in coded_text:
        if char.isalpha():
            decoded_chars.append(decoder[char])
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)

def decode_zen_of_python():
    zen_decoder = this.d
    coded_zen = this.s
    print(coded_zen)
    decoded_zen = decode_from_dict(zen_decoder, coded_zen)
    print('\n' + decoded_zen)
