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
        Board.size = 9
        b = Board()
        board = b.get_board()

        board[5][5] = Stone(StoneColor.BLACK)
        board[5][6] = Stone(StoneColor.BLACK)
        board[6][5] = Stone(StoneColor.BLACK)
        board[5][4] = Stone(StoneColor.BLACK)

        pos = Vector2(5, 5)
        count = b.liberties_count(pos)

        self.assertEquals(count, 1)

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

    def test_get_neighbors_of_color(self):
        Board.size = 9
        b = Board()
        board = b.get_board()

        board[5][5] = Stone(StoneColor.BLACK)
        board[5][6] = Stone(StoneColor.BLACK)
        board[6][5] = Stone(StoneColor.BLACK)
        board[5][4] = Stone(StoneColor.BLACK)
        board[4][5] = Stone(StoneColor.WHITE)

        pos = Vector2(5, 5)
        neigh_list_black = b.get_neighbors_of_color(pos, StoneColor.BLACK)
        neigh_list_white = b.get_neighbors_of_color(pos, StoneColor.WHITE)

        self.assertEquals(len(neigh_list_black), 3)
        self.assertEquals(len(neigh_list_white), 1)

    def test_get_surrounding_points_list(self):
        Board.size = 9
        b = Board()

        pos1 = Vector2(0, 0)
        pos2 = Vector2(5, 5)

        list1 = b.get_surrounding_points_list(pos1)
        list2 = b.get_surrounding_points_list(pos2)

        self.assertEquals(len(list1), 2)
        self.assertEquals(len(list2), 4)
