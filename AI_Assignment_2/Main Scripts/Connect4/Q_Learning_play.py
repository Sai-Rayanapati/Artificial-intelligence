from matplotlib import pyplot as plt
from Connect4 import Connect4
from Algorithms.Q_Learning_Connect4 import QLearningAgent
import pickle
from Agents.default_agent_connect4 import default_agent
from Algorithms.Minimax_Alpha_Beta_Connect4 import minimax_best_move
from Agents.random_agent import random_agent

qlearning_wins = 0
default_wins = 0
game_draw = 0
minimax_wins = 0
random_wins = 0

q_player = QLearningAgent(0.9, 0.3, 0.9)

qFile = open("Q_Learning_models/QTable_connect4.pkl", "rb")

q_table = pickle.load(qFile)

q_player.set_q_table(q_table)

board = Connect4(dimensions=(7,6))

no_of_games = input("No of games: ")
opponent = input("Choose opponent (Default or Random or Minimax): ")
for game in range(int(no_of_games)):
    board_copy = board.copy()

    print(board_copy)
    print(board_copy.turn)

    while board_copy.result() is None:
        if board_copy.turn == 1:
            move = q_player.choose_action(board_copy)
            print("Q-Agent Turn. Selected Move: ", move)
            board_copy.push(move)
            print(board_copy)
        elif board_copy.turn == 2:
            move = None
            if opponent == "Default":
                move = default_agent(board_copy, board_copy.turn)
                print("Default Agent Turn. Selected Move: ", move)
            elif opponent == "Random":
                move = random_agent(board_copy)
                print("Random Agent Turn. Selected Move: ", move)
            elif opponent == "Minimax":
                move = minimax_best_move(board_copy,False,2)
                print("Minimax Agent Turn. Selected Move: ", move)
            board_copy.push(move)
            print(board_copy)

    if opponent == "Default":
        if board_copy.result() is not None:
            if board_copy.result() == 1:
                print("Q Learning agent wins!")
                qlearning_wins = qlearning_wins + 1
            elif board_copy.result() == 2:
                print("Default player wins!")
                default_wins = default_wins + 1
            elif board_copy.result() == 0:
                print("Game Draw!")
                game_draw = game_draw + 1
    if opponent == "Random":
        if board_copy.result() is not None:
            if board_copy.result() == 1:
                print("Q Learning agent wins!")
                qlearning_wins = qlearning_wins + 1
            elif board_copy.result() == 2:
                print("Random player wins!")
                random_wins = random_wins + 1
            elif board_copy.result() == 0:
                print("Game Draw!")
                game_draw = game_draw + 1
    if opponent == "Minimax":
        if board_copy.result() is not None:
            if board_copy.result() == 1:
                print("Q Learning agent wins!")
                qlearning_wins = qlearning_wins + 1
            elif board_copy.result() == 2:
                print("Minimax player wins!")
                minimax_wins = minimax_wins + 1
            elif board_copy.result() == 0:
                print("Game Draw!")
                game_draw = game_draw + 1

if opponent == "Default":
    # Graph of the results
    categories = ['Q Learning Player Wins', 'Default Player Wins', 'Draws']

    # Values
    values = [qlearning_wins, default_wins, game_draw]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['blue', 'red', 'green'])

    # Adding title and labels
    plt.title(f'Q Learning Player vs Default Player - Connect4 ({no_of_games} games)\n')
    plt.xlabel('Outcome')
    plt.ylabel('Number of Games')

    plt.savefig("figures/Q_Learning_vs_default(Connect4).png")

    # Showing the plot
    plt.show()

if opponent == "Random":
    # Graph of the results
    categories = ['Q Learning Player Wins', 'Random Player Wins', 'Draws']

    # Values
    values = [qlearning_wins, random_wins, game_draw]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['blue', 'red', 'green'])

    # Adding title and labels
    plt.title(f'Q Learning Player vs Random Player - Connect4 ({no_of_games} games)\n')
    plt.xlabel('Outcome')
    plt.ylabel('Number of Games')

    plt.savefig("figures/Q_Learning_vs_random(Connect4).png")

    # Showing the plot
    plt.show()

if opponent == "Minimax":
    # Graph of the results
    categories = ['Q Learning Player Wins', 'Minimax Player Wins', 'Draws']

    # Values
    values = [qlearning_wins, minimax_wins, game_draw]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['blue', 'red', 'green'])

    # Adding title and labels
    plt.title(f'Q Learning Player vs Default Player - Connect4 ({no_of_games} games)\n')
    plt.xlabel('Outcome')
    plt.ylabel('Number of Games')

    plt.savefig("figures/Q_Learning_vs_minimax(Connect4 - 1000).png")

    # Showing the plot
    plt.show()

