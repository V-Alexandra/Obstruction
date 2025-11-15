import unittest

from src.domain.coordinates import Point
from src.domain.board import Board
from src.domain.cell import Cell, StateOfCell
from src.strategy.beginner import BeginnerStrategy
from src.strategy.minimax import MinimaxStrategy, MinimaxResults
from src.strategy.random import RandomStrategy


class TestBeginnerStrategy(unittest.TestCase):
    def setUp(self):
        self.__strategy = BeginnerStrategy()
        self.__board = Board()

        self.__board[1][1] = self.__board[4][1] = Cell(StateOfCell.X_CELL)
        self.__board[1][4] = self.__board[3][3] = Cell(StateOfCell.O_CELL)
        free_cells = [(5, 3), (5, 4), (5, 5), (4, 5), (3, 5)]
        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                if (row, column) not in free_cells and self.__board[row][column].state == StateOfCell.ACCESSIBLE_CELL:
                    self.__board[row][column].state = StateOfCell.INACCESSIBLE_CELL

    def test_attempt_defensive_move(self):
        self.assertEqual(self.__strategy.move(self.__board), Point(5, 5))

    def test_attempt_winning_move(self):
        self.__board[3][5].state = StateOfCell.X_CELL
        self.__board[4][5].state = StateOfCell.INACCESSIBLE_CELL
        self.assertEqual(self.__strategy.attempt_winning_move(self.__board), Point(5, 4))
        self.__board[3][5].state = self.__board[4][5].state = StateOfCell.ACCESSIBLE_CELL

    def test_move(self):
        self.__board[3][5].state = StateOfCell.X_CELL
        self.__board[4][5].state = StateOfCell.INACCESSIBLE_CELL
        self.assertEqual(self.__strategy.move(self.__board), Point(5, 4))
        self.__board = Board()
        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                if (row, column) != (0, 0) and (row, column) != (5, 5):
                    self.__board[row][column].state = StateOfCell.INACCESSIBLE_CELL
        random_point = self.__strategy.move(self.__board)
        self.assertEqual(self.__board[random_point.x][random_point.y].state, StateOfCell.ACCESSIBLE_CELL)


class TestRandomStrategy(unittest.TestCase):
    def setUp(self):
        self.__board = Board(2, 2)
        self.__board[0][1].state = self.__board[1][0].state = self.__board[1][1].state = CellState.BLOCKED_CELL
        self.__strategy = RandomStrategy()

    def test_random_strategy(self):
        self.assertEqual(self.__strategy.move(self.__board), Point(0, 0))


class TestMinimaxStrategy(unittest.TestCase):
    def setUp(self):
        self.__board = Board()
        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                self.__board[row][column].state = StateOfCell.INACCESSIBLE_CELL

        self.__board[0][1].state = self.__board[1][0].state = self.__board[1][1].state = self.__board[1][2].state \
                                    = self.__board[2][0].state = StateOfCell.ACCESSIBLE_CELL

        self.__minimax_strategy = MinimaxStrategy()

    def test_move(self):
        move = self.__minimax_strategy.move(self.__board)
        self.assertEqual(move, Point(1, 1))

    def test_attempt_impossible_move(self):
        self.__minimax_strategy = MinimaxStrategy([Point(0, 0)])
        self.assertEqual(False, self.__minimax_strategy.attempt_move(self.__board))

    def test_minimax_for_high_possible_depth(self):
        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                self.__board[row][column].state = StateOfCell.INACCESSIBLE_CELL
        self.__board[0][0].state = StateOfCell.ACCESSIBLE_CELL
        score = self.__minimax_strategy.minimax(self.__board, 3, True)
        self.assertEqual(score, MinimaxResults.NONE.value)

    def test_minimax_always_winning_option(self):
        for row in range(self.__board.rows):
            for column in range(self.__board.columns):
                self.__board[row][column].state = StateOfCell.INACCESSIBLE_CELL
        self.__board[0][0].state = StateOfCell.ACCESSIBLE_CELL

        score = self.__minimax_strategy.minimax(self.__board, 0, True)
        self.assertEqual(MinimaxResults.MINIMIZER.value, score)

    def test_minimax_always_losing_option(self):
        self.__board[3][3].state = self.__board[4][4].state = self.__board[3][4].state = self.__board[4][3].state = CellState.FREE_CELL
        score = self.__minimax_strategy.minimax(self.__board, 0, True)
        self.assertEqual(score, MinimaxResults.MAXIMIZER.value, score)