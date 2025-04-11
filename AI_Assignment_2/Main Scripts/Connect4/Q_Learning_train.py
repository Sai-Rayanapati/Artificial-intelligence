import os
from Connect4.Connect4 import Connect4
import pickle
from Algorithms.Q_Learning_Connect4 import QLearningAgent


TicTacToeBoard = Connect4(dimensions=(7, 6))
TicTacToeAgent = QLearningAgent(0.9, 0.3, 0.9)
TicTacToeAgent.train(TicTacToeBoard.copy(), 10000)
directory = "Q_Learning_models"

if not os.path.exists(directory):
    os.makedirs(directory)

file_path = os.path.join(directory, "QTable_connect4.pkl")

pickle.dump(TicTacToeAgent.get_q_table(), open(file_path, "wb"))
