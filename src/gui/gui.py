from enum import Enum
import os
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from src.domain.coordinates import Point
from src.gui.gui_board import GUIBoard
from src.ui.ui import UI_Error
from src.services.services import CoordinatesError, GameError

class GUIConstants:
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 700
    BOARD_DIMENSION = 700
    WINNER_FONT_DIM = 40
    BACKGROUND_COLOR = (190 , 205 , 215)
    CELL_COLOR = (253 , 188 , 188)
    OPTIONAL_TEXT_COLOR = (61 , 93 , 154)
    TEXT_COLOR = (255 , 0 , 127)
    WINDOW_CAPTION = 'Obstruction'
    END_GAME_TIME_WAIT = 5000

class GUI:
    def __init__(self, game, human, computer):
        pygame.init()
        pygame.display.set_caption(GUIConstants.WINDOW_CAPTION)
        icon = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + r'//src/icon/icon.png'
        programIcon = pygame.image.load(icon)
        pygame.display.set_icon(programIcon)
        self.__game = game
        self.__main_window = pygame.display.set_mode((GUIConstants.SCREEN_WIDTH, GUIConstants.SCREEN_HEIGHT))
        self.__gui_board = GUIBoard(self.__main_window , (0 , 0) , GUIConstants.BOARD_DIMENSION ,
                                    GUIConstants.CELL_COLOR)
        self.__human_symbol = human
        self.__computer_symbol = computer
    def __find_board_position(self, window_position):

        x, y = window_position[0], window_position[1]
        if x > GUIConstants.BOARD_DIMENSION or y > GUIConstants.BOARD_DIMENSION:
            return None

        CELL_DIMENSION = GUIConstants.BOARD_DIMENSION // self.__gui_board.side
        return Point(x // CELL_DIMENSION, y // CELL_DIMENSION)

    def __human_turn(self, position):
        try:
            return self.__game.HumanMove(self.__human_symbol, self.__find_board_position(position))
        except (CoordinatesError, UI_Error) as inputError:
            return None

    def __computer_turn(self):
        return self.__game.ComputerMove(self.__computer_symbol)

    def __display_winner(self , winner) :

        font = pygame.font.SysFont('Comic Sans MS' , GUIConstants.WINNER_FONT_DIM , bold = True)


        text = '{} won the game!'.format(winner)


        text_surface = font.render(text , True , (255 , 255 , 255))
        text_rect = text_surface.get_rect(center = (GUIConstants.SCREEN_WIDTH / 2 , 75))


        outline_surface = font.render(text , True , (255 , 0 , 127))
        outline_rect = outline_surface.get_rect(center = (GUIConstants.SCREEN_WIDTH / 2 , 75))

        self.__main_window.fill(GUIConstants.BACKGROUND_COLOR)
        self.__gui_board.draw()
        self.__main_window.blit(outline_surface , outline_rect.move(-3 , -3))
        self.__main_window.blit(outline_surface , outline_rect.move(3 , -3))
        self.__main_window.blit(outline_surface , outline_rect.move(-3 , 3))
        self.__main_window.blit(outline_surface , outline_rect.move(3 , 3))


        self.__main_window.blit(text_surface , text_rect)

        pygame.display.update()


        pygame.time.wait(GUIConstants.END_GAME_TIME_WAIT)

    def __handle_mousebuttonup_event(self, position):

        game_over = self.__human_turn(position)
        if game_over is None:
            return False
        elif game_over:
            self.__gui_board.update_board(self.__game.board)
            self.__main_window.fill(GUIConstants.BACKGROUND_COLOR)
            self.__gui_board.draw()
            pygame.display.flip()
            self.__display_winner('You')
            return True
        game_over = self.__computer_turn()
        if game_over:
            self.__gui_board.update_board(self.__game.board)
            self.__main_window.fill(GUIConstants.BACKGROUND_COLOR)
            self.__gui_board.draw()
            self.__display_winner('Computer')
            return True
        return False

    def run(self):
        try:
            running = True
            while running:
                for event in pygame.event.get():
                    running = event.type != QUIT and (event.type != KEYDOWN or event.key != K_ESCAPE)
                    if event.type == pygame.MOUSEBUTTONUP:
                        position = pygame.mouse.get_pos()
                        if self.__handle_mousebuttonup_event(position):
                            running = False
                        self.__gui_board.update_board(self.__game.board)
                self.__main_window.fill(GUIConstants.BACKGROUND_COLOR)
                self.__gui_board.draw()
                pygame.display.flip()
        except (UI_Error, CoordinatesError, GameError) as error:
            pass