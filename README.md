1. IMPLEMENTATION DETAILS:
   - Board Representation: A 1D list of 9 elements where None represents an 
     empty cell, 'X' represents the AI (Maximizer), and 'O' represents the 
     Human (Minimizer).
   - Core Algorithm: Minimax algorithm reinforced with Alpha-Beta pruning to 
     cut off unpromising branches early.
   - Design Strategy: Monolithic single-file structure optimized for live 
     demonstrations and defense evaluations without file-switching friction.

2. RESULTS & PERFORMANCE ANALYSIS:
   - Correctness: The AI is unbeatable. It perfectly blocks winning threats.
   - Pruning Efficiency: Alpha-Beta pruning drastically reduces the search 
     space. For instance, on the very first turn of the AI after the human has started with 1 i.e left top:
       * Pure Minimax explores: 59,704 nodes
       * Alpha-Beta Pruning explores: 4089 nodes
     This represents a ~93% reduction in state evaluations, proving the 
     efficiency of the mathematical cutoffs (alpha >= beta).
   - I've also added an extra layer of code that further increases the efficiency of the algorithm in the best_move function
     we check if we've found the maximun result i.e 1 then stop the search for the best move after then.