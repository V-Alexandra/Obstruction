
from jproperties import Properties
from src.gui.gui import GUI
from src.ui.ui import UI
from src.domain.board import Board
from src.services.services import GameService
from src.strategy.beginner import BeginnerStrategy
from src.strategy.minimax import MinimaxStrategy
from src.strategy.random import RandomStrategy


class ProgramSettings:
    def __init__(self, file_path):
        properties = Properties()
        with open(file_path, 'rb') as configuration_file:
            properties.load(configuration_file)
        try:
            self.__ui = self.__get_ui(properties['INTERFACE'].data)
            self.__strategy = self.__get_strategy(properties['STRATEGY'].data)
            self.__human_symbol = properties['HUMAN'].data
            self.__computer_symbol = properties['COMPUTER'].data
        except KeyError as keyError:
            print(keyError, '\n')
        except Exception as exception:
            print("Unexpected exception occurred: '{}'.\n".format(exception))
            exit(0)

    def __get_ui(self, ui):
        ui_dictionary = {'ui': UI, 'gui': GUI}
        return ui_dictionary[ui]

    def __get_strategy(self, strategy):
        strategy_dictionary = {'random': RandomStrategy, 'beginner': BeginnerStrategy, 'minimax': MinimaxStrategy}
        return strategy_dictionary[strategy]

    @property
    def ui(self):
        return self.__ui

    @property
    def strategy(self):
        return self.__strategy

    @property
    def human(self):
        return self.__human_symbol

    @property
    def computer(self):
        return self.__computer_symbol


if __name__ == "__main__":
    SETTINGS_FILE_PATH = '../settings.properties'
    settings = ProgramSettings(SETTINGS_FILE_PATH)
    board = Board()
    strategy = settings.strategy()
    game = GameService(board, strategy)
    ui = settings.ui(game, settings.human, settings.computer)
    ui.run()