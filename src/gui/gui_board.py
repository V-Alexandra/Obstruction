from enum import Enum
import pygame
from src.domain.cell import StateOfCell
from src.gui.gui_cell import GUICell

class BoardConstants(Enum):
    COLOR = (255, 0, 127)
    BOARD_SIDE = 6
    MARGIN_WIDTH = 2
class GUIBoard(pygame.sprite.Sprite):
    def __init__(self, main_window, position, dimension,cell_color,side = BoardConstants.BOARD_SIDE.value ):
        super(GUIBoard, self).__init__()
        self.__main_window = main_window
        self.__surface = pygame.Surface((dimension,dimension))
        self.__cell_color = cell_color
        self.__rectangle = self.__surface.get_rect(left = position[0], top = position[1])
        self.__side = side
        self.__gui_board = self.__init_board_cells()
    @property
    def side(self):
        return self.__side
    def __init_board_cells(self):
        CELL_SIDE = self.__surface.get_height() / self.__side
        board = []
        for row in range(self.__side):
            board.append([])
            for column in range(self.__side):
                board[row].append(GUICell(self.__surface, (CELL_SIDE * row, CELL_SIDE * column), CELL_SIDE, self.__cell_color))
        return board

    def draw(self) :
        for row in range(self.__side) :
            for column in range(self.__side) :
                self.__gui_board[row][column].draw()
        self.__main_window.blit(self.__surface , self.__rectangle)

    def update_board(self , board) :
        for row in range(board.rows) :
            for column in range(board.columns) :
                state_dict = {StateOfCell.X_CELL : self.__gui_board[row][column].move_X ,
                              StateOfCell.O_CELL : self.__gui_board[row][column].move_O ,
                              StateOfCell.ACCESSIBLE_CELL : self.__gui_board[row][column].empty ,
                              StateOfCell.INACCESSIBLE_CELL : self.__gui_board[row][column].block}
                state_dict[board[row][column].state]()