from unittest import TestCase
from board import Board
from stone_color import StoneColor
from vector2 import Vector2
from stone import Stone


class TestBoard(TestCase):
    def test_place_stone(self):
        self.fail()

    def test_is_empty(self):
        Board.size = 9
        b = Board()
        pos1 = Vector2(2, 3)
        pos2 = Vector2(3, 4)

        b.board[2][3] = Stone(StoneColor.BLACK)

        self.assertEquals(b.is_empty(pos1), False)
        self.assertEquals(b.is_empty(pos2), True)

    def test_liberties_count(self):
        self.fail()

    def test_in_bounds(self):
        Board.size = 9
        b = Board()
        pos1 = Vector2(2, 3)
        pos2 = Vector2(10, 4)
        pos3 = Vector2(-1, 5)

        self.assertEquals(b.in_bounds(pos1), True)
        self.assertEquals(b.in_bounds(pos2), False)
        self.assertEquals(b.in_bounds(pos3), False)

    def test_get_stone_at_position(self):
        Board.size = 9
        b = Board()
        pos1 = Vector2(2, 3)
        pos2 = Vector2(3, 5)

        stone = Stone(StoneColor.BLACK)
        b.board[2][3] = stone

        color = stone.get_color()
        stone1 = b.get_stone_at_position(pos1)

        print stone1

        stone2 = b.get_stone_at_position(pos2)

        self.assertEquals(color, stone1.get_color())
        self.assertEquals(stone2, None)
