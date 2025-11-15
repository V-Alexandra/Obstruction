from src.strategy.strategy import Strategy
from src.domain.cell import StateOfCell
from enum import Enum
import sys


class MinimaxResults(Enum):
    MAXIMIZER = sys.maxsize
    MINIMIZER = -sys.maxsize
    NONE = 0
    SCORE_INCREMENT = 1


class MinimaxStrategy(Strategy):
    def __init__(self, temporarily_occupied_cells=[]):
        self.__temporarily_occupied_cells = temporarily_occupied_cells

    def move(self, board):
        free_points = self._get_free_points(board)
        best_score = MinimaxResults.MINIMIZER.value
        best_move = None

        for point in free_points:
            self.__temporarily_occupied_cells.append(point)
            score = self.minimax(board, 0, True)
            self.__temporarily_occupied_cells.remove(point)
            if score >= best_score:
                best_score = score
                best_move = point
        return best_move

    def attempt_winning(self, board):
        free_points = self._get_free_points(board)
        for point in free_points:
            blocked = False
            for temporarily_cell in self.__temporarily_occupied_cells:
                if -1 <= temporarily_cell.x - point.x <= 1 and -1 <= temporarily_cell.y - point.y <= 1:
                    blocked = True
                    break
            if not blocked:
                return False
        return True

    def attempt_move(self, board):
        attempted_move = self.__temporarily_occupied_cells[-1]
        if board[attempted_move.x][attempted_move.y].state != StateOfCell.ACCESSIBLE_CELL:
            return False
        for cell in self.__temporarily_occupied_cells[:-1]:
            if -1 <= cell.x - attempted_move.x <= 1 and -1 <= cell.y - attempted_move.y <= 1:
                return False
        return True

    def minimax(self, board, depth, maximizer):
        if depth > 2:
            return MinimaxResults.NONE.value

        if self.attempt_winning(board):
            return MinimaxResults.MAXIMIZER.value

        free_points = self._get_free_points(board)
        in_depth_scores = []
        for point in free_points:
            self.__temporarily_occupied_cells.append(point)
            if not self.attempt_move(board):
                self.__temporarily_occupied_cells.remove(point)
                continue
            in_depth_scores.append(-self.minimax(board, depth + 1, not maximizer))
            self.__temporarily_occupied_cells.remove(point)
        maxim_score = MinimaxResults.MINIMIZER.value
        minim_score = MinimaxResults.MAXIMIZER.value
        for score in in_depth_scores:
            if score < minim_score:
                minim_score = score
            if score > maxim_score:
                maxim_score = score

        return maxim_score if maximizer else minim_score