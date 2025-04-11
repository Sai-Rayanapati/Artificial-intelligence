import random
from tictactoe import Board


def default_agent(board, player):
    # Check for win moves
    for move in board.possible_moves():
        board_copy = board.copy()
        board_copy.set_mark(move.tolist(), player)
        # If player wins
        if board_copy.result() == player:
            return move.tolist()

    # Check for block moves
    opponent = 1 if player == 2 else 2
    for move in board.possible_moves():
        board_copy = board.copy()
        board_copy.set_mark(move.tolist(), opponent)
        # If opponent wins ie. blocking the move
        if board_copy.result() == opponent:
            return move.tolist()

    # If no win or block moves, return a random move
    return random.choice(board.possible_moves().tolist())


if __name__=='__main__':

    board = Board(dimensions=(3,3))
    board.set_mark((0,0), 1)
    board.set_mark((0, 1), 1)

    print(default_agent(board,2))