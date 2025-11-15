from enum import Enum
class StateOfCell(Enum):
    ACCESSIBLE_CELL = 0
    INACCESSIBLE_CELL = 1
    X_CELL = 2
    O_CELL = 3
    TEMPORARILY_OCCUPIED = 4
class Cell:
    state: StateOfCell = StateOfCell.ACCESSIBLE_CELL
    def move_X(self):
        self.state = StateOfCell.X_CELL
    def move_O(self):
        self.state = StateOfCell.O_CELL
    def empty(self):
        self.state = StateOfCell.ACCESSIBLE_CELL
    def blocked(self):
        self.state = StateOfCell.INACCESSIBLE_CELL
    def __str__(self):
        state_of_cell = {0: '', 1: '#', 2: 'X', 3: 'O'}
        return state_of_cell[self.state.value]