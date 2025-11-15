from enum import Enum
from texttable import Texttable
from src.domain.cell import Cell
from src.domain.iterator import Collection

class DefaultDimensions(Enum):
    ROWS = 6
    COLUMNS = 6

class Board:
    def __init__(self, rows = DefaultDimensions.ROWS.value, columns = DefaultDimensions.COLUMNS.value):
        self.__rows = rows
        self.__columns = columns
        self.__data = self.__CreateBoard()

    @property
    def rows(self):
        return self.__rows
    @property
    def columns(self):
        return self.__columns
    def __CreateBoard(self):
        return Collection([Collection([Cell() for column in range(self.__columns)]) for row in range(self.__rows)])

    def __getitem__(self, key):
        return self.__data[key]
    def __str__(self):
        representation = Texttable()
        header = [''] + [chr(ord('A') + index) for index in range(self.__columns)]
        representation.header(header)
        for row in range(self.__rows):
            row_data = [str(row + 1)] + [self.__data[row][column] for column in range(self.__columns)]
            representation.add_row(row_data)
        return representation.draw()
