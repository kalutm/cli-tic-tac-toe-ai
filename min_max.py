from math import inf

def main():
    game_state = [None] * 9
    human_turn = True
    print(f"{visualize_board(game_state)}")
    while True:
        result = evaluate(game_state)
        if result is not None:
            print(who_won(result))
            break
        if human_turn:
            available_positions = ""
            for index in legal_moves(game_state):
                available_positions = available_positions + f" {index + 1}"
            chosen = int(input(f"Your turn, which position will you play?: {available_positions}\n"))
            # to make things easier assume human is always 'O';
            game_state[chosen - 1] = 'O'
            human_turn = False
        else:
            best_index, best_score = best_move(game_state)
            # consequently assume computer is always 'X'
            game_state[best_index] = 'X'
            human_turn = True
        print(f"{visualize_board(game_state)}\n")

def who_won(integer):
    return "Computer Won" if integer == 1 else "You Won" if integer == -1 else "Draw"

def visualize_board(board):
    """
    Takes a 1D list of 9 elements and returns a beautifully formatted 
    string representation of the Tic-Tac-Toe board.
    """
    # Replace None or empty spaces with a single space ' ' for perfect alignment
    display_cells = [str(cell) if cell in ['X', 'O'] else ' ' for cell in board]
    
    # Construct the grid string
    board_string = (
        f" {display_cells[0]} | {display_cells[1]} | {display_cells[2]} \n"
        f"---+---+---\n"
        f" {display_cells[3]} | {display_cells[4]} | {display_cells[5]} \n"
        f"---+---+---\n"
        f" {display_cells[6]} | {display_cells[7]} | {display_cells[8]} "
    )
    
    return board_string


WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

def evaluate(board):
    """
    Returns:
        1  -> X wins
        -1 -> O wins
         0 -> draw
         None -> game is still ongoing
    """
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return 1 if board[a] == "X" else -1

    if None not in board:
        return 0

    return None

def legal_moves(board):
    return [i for i, cell in enumerate(board) if cell is None]

def min_max(board, max_player, alpha=-inf, beta=inf):
    terminal_score = evaluate(board)
    if terminal_score is not None:
        return terminal_score

    if max_player:
        best_val = -inf

        for index in legal_moves(board):
            board[index] = "X"   # apply move

            val = min_max(board, False, alpha, beta)

            board[index] = None  # undo move

            best_val = max(best_val, val)
            alpha = max(alpha, best_val)

            if alpha >= beta:
                break

        return best_val

    else:
        best_val = inf

        for index in legal_moves(board):
            board[index] = "O"   # apply move

            val = min_max(board, True, alpha, beta)

            board[index] = None  # undo move

            best_val = min(best_val, val)
            beta = min(beta, best_val)

            if beta <= alpha:
                break

        return best_val

def best_move(board):
    """
    Returns (best_index, best_score) for MAX = X.
    """
    best_score = -inf
    best_index = None

    for index in legal_moves(board):
        board[index] = "X"
        score = min_max(board, False, -inf, inf)
        board[index] = None

        if score > best_score:
            best_score = score
            best_index = index

    return best_index, best_score

if __name__ == '__main__':
    main()