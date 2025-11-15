from src.strategy.strategy import Strategy
from src.domain.cell import StateOfCell
from src.domain.coordinates import Point
from random import randint


class RandomStrategy(Strategy):
    def move(self, board):
        x = randint(0, board.rows - 1)
        y = randint(0, board.columns - 1)
        while board[x][y].state != StateOfCell.ACCESSIBLE_CELL:
            x = randint(0, board.rows - 1)
            y = randint(0, board.columns - 1)
        return Point(x, y)