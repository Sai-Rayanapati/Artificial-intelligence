import math


def minimax_alphabeta(board, is_maximizer_turn, ai_player, alpha, beta):
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

    else:
        if is_maximizer_turn:
            best_score = -math.inf
            for move in board.possible_moves():
                board_copy = board.copy()
                board_copy.push(move)
                score = minimax_alphabeta(board_copy, False, ai_player, alpha, beta)
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
                score = minimax_alphabeta(board_copy, True, ai_player, alpha, beta)
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
        score = minimax_alphabeta(board_copy, is_maximizer_turn, ai_player, -math.inf, math.inf)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
