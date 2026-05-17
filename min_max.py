# practice code to try to implement min max algorithm my self

from math import inf
from state import State
def min_max(state: State, depth, max_player, alpha, beta):
    # base case
    if depth == 0:
        return eval_function(state)

    if max_player:
        best_val = -inf

        for move in legal_moves(state):
            child = apply_move(state, move)
            val = min_max(child, depth - 1, False, alpha, beta)

            best_val = max(best_val, val)
            alpha = max(alpha, best_val)

            if alpha >= beta:
                break

        return best_val
    
    else:
        best_val = +inf

        for move in legal_moves(state):
            child = apply_move(state, move)
            val = min_max(child, depth - 1, True, alpha, beta)

            best_val = min(best_val, val)
            beta = min(beta, best_val)

            if beta <= alpha:
                break
        return best_val

def eval_function(state: State):
    return state.knight - state.orc

def legal_moves(state: State):
    pass

def apply_move():
    pass