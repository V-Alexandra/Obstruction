import unittest

from src.domain.cell import Cell, StateOfCell


class TestCell(unittest.TestCase):
    def setUp(self):
        self.__cell = Cell()

    def test_putX(self):
        self.__cell.move_X()
        self.assertEqual(self.__cell.state, StateOfCell.X_CELL)

    def test_putO(self):
        self.__cell.move_O()
        self.assertEqual(self.__cell.state, StateOfCell.O_CELL)

    def test_free(self):
        self.__cell.free()
        self.assertEqual(self.__cell.state, StateOfCell.ACCESSIBLE_CELL)

    def test_block(self):
        self.__cell.block()
        self.assertEqual(self.__cell.state, StateOfCell.INACCESSIBLE_CELL)

    def test_str(self):
        self.__cell.move_X()
        self.assertEqual(str(self.__cell), 'X')