from tictactoe import Board
import random


def random_agent(board):
    possible_moves = board.possible_moves()
    random_move = random.choice(possible_moves)

    return random_move.tolist()


if __name__=='__main__':

    board = Board(dimensions=(3,3))

    print(random_agent(board))
