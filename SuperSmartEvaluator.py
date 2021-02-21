from OthelloEvaluator import OthelloEvaluator
import time


class SuperSmartEvaluator(OthelloEvaluator):
    """
    Class to represent a evaluator used by a Minimax algorithm. 

    Author: dv18mln
    """
    

    def evaluate(self, othello_position, timeout):
        """
        The rules and strategies to play the game it taken from this website:
        https://www.ultraboardgames.com/othello/tips.php

        There are alot of strategies to apply to be a good othello player, the evaluation function
        implements three of these techniques.

        1. Aim for corners (and squares close to them), disks placed in the corner cannot be flipped.
        2. Disc Minimization, the one with the lowst number of tiles are often in the lead.
        3. Danger zones: 10 (2,2), 11 (2,3), 18 (3,2), 19 (3,3), 21 (3,5), 29 (4,5), 30 (4, 6), 31 (4, 7), 35 (5, 3), 38 (5,6), 39 (5,7), 42 (6,2), 43 (6,3), 44 (6,4)
        5. Stay in the center

        From this, weight for each tile can be derived. Example for row 1 is as follows:


        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        ---|---|---|---|---|---|---|---|---|---
        1 |120|-20|20 | 5 | 5 |20 |-20|120| 1
        ---|---|---|---|---|---|---|---|---|---
        2 |   |   |   |   |   |   |   |   | 2
        ---|---|---|---|---|---|---|---|---|---
        3 |   |   |   |   |   |   |   |   | 3
        ---|---|---|---|---|---|---|---|---|---
        4 |   |   |   | 0 | X |   |   |   | 4
        ---|---|---|---|---|---|---|---|---|---
        5 |   |   |   | X | 0 |   |   |   | 5
        ---|---|---|---|---|---|---|---|---|---
        6 |   |   |   |   |   |   |   |   | 6
        ---|---|---|---|---|---|---|---|---|---
        7 |   |   |   |   |   |   |   |   | 7
        ---|---|---|---|---|---|---|---|---|---
        8 |   |   |   |   |   |   |   |   | 8
        ---|---|---|---|---|---|---|---|---|---
        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |


        This function is used in a later part of the game, 
        when the inner 4x4 matrix is full.

        :param othello_position: Position to evaluate.
        :param timeout: Set timeout for the algortihm to exit.
        """

        tile_score = [
            [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
            [0, 120, -20,  20,   5,   5,  20, -20, 120,   0],
            [0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0],
            [0,  20,  -5,   5,   3,   3,   5,  -5,  20,   0],
            [0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0],
            [0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0],
            [0,  20,  -5,   5,   3,   3,   5,  -5,  20,   0],
            [0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0],
            [0, 120, -20,  20,   5,   5,  20, -20, 120,   0],
            [0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
        ]

        B_score = 0
        B_markers = 0
        W_score = 0
        W_markers = 0
        E = 0

        for i in range(1,9):
            if time.time() >= timeout:
                return None
            for j in range(1,9):
                
                # Aim for corners
                if othello_position.board[i][j] == 'W':
                    
                    W_score += tile_score[i][j]
                   
                    if i > 4:
                        W_score += (8 - i)
                    if i < 4:
                        W_score += i
                    if j > 4:
                        W_score += (8 - j)
                    if j < 4:
                        W_score += j
                            
                    W_markers += 1

                if othello_position.board[i][j] == 'B':
                    
                    B_score += tile_score[i][j]
                    
                    if i > 4:
                        B_score += (8 - i)
                    if i < 4:
                        B_score += i
                    if j > 4:
                        B_score += (8 - j)
                    if j < 4:
                        B_score += j

                    B_markers += 1

                else:
                    
                    if i >= 3 and i <= 6 and j >= 3 and j <= 6:
                        W_score -= 5
                        B_score -= 5

                    E += 1

        if E < 15:
                W_score += W_markers
                B_score += B_markers
        else: 
            W_score -= W_markers
            B_score -= B_markers

        if W_markers <= 3:
            W_score += 2 * W_markers
        if B_markers <= 3:
            B_score += 2 * B_markers

        # Max - Min
        if othello_position.to_move():
            return W_score
        else:
            return -B_score
        
