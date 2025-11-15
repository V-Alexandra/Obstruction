import unittest

from src.domain.board import Board
from src.domain.cell import StateOfCell
from src.domain.coordinates import Point
from src.services.services import GameService, CoordinatesError
from src.strategy.beginner import BeginnerStrategy


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.__game = GameService(Board(), BeginnerStrategy())

    def test_move(self):
        point = Point(0, 0)
        h_symbol = 'X'
        c_symbol = 'O'
        board = self.__game.board
        self.__game.HumanMove(h_symbol, point)

        blockades = [(0, 1), (1, 1), (1, 0)]
        for row in range(board.rows):
            for column in range(board.columns):
                if not row and not column:
                    self.assertEqual(board[row][column].state, StateOfCell.X_CELL)
                elif (row, column) in blockades:
                    self.assertEqual(board[row][column].state, StateOfCell.INACCESSIBLE_CELL)
                else:
                    self.assertEqual(board[row][column].state, StateOfCell.ACCESSIBLE_CELL)

        point = Point(-1, 0)
        self.assertRaises(CoordinatesError, self.__game.HumanMove(), h_symbol, point)
        try:
            self.__game.HumanMove(h_symbol, point)
        except CoordinatesError as ce:
            self.assertEqual('CoordinatesError: Invalid coordinates.\n', str(ce))
        point = Point(1, 1)
        self.assertRaises(CoordinatesError, self.__game.HumanMove(), h_symbol, point)
        self.__game.ComputerMove(c_symbol)
        cnt = 0
        for row in range(board.rows):
            for column in range(board.columns):
                if board[row][column].state == StateOfCell.O_CELL:
                    cnt += 1
        self.assertEqual(cnt, 1)