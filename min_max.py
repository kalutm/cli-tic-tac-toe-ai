from math import inf

WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

# =========================
# UI HELPERS
# =========================

def clear_spacing():
    print("\n" * 2)

def intro():
    print("=" * 35)
    print("      TIC TAC TOE")
    print("=" * 35)
    print("You are O")
    print("Computer is X")
    print("\nBoard positions:\n")

    demo = [str(i) for i in range(1, 10)]
    print(visualize_board(demo))
    print()

def visualize_board(board):

    display = []

    for i, cell in enumerate(board):
        if cell is None:
            display.append(str(i + 1))
        else:
            display.append(cell)

    return (
        f" {display[0]} │ {display[1]} │ {display[2]} \n"
        f"───┼───┼───\n"
        f" {display[3]} │ {display[4]} │ {display[5]} \n"
        f"───┼───┼───\n"
        f" {display[6]} │ {display[7]} │ {display[8]} "
    )

def who_won(score):
    if score == 1:
        return "Computer Won!"
    elif score == -1:
        return "You Won!"
    return "Draw!"

# =========================
# GAME LOGIC
# =========================

def evaluate(board):

    for a, b, c in WINNING_COMBINATIONS:

        if (
            board[a] is not None
            and board[a] == board[b] == board[c]
        ):
            return 1 if board[a] == 'X' else -1

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

        for move in legal_moves(board):

            board[move] = 'X'

            val = min_max(board, False, alpha, beta)

            board[move] = None

            best_val = max(best_val, val)

            alpha = max(alpha, best_val)

            if alpha >= beta:
                break

        return best_val

    else:

        best_val = inf

        for move in legal_moves(board):

            board[move] = 'O'

            val = min_max(board, True, alpha, beta)

            board[move] = None

            best_val = min(best_val, val)

            beta = min(beta, best_val)

            if beta <= alpha:
                break

        return best_val

def best_move(board):

    best_score = -inf
    best_index = None

    for move in legal_moves(board):

        board[move] = 'X'

        score = min_max(board, False, -inf, inf)

        board[move] = None

        if score > best_score:
            best_score = score
            best_index = move

            # already found a potential winner move so terminate the search
            if best_score == 1:
                break

    return best_index, best_score

# =========================
# INPUT HANDLING
# =========================

def get_human_move(board):

    while True:

        try:

            chosen = int(
                input("\nChoose a position (1-9): ")
            )

            if chosen < 1 or chosen > 9:
                print("Position must be between 1 and 9.")
                continue

            index = chosen - 1

            if board[index] is not None:
                print("That position is already occupied.")
                continue

            return index

        except ValueError:
            print("Please enter a valid number.")

# =========================
# MAIN GAME LOOP
# =========================

def main():

    intro()

    board = [None] * 9

    human_turn = True

    while True:

        clear_spacing()

        print(visualize_board(board))

        result = evaluate(board)

        if result is not None:
            print(f"\n{who_won(result)}")
            break

        if human_turn:

            move = get_human_move(board)

            board[move] = 'O'

        else:

            print("\nComputer is thinking...")

            move, score = best_move(board)

            board[move] = 'X'

            print(f"Computer chose position {move + 1}")

        human_turn = not human_turn

if __name__ == '__main__':
    main()