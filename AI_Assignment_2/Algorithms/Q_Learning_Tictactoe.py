import numpy as np
import random
from Agents.default_agent_tictactoe import default_agent as default_tictactoe


class QLearningAgent:
    def __init__(self, epsilon, alpha, gamma):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.q_table = dict()

    def get_reward(self, board):
        game_result = board.result()
        if game_result is not None:
            if game_result == 1:
                return 10
            elif game_result == 2:
                return -10
            elif game_result == 0:
                return 1
        else:
            return 0

    def state_to_str(self, board):
        return str(board.board.flatten().tolist())

    def init_QTable(self, board):
        state = self.state_to_str(board)
        if state not in self.q_table:
            possible_moves = board.possible_moves().tolist()
            self.q_table[state] = {tuple(move): 0.0 for move in possible_moves}
        return state


    def update_q_values(self, board, action):
        current_state = self.init_QTable(board)
        reward = self.get_reward(board)
        future_board = board.copy()
        future_board.push(action)
        future_state = self.init_QTable(future_board)
        old_q_value = self.q_table[current_state][action]

        if future_board.result() is not None:
            new_q_value = old_q_value + self.alpha * (reward - old_q_value)
        else:
            future_q_values = self.q_table[future_state]
            if future_board.turn == 1:
                expected_q_values = max(future_q_values.values())
            else:
                expected_q_values = min(future_q_values.values())
            new_q_value = old_q_value + self.alpha * (reward + self.gamma * expected_q_values - old_q_value)

        self.q_table[current_state][action] = new_q_value

    def minmax(self, q_values, minmax):
        optimal_value = minmax(list(q_values.values()))
        count = list(q_values).count(minmax)
        if count > 1:
            best_moves = [move for move in list(q_values.keys()) if q_values[move] == optimal_value]
            move = best_moves[np.random.choice(len(best_moves))]
        else:
            move = max(q_values, key=q_values.get)
        return move

    def choose_action(self, board):
        if random.uniform(0, 1) < self.epsilon:
            return tuple(default_tictactoe(board, board.turn))
        else:
            current_state = self.init_QTable(board)
            q_values = self.q_table[current_state]
            if board.turn == 1:
                return self.minmax(q_values, max)
            elif board.turn == 2:
                return self.minmax(q_values, min)

    def train(self, board, episodes):
        decay_rate = 0.9
        for episode in range(episodes):
            print("Episode no:", episode)
            board_copy = board.copy()
            if episode != 0 and episode % 5000 == 0:
                self.epsilon = self.epsilon * decay_rate
                print(self.epsilon)
            while board_copy.result() is None:
                action = self.choose_action(board_copy)
                self.update_q_values(board_copy, action)
                board_copy.push(action)

    def get_q_table(self):
        return self.q_table

    def set_q_table(self, q_table):
        self.q_table = q_table
