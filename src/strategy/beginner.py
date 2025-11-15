from src.strategy.strategy import Strategy
from src.domain.cell import StateOfCell
from random import randint


class BeginnerStrategy(Strategy):
    def move(self, board):
        winning_move = self.attempt_winning_move(board)
        if winning_move:
            return winning_move
        possible_moves = self.attempt_defensive_move(board)
        if possible_moves:
            return self.make_random_move(board, possible_moves)
        return self.make_random_move(board, self._get_free_points(board))

    def make_random_move(self, board, possible_moves):
        return possible_moves[randint(0, len(possible_moves) - 1)]

    def attempt_winning_move(self, board, default_temp_moves=[]):
        for point in self._get_free_points(board):
            if board[point.x][point.y].state == StateOfCell.ACCESSIBLE_CELL:
                self.temporarily_moves(board, [point] + default_temp_moves)
                if not len(self._get_free_points(board)):
                    self.free_temporary_occupations(board)
                    return point
                self.free_temporary_occupations(board)
        return None

    def attempt_defensive_move(self, board):
        possible_moves = []
        for point in self._get_free_points(board):
            if not self.attempt_winning_move(board, [point]):
                possible_moves.append(point)
            self.free_temporary_occupations(board)
        return None if possible_moves == [] else possible_moves

    def temporarily_moves(self, board, points):
        directions = [-1, 0, 1]
        for point in points:
            for row_dir in directions:
                for column_dir in directions:
                    if point.x + row_dir in range(board.rows) and point.y + column_dir in range(board.columns) and board[point.x + row_dir][point.y + column_dir].state == StateOfCell.ACCESSIBLE_CELL:
                        board[point.x + row_dir][point.y + column_dir].state = StateOfCell.TEMPORARILY_OCCUPIED

    def free_temporary_occupations(self, board):
        for row in range(board.rows):
            for column in range(board.columns):
                if board[row][column].state == StateOfCell.TEMPORARILY_OCCUPIED:
                    board[row][column].state = StateOfCell.ACCESSIBLE_CELL