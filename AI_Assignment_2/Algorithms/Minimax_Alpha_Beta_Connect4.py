import math


# Code inspired from https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f and
# https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py#L85
def minimax_alphabeta(board, depth, is_maximizer_turn, ai_player, alpha, beta):
    game_result = board.result()

    if depth == 0 or game_result is not None:
        # Tie
        if game_result == 0:
            return 0

        elif game_result == 1:
            if ai_player == 1:
                return 10
            elif ai_player == 2:
                return -10
        elif game_result == 2:
            if ai_player == 1:
                return -10
            elif ai_player == 2:
                return 10
        else:
            return score_position(board, ai_player)

    else:
        if is_maximizer_turn:
            best_score = -math.inf
            for move in board.possible_moves():
                board_copy = board.copy()
                board_copy.push(move)
                score = minimax_alphabeta(board_copy, depth - 1, False, ai_player, alpha, beta)
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = math.inf
            for move in board.possible_moves():
                board_copy = board.copy()
                board_copy.push(move)
                score = minimax_alphabeta(board_copy, depth - 1, True, ai_player, alpha, beta)
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score


def minimax_best_move(board, is_maximizer_turn, ai_player):
    best_score = -math.inf
    best_move = None

    for move in board.possible_moves():
        board_copy = board.copy()
        board_copy.push(move)
        score = minimax_alphabeta(board_copy, 6, is_maximizer_turn, ai_player, -math.inf, math.inf)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def evaluate_window(window, player):
    score = 0
    opp_player = 2 if player == 1 else 1

    if window.count(player) == 4:
        score += 10
    elif window.count(player) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_player) == 3 and window.count(0) == 1:
        score -= 4

    return score


def score_position(board, player):
    score = 0

    ROW_COUNT = board.dimensions[1]
    COLUMN_COUNT = board.dimensions[0]

    # Score center column
    center_array = board.get_column(COLUMN_COUNT // 2)
    center_count = center_array.count(player)
    score += center_count * 3

    # Score horizontal
    for r in range(ROW_COUNT):
        row_array = board.get_row(r)
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + 4]
            score += evaluate_window(window, player)

    # Score vertical
    for c in range(COLUMN_COUNT):
        col_array = board.get_column(c)
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + 4]
            score += evaluate_window(window, player)

    # Score positive sloped diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board.get_mark_at_position((c + i, r + i)) for i in range(4)]
            score += evaluate_window(window, player)

    # Score negative sloped diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board.get_mark_at_position((c + i, r + 3 - i)) for i in range(4)]
            score += evaluate_window(window, player)

    return score
