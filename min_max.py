from math import inf

WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

# Global counter to track node evaluations
node_counter = 0

# Global cache for Memoization (Transposition Table)
transposition_table = {}

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
        if board[a] is not None and board[a] == board[b] == board[c]:
            return 1 if board[a] == "X" else -1

    if None not in board:
        return 0

    return None

def legal_moves(board):
    return [i for i, cell in enumerate(board) if cell is None]

def min_max(board, max_player, alpha, beta, use_pruning=True, use_memo=False):
    global node_counter

    board_tuple = tuple(board)
    if use_memo and board_tuple in transposition_table:
        return transposition_table[board_tuple]

    node_counter += 1

    terminal_score = evaluate(board)
    if terminal_score is not None:
        return terminal_score

    if max_player:
        best_val = -inf
        pruned = False  
        
        for move in legal_moves(board):
            board[move] = "X"
            val = min_max(board, False, alpha, beta, use_pruning, use_memo)
            board[move] = None

            best_val = max(best_val, val)
            alpha = max(alpha, best_val)

            if use_pruning and alpha >= beta:
                pruned = True 
                break
        

        if use_memo and not pruned:
            transposition_table[board_tuple] = best_val
        return best_val
        
    else:
        best_val = inf
        pruned = False  
        
        for move in legal_moves(board):
            board[move] = "O"
            val = min_max(board, True, alpha, beta, use_pruning, use_memo)
            board[move] = None

            best_val = min(best_val, val)
            beta = min(beta, best_val)

            if use_pruning and beta <= alpha:
                pruned = True 
                break

        if use_memo and not pruned:
            transposition_table[board_tuple] = best_val
        return best_val


def best_move(board):
    global node_counter

    # 1. WITHOUT Pruning
    node_counter = 0
    for move in legal_moves(board):
        board[move] = "X"
        _ = min_max(board, False, -inf, inf, use_pruning=False, use_memo=False)
        board[move] = None
    nodes_without_pruning = node_counter

    # 2. WITH Pruning (BUT NO BREAK AT ROOT)
    node_counter = 0
    for move in legal_moves(board):
        board[move] = "X"
        _ = min_max(board, False, -inf, inf, use_pruning=True, use_memo=False)
        board[move] = None
    nodes_with_pruning_no_break = node_counter

    # 3. WITH Pruning AND BREAK AT ROOT
    node_counter = 0
    best_score_temp = -inf
    for move in legal_moves(board):
        board[move] = "X"
        score = min_max(board, False, -inf, inf, use_pruning=True, use_memo=False)
        board[move] = None
        if score > best_score_temp:
            best_score_temp = score
            if score == 1:  
                break
    nodes_with_pruning_and_break = node_counter

    # 4. WITH Pruning + ROOT BREAK + MEMOIZATION
    node_counter = 0
    best_score = -inf
    best_index = None
    for move in legal_moves(board):
        board[move] = "X"
        score = min_max(board, False, -inf, inf, use_pruning=True, use_memo=True)
        board[move] = None
        
        if score > best_score:
            best_score = score
            best_index = move
            if score == 1:
                break
    nodes_with_memo = node_counter

    return (
        best_index,
        best_score,
        nodes_with_pruning_no_break,
        nodes_with_pruning_and_break,
        nodes_without_pruning,
        nodes_with_memo
    )


# =========================
# INPUT HANDLING
# =========================

def get_human_move(board):
    while True:
        try:
            chosen = int(input("\nChoose a position (1-9): "))
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
            board[move] = "O"
            human_turn = False
        else:
            print("\nComputer is thinking...")
            move, score, p_no_break, p_break, no_pruning, memo_nodes = best_move(board)
            board[move] = "X"

            print(f"--- Node Comparison ---")
            print(f"Brute Force (No Pruning):    {no_pruning}")
            print(f"Alpha-Beta (No Root Break):  {p_no_break}")
            print(f"Alpha-Beta + Root Break:     {p_break}")
            print(f"Alpha-Beta + Break + Memo:   {memo_nodes}")
            print(f"-----------------------")

            human_turn = True


if __name__ == "__main__":
    main()