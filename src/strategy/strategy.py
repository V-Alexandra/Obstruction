from abc import abstractmethod
from src.domain.cell import StateOfCell
from src.domain.coordinates import Point


class Strategy:
    @abstractmethod
    def move(self, *args):
        pass
    def _get_free_points(self, board):
        return [Point(x, y) for x in range(board.rows) for y in range(board.columns) if board[x][y].state == StateOfCell.ACCESSIBLE_CELL]