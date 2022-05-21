"""
Tic Tac Toe Player

video starts @ 1:11:46

"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # isolate columns
    col1 = [board[0][0],board[1][0],board[2][0]]
    col2 = [board[0][1],board[1][1],board[2][1]]
    col3 = [board[0][2],board[1][2],board[2][2]]
    
    # isolate rows
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]

    # isolate diagnols
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[2][0], board[1][1], board[0][2]]

    # put all possible checks in a list
    checks = [col1, col2, col3, row1, row2, row3, diag1, diag2]

    # loop through checks in search of possible goal state
    for check in checks:
        # isolate spaces on board
        space1 = check[0]
        space2 = check[1]
        space3 = check[2]

        # update winner, end loop if found
        winner = (space1 == space2 == space3) and (space1 != EMPTY and space2 != EMPTY and space3 != EMPTY)
        if winner:
            break

    return winner


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
