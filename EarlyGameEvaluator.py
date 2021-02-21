from OthelloEvaluator import OthelloEvaluator
import time



class EarlyGameEvalutor(OthelloEvaluator):
    """
    Class to represent a evaluator used by a Minimax algorithm. 

    Author: dv18mln
    """
    
    def evaluate(self, othello_position, timeout):
        """
        Evaluation function only used in the early part of the game. 
        The functions values the inner 4x4 matrix highly, when matrix 
        is full the evaluation function is replaced. Filling the middle
        in the beginning can yield in great mobility in later parts of
        the game. 
        :param othello_position: Position to evaluate.
        :param timeout: Set timeout for the algortihm to exit.
        """

        tile_score = [
            [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
            [0, 120, -50,  -5,  -5,  -5,  -5, -50, 120,   0],
            [0, -50, -50,  -5,  -5,  -5,  -5, -50, -50,   0],
            [0,  -5,  -5,  10,   5,   5,  10,  -5,  -5,   0],
            [0,  -5,  -5,   5,   5,   5,   5,  -5,  -5,   0],
            [0,  -5,  -5,   5,   5,   5,   5,  -5,  -5,   0],
            [0,  -5,  -5,  10,   5,   5,  10,  -5,  -5,   0],
            [0, -50, -50,  -5,  -5,  -5,  -5, -50, -50,   0],
            [0, 120, -50,  -5,  -5,  -5,  -5, -50, 120,   0],
            [0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
        ]


        W_score = 0
        B_score = 0
        E = 0
        W_markers = 0
        B_markers = 0


        for i in range(1,9):
            if time.time() >= timeout:
                return None
            for j in range(1,9):
                
                if othello_position.board[i][j] == 'W':
                   W_score += tile_score[i][j]
                   W_markers += 1
                
                elif othello_position.board[i][j] == 'B':
                    B_score += tile_score[i][j]
                    B_markers += 1

                else:
                    E += 1

        if W_markers > 5 and B_markers > 5:
            W_score -= W_markers
            B_score -= B_markers

        if W_markers <= 3:
            W_score += 2 * W_markers
        if B_markers <= 3:
            B_score += 2 * B_markers


        if othello_position.to_move():
            return W_score
        else:
            return -B_score
