import random
from Connect4 import Connect4
def default_agent(board, player):
    # Check for win moves
    for move in board.possible_moves():
        board_copy = board.copy()
        board_copy.set_markc4(move.tolist(), player)
        # If player wins
        if board_copy.result() == player:
            return move.tolist()

    # Check for block moves
    opponent = 1 if player == 2 else 2
    for move in board.possible_moves():
        board_copy = board.copy()
        board_copy.set_markc4(move.tolist(), opponent)
        # If opponent wins ie. blocking the move
        if board_copy.result() == opponent:
            return move.tolist()

    # If no win or block moves, return a random move
    return random.choice(board.possible_moves())


if __name__=='__main__':
    board = Connect4(dimensions=(7, 6))
    print(board)

    board.push(1)
    print(board)

    while board.result() is None:
        user_input = input("Enter Column: ")
        board.push(int(user_input))
        print(board)
        board.push(default_agent(board,2))
        print(board)

