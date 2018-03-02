from random import randint


# Function to display the board
def display_board(board):
    '''
    Display the current board
    Args: `board` -> List of values in current board
    '''
    # Clear the output
    print('\n' * 50)
    print('{}|{}|{}'.format(board[7], board[8], board[9]))
    print('{}|{}|{}'.format(board[4], board[5], board[6]))
    print('{}|{}|{}'.format(board[1], board[2], board[3]))


# Function to take in player input
def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    return ('O', 'X')


# Function to place marker on board
def place_marker(board, marker, position):
    '''
    Function that takes in the board list object, a marker ('X' or 'O') and a
    desired position (1-9) and assigns it to board
    '''
    board[position] = marker


# Function to check if a player has won
def win_check(board, mark):
    '''
    Function that takes in a board and a mark (X or O) and checks if that mark
    has won
    '''
    rows = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    cols = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    diag = [(1, 5, 9), (3, 5, 7)]

    # Check if all rows have same marker
    for i, j, k in rows:
        if board[i] == board[j] == board[k] == mark:
            print('Mark {} has won!'.format(mark))
            return True

    # Check if all cols have same marker
    for i, j, k in cols:
        if board[i] == board[j] == board[k] == mark:
            print('Mark {} has won!'.format(mark))
            return True

    # Check if all diagonals have same marker
    for i, j, k in diag:
        if board[i] == board[j] == board[k] == mark:
            print('Mark {} has won!'.format(mark))
            return True

    return False


# Function to select which player goes first
def choose_first():
    '''
    Function to randomly choose which player goes first
    '''
    flip = randint(0, 1)
    if flip:
        return 'Player 1'
    return 'Player 2'


# Function to check if a space is freely available on board
def space_check(board, position):
    '''
    Function to check if space is freely available on board
    '''
    return board[position] == ' '


# Function to check if board is full
def is_board_full(board):
    '''
    Function to check if the board is full
    '''
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Function that asks for player's next position
def player_choice(board):
    '''
    Function that asks for a player's next position (1-9) and space_check() to
    see if it's free
    '''
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position


# Function to check if a player wants to play again
def replay():
    choice = input('Play again? Enter Yes or No: ')
    return choice.lower() == 'yes'
