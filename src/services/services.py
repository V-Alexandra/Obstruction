from src.domain.cell import StateOfCell
from src.domain.coordinates import Point

class GameError(Exception):
    def __init__(self, message):
        self._message = message
    def __str__(self):
        return self._message

class CoordinatesError(GameError):
    pass
class GameService:
    def __init__(self, board, strategy):
        self.__board = board
        self.__strategy = strategy
    @property
    def board(self):
        return self.__board
    def __GameOver(self):
        return not StateOfCell.ACCESSIBLE_CELL in [cell.state for row in range(self.__board.rows) for cell in self.__board[row]]
    def __GetCellState(self, point):
        return self.__board[point.x][point.y].state
    def __ValidateMove(self, point):
        if point.x not in range(self.__board.rows) or point.y not in range(self.__board.columns):
            raise CoordinatesError('Invalid coordinates.\n')
        if not self.__GetCellState(point) == StateOfCell.ACCESSIBLE_CELL:
            raise CoordinatesError('Cell is not accessible.\n')
    def __block_adjacent(self, point):
        blocked_cells = 0
        directions = [-1, 0 , 1]
        for row_direction in directions:
            for column_direction in directions:
                if point.x + row_direction in range(self.__board.rows) and point.y + column_direction in range(self.__board.columns) and Point(0,0) != Point(row_direction,column_direction):
                    self.__board[point.x + row_direction][point.y + column_direction].state = StateOfCell.INACCESSIBLE_CELL
                    blocked_cells += 1
        return blocked_cells
    def HumanMove(self, value, point):
        state_dictionary = {'X': StateOfCell.X_CELL, 'O': StateOfCell.O_CELL}
        self.__ValidateMove(point)
        self.__board[point.x][point.y].state = state_dictionary[value]
        self.__block_adjacent(point)
        return self.__GameOver()
    def ComputerMove(self, value):
        state_dictionary = {'X': StateOfCell.X_CELL, 'O': StateOfCell.O_CELL}
        point = self.__strategy.move(self.__board)
        x = point.x
        y = point.y
        self.__board[x][y].state = state_dictionary[value]
        self.__block_adjacent(Point(x, y))
        return self.__GameOver()
