# practice code to try to implement min max algorithm my self
from math import inf

board = [None] * 9

def min_max(board, depth, max_player, alpha, beta):
    # base case
    if depth == 0:
        return eval_function(board)

    if max_player:
        best_val = -inf

        for index in legal_moves(board):
            apply_move(index, True)
            val = min_max(board, depth - 1, False, alpha, beta)

            best_val = max(best_val, val)
            alpha = max(alpha, best_val)

            if alpha >= beta:
                break

        return best_val
    
    else:
        best_val = +inf

        for index in legal_moves():
            apply_move(index, False)
            val = min_max(board, depth - 1, True, alpha, beta)

            best_val = min(best_val, val)
            beta = min(beta, best_val)

            if beta <= alpha:
                break
        return best_val

def eval_function(board):
    """
    Determines the result of a Tic-Tac-Toe game.
    Input: A list of 9 elements (e.g., ["X", "O", "X", None, "X", "O", None, None, None])
    Returns: 1 (X wins), -1 (O wins), 0 (draw)
    """
    # All possible winning combinations of indices
    winning_combinations = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]
    
    # 1. Check for a winner
    for combo in winning_combinations:
        a, b, c = combo
        # Ensure the cell is not empty and all three match
        if board[a] in ['X', 'O'] and board[a] == board[b] == board[c]:
            if board[a] == 'X': return 1 
            if board[a] == 'O': return -1
            
    # 2. Check for a draw (no None left)
    if None not in board:
        return 0

def legal_moves(board):
    open_indexes = []
    for i in range(len(board)):
        if board[i] is not None:
            open_indexes.append(i)
    return open_indexes

def apply_move(board, index, max_player):
    if max_player:
        board[index] = 'X'
    else:
        board[index] = 'O'