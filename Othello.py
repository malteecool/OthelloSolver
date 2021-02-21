from OthelloAlgorithm import OthelloAlgorithm
from SuperSmartEvaluator import SuperSmartEvaluator
from EarlyGameEvaluator import EarlyGameEvalutor
from OthelloPosition import OthelloPosition
from OthelloAction import OthelloAction
import sys
import time


def print_action():
    """
    Prints the best found move within the given time period.
    """
    global move
    move.print_move()
    exit()
    

class game(OthelloAlgorithm):

    """
    Class implementing a Minimax search algorithm, with alpha beta pruning, to 
    determine the best action to make in the board game othello.

    Author: dv18mln
    """

    def __init__(self, evaluator = SuperSmartEvaluator(), search_depth = 4):
        """
        Inits the class with a search depth of 4, and a new evaluator class. 
        The search depth will be updated using iterative deepening search. 
        """
        self.set_evaluator(evaluator)
        self.set_search_depth(search_depth)

    def set_evaluator(self, othello_evaluator):
        """
        Sets the evaluator to use in the algorithm.
        """
        self.evaluator = othello_evaluator.evaluate

    
    def set_search_depth(self, depth):
        """
        Sets the search depth of the tree.
        The depth is set to 4 by default. 
        :param depth: depth to be set.
        """

        self.search_depth = depth

    
    def evaluate(self, othello_position, timeout):
        """
        Function implemented from the interface. 
        Used to call the minimax search function and returns 
        the best evaluated action/move to make.
        :param othello_position: The initial position. 
        :return: The best move.
        """
        global move

        if othello_position.to_move():
            move.value = -9999
        else: 
            move.value = 9999

        while time.time() < timeout:
            
            E_markers = 0
            for i in range(3,7):
                for j in range(3,7):
                    if othello_position.board[i][j] == 'E':
                        E_markers += 1

            if E_markers >= 4:
                self.set_evaluator(EarlyGameEvalutor())
            else:
                self.set_evaluator(SuperSmartEvaluator())

            temp_action = self.minimax(othello_position, 0, -9999, 9999, timeout)

            if othello_position.to_move():
                if temp_action.value > move.value:
                    move = temp_action
                    
            else:
                if temp_action.value < move.value:
                    move = temp_action

            depth = self.search_depth + 1
            g.set_search_depth(depth)

        return move

    
    def minimax(self, othello_position, depth, alpha, beta, timeout):
        """
        Function to represent a minimax algorithm. The minimax algorithm
        is used to find the best move to make in a othello game. 
        The algorithm also implements alpha beta prunining to make the search
        more effective. 
        To evaluate how "good" a certain move is, a evalutation function is used.
        
        To determine the current best move, the algorithm also needs to find the
        best position for the opponent, as a take to "predict" that move. This in turn
        needs to check again for ITS opponents best position, etc. This is done 
        until a certain depth is reached. 

        :param othello_position: The position current position
        :param depth: The current depth
        :param alpha: alpha value used to determine if we do not need to explore more nodes (used by max).
        :param beta: beta value used to determine if we do not need to explore more nodes (used by min).
        :return: The action with the most score.
        """

        _min = 9999
        _max = -9999

        if depth >= self.search_depth:
            action = OthelloAction(0,0)
            action.value = self.evaluator(othello_position, timeout)
            if action.value == None:
                print_action()
            return action

        valid_moves = othello_position.get_moves(timeout)

        if valid_moves == None:
            print_action()

        if len(valid_moves) == 0:

            action = OthelloAction(0,0,True)

            action.value = self.evaluator(othello_position, timeout)
            if action.value == None:
                print_action()
            return action

        action = OthelloAction(0,0)
        
        for move in valid_moves:
            pos = othello_position.make_move(move, timeout)
            if pos == None:
                print_action()

            temp_action = self.minimax(pos, depth+1, alpha, beta, timeout)

            if othello_position.to_move():
                if temp_action.value > _max:
                    move.value = _max = temp_action.value
                    action = move
                
                if _max >= beta:
                    move.value = _max
                    return move

                if _max > alpha:
                    alpha = _max

            else:
                if temp_action.value < _min:
                    move.value = _min = temp_action.value
                    action = move

                    if _min <= alpha:
                        move.value = _min
                        return move

                    if _min < beta:
                        beta = _min
            
        return action

##########################################################
move = OthelloAction(0, 0)
if len(sys.argv) < 3:
    print("Too few arguments")
    exit()

if len(sys.argv[1]) > 1 and len(sys.argv[1]) < 65 or len(sys.argv[1]) > 65:
    print("Position string invalid.")
    exit()

# Check if position string is passed.
elif len(sys.argv[1]) == 65:
    pos = OthelloPosition(sys.argv[1])

#Else init with the start posiiton.
else:
    pos = OthelloPosition()
    pos.initialize()

g = game(search_depth=1)

timeout = time.time() + int(sys.argv[2])

move = g.evaluate(pos, timeout)
print_action()
