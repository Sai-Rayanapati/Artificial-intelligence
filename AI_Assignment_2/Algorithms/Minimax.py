import math


# Code inspired from https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
def minimax(board, is_maximizer_turn, ai_player):
    game_result = board.result()

    if game_result is not None:
        # Tie
        if game_result == 0:
            return 0

        if ai_player == 1:
            # Win
            if game_result == 1:
                return 10
            # Loose
            elif game_result == 2:
                return -10

        if ai_player == 2:
            # Loose
            if game_result == 1:
                return -10
            # Win
            elif game_result == 2:
                return 10

    scores = []

    for move in board.possible_moves():
        board_copy = board.copy()
        board_copy.push(move)
        scores.append(minimax(board_copy, not is_maximizer_turn, ai_player))

    if is_maximizer_turn:
        return max(scores)
    else:
        return min(scores)


def minimax_best_move(board, is_maximizer_turn, ai_player):
    best_score = -math.inf
    best_move = None

    for move in board.possible_moves():
        board_copy = board.copy()
        board_copy.push(move)
        score = minimax(board_copy, is_maximizer_turn, ai_player)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
