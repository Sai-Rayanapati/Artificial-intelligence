from tictactoe import Board
import numpy as np
import numpy.typing as npt
from typing import Iterable


# Adapted from https://github.com/abhikbhattacharjee/CS7IS2-Reinforcement-Learning-Adversarial-Search/blob/main/Connect4/connectClass.py
class Connect4(Board):
    def _init_(self, dimensions: Iterable[int] = ...) -> None:
        super()._init_(dimensions, x_in_a_row=4)
        self.state_dict = dict()
        self.dimensions = dimensions

    def possible_moves(self) -> npt.NDArray[np.int64]:
        possible_moves_list = []
        self.x_in_a_row = 4
        for move in super().possible_moves():
            if move[0] in possible_moves_list:
                continue
            else:
                possible_moves_list.append(move[0])
        return possible_moves_list

    def push(self, col):
        self.state_dict = dict()
        self.x_in_a_row = 4
        for move in super().possible_moves():
            self.state_dict[move[0]] = []
        for move in super().possible_moves():
            self.state_dict[move[0]].append(move[1])
        super().push((col, max(self.state_dict[col])))

    def copy(self):
        self.x_in_a_row = 4
        board = Connect4(self.dimensions)
        board.turn = self.turn
        board.board = self.board.copy()
        return board

    def set_markc4(self, coordinates: Iterable[int], player: int) -> None:
        self.state_dict = dict()
        self.x_in_a_row = 4
        for move in super().possible_moves():
            self.state_dict[move[0]] = []
        for move in super().possible_moves():
            self.state_dict[move[0]].append(move[1])
        col = coordinates
        super().set_mark((col, max(self.state_dict[col])), player)

    def get_column(self, col_no):
        _list = []
        for i in range(0, self.dimensions[1]):
            value = self.get_mark_at_position((col_no, i))
            _list.append(int(value))
        return _list

    def get_row(self, row_no):
        _list = []
        for i in range(0, self.dimensions[0]):
            value = self.get_mark_at_position((i, row_no))
            _list.append(int(value))
        return _list
