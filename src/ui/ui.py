from src.domain.coordinates import Point
from src.services.services import CoordinatesError, GameError

class UI_Error(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class UI:
    def __init__(self, game, human, computer):
        self.__game = game
        self.__human = human
        self.__computer = computer
    def __human_move(self):
        move_completed = False
        while not move_completed:
            try:
                move_completed = True
                print("Your turn! ")
                coordinates = self.__GetHumanMove()
                game_over = self.__game.HumanMove(self.__human, coordinates)
                print('Move successfully performed.\n')
                return game_over
            except (CoordinatesError, UI_Error) as error:
                print(error)
                move_completed = False
    def __computer_move(self):
        print("Computer's turn: ")
        print('Computer move succesfully performed.\n')
        return self.__game.ComputerMove(self.__computer)

    def __GetHumanMove(self):
        x_coordinate = input('Please input the x coordinate of your move: ')
        y_coordinate = input('Please input the y coordinate of your move: ')
        if not x_coordinate.isdigit() or not y_coordinate.isdigit():
            raise UI_Error('({}, {}) is not a valid point.\n'.format(x_coordinate, y_coordinate))
        return Point(int(x_coordinate) - 1, int(y_coordinate) - 1)
    def __DrawBoard(self):
        print(self.__game.board)
    def run(self):
        try:
            symbol_turn = {self.__human: self.__human_move, self.__computer: self.__computer_move}
            game_over = False
            while not game_over:
                self.__DrawBoard()
                game_over = symbol_turn['X']()
                self.__DrawBoard()
                if game_over:
                    print('Player X wins!\n')
                else:
                    game_over  = symbol_turn['O']()
                    if game_over:
                        print('Player O wins!\n')
            self.__DrawBoard()
        except Exception as exception:
            print("Unexpected error: {}.\n".format(exception))