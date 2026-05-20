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
       * Alpha-Beta + Root Break + Memoization: Plummets the search space down to roughly ~1,396 nodes. Because the Transposition Table cache persists across the entire game, subsequent turns often drop to single-digit node evaluations as the AI relies on its pre-calculated history.