1. IMPLEMENTATION DETAILS:
   - Board Representation: A 1D list of 9 elements where `None` represents an empty cell, 'X' represents the AI (Maximizer), and 'O' represents the Human (Minimizer).
   - Core Algorithm: Minimax algorithm reinforced with Alpha-Beta pruning to cut off unpromising branches early.
   - Advanced Optimization: Transposition Table (Memoization) caches previously evaluated board states, exploiting the deterministic nature of the game to instantly recall results for identical sub-trees.
   - Design Strategy: Monolithic single-file structure optimized for live demonstrations and defense evaluations without file-switching friction.

2. RESULTS & PERFORMANCE ANALYSIS:
   - Correctness: The AI is unbeatable. It perfectly blocks winning threats and forces draws or wins.
   - Efficiency Progression: The node evaluation counts demonstrate massive exponential improvements at each optimization layer. For example, on the AI's first turn (after the human opens in the top-left position 1):
       * Pure Minimax explores: ~59,704 nodes
       * Alpha-Beta Pruning explores: ~4,089 nodes (a ~93% reduction, proving the efficiency of mathematical cutoffs where alpha >= beta).
       * Alpha-Beta + Root Break: Introduces an early exit condition in the root `best_move` loop. If a guaranteed winning move (score of 1) is found, the loop breaks instantly, optimizing late-game evaluations.
       * Alpha-Beta + Root Break + Memoization: Optimizes the search further. Because the Transposition Table cache persists across the entire game, subsequent turns often drop to single-digit node evaluations as the AI relies on its pre-calculated history.
3. COMPLEXITY ANALYSIS:
   - Asymptotic Complexity: O(1) (Constant Time). Because the Tic-Tac-Toe grid is strictly constrained to a 3x3 layout, the input size 'n' is fixed, capping the absolute maximum upper bound of calculations.
   - Algorithmic Tree Complexity (Worst-Case): O(b^d), where 'b' is the branching factor and 'd' is the depth. Unoptimized Minimax must explore the entire game tree up to a maximum of 9! (362,880) state permutations.
   - Optimized Alpha-Beta Complexity (Best-Case): O(b^(d/2)). When move ordering allows optimal cutoffs, alpha-beta pruning effectively cuts the exponent of the search depth in half.
   - Memoization Impact: Reduces redundant sub-tree evaluations to O(V), where 'V' is the number of unique valid board states (only 5,827 in Tic-Tac-Toe), converting an exponential search path into a highly optimized, flat lookup table.