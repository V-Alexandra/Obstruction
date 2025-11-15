from enum import Enum
import pygame
class CellConstants(Enum):
    INNACCESSIBLE_COLOR = (255, 181, 115)
    MARGIN_SHRINK_FACTOR = 25
    COLOR = (255, 0, 127)

class GUICell(pygame.sprite.Sprite):
    def __init__(self, main_surface, position, dimension, color):
        super(GUICell, self).__init__()
        self.__main_surface = main_surface
        self.__surface = pygame.Surface((dimension, dimension))
        self.__surface.fill(color)
        self.__color = color
        self.__rectangle = self.__surface.get_rect(left=position[0], top=position[1])
    def draw(self):
        self.__DrawCell()
        self.__DrawMargin()
    def move_X(self):
        pygame.draw.line(self.__surface , CellConstants.COLOR.value , (0, 0) , (self.__surface.get_width(), self.__surface.get_height()) , 8)
        pygame.draw.line(self.__surface , CellConstants.COLOR.value , (0, self.__surface.get_height()) , (self.__surface.get_width(), 0) , 8)
    def move_O(self):
        circle = (self.__surface.get_width() / 2, self.__surface.get_height() / 2)
        pygame.draw.circle(self.__surface , CellConstants.COLOR.value , circle , self.__surface.get_width() / 3 , 8)
    def block(self):
        self.__surface.fill(CellConstants.INNACCESSIBLE_COLOR.value)
    def empty(self):
        self.__surface.fill(self.__color)
    def __DrawCell(self):
        self.__main_surface.blit(self.__surface, self.__rectangle)
    def __DrawMargin(self):
        HORIZONTAL_MARGIN_WIDTH = self.__surface.get_width()
        HORIZONTAL_MARGIN_HEIGHT = self.__surface.get_height() / CellConstants.MARGIN_SHRINK_FACTOR.value
        VERTICAL_MARGIN_WIDTH = self.__surface.get_width() / CellConstants.MARGIN_SHRINK_FACTOR.value
        VERTICAL_MARGIN_HEIGHT = self.__surface.get_height()
        BLACK_COLOR = (255 , 255 , 255)

        top_left_corners = {'N' : (0 , 0) , 'E' : (self.__surface.get_width() - VERTICAL_MARGIN_WIDTH , 0) ,
                            'S' : (0 , self.__surface.get_height() - HORIZONTAL_MARGIN_HEIGHT) , 'W' : (0 , 0)}
        dimensions = {'N' : (HORIZONTAL_MARGIN_WIDTH , HORIZONTAL_MARGIN_HEIGHT) ,
                      'E' : (VERTICAL_MARGIN_WIDTH , VERTICAL_MARGIN_HEIGHT) ,
                      'S' : (HORIZONTAL_MARGIN_WIDTH , HORIZONTAL_MARGIN_HEIGHT) ,
                      'W' : (VERTICAL_MARGIN_WIDTH , VERTICAL_MARGIN_HEIGHT)}
        for direction in top_left_corners :
            corner_point = top_left_corners[direction]
            dimension = dimensions[direction]
            pygame.draw.rect(self.__surface , BLACK_COLOR , pygame.Rect(corner_point[0] , corner_point[1] , dimension[0] , dimension[1]))