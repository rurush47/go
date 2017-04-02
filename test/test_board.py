from unittest import TestCase
from board import Board
from stone_color import StoneColor
from vector2 import Vector2


class TestBoard(TestCase):
    def test_place_stone(self):
        self.fail() #WHY RURKU ?

    def test_is_empty(self):
        Board.size = 9
        b = Board()
        pos1 = Vector2(2, 3)
        pos2 = Vector2(3, 4)

        b.board[2][3] = StoneColor.BLACK

        self.assertEquals(b.is_empty(pos1), False)
        self.assertEquals(b.is_empty(pos2), True)

    def test_liberties_count(self):
        Board.size = 9
        b = Board()
        board = b.get_board()

        board[5][5] = StoneColor.BLACK
        board[5][6] = StoneColor.BLACK
        board[6][5] = StoneColor.BLACK
        board[5][4] = StoneColor.BLACK

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

        stone = StoneColor.BLACK
        b.board[2][3] = stone

        stone1 = b.get_stone_at_position(pos1)

        print stone1

        stone2 = b.get_stone_at_position(pos2)

        self.assertEquals(stone2, None)

    def test_get_neighbors_of_color(self):
        Board.size = 9
        b = Board()
        board = b.get_board()

        board[5][5] = StoneColor.BLACK
        board[5][6] = StoneColor.BLACK
        board[6][5] = StoneColor.BLACK
        board[5][4] = StoneColor.BLACK
        board[4][5] = StoneColor.WHITE

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

    def test_get_dead_stones_string(self):
        Board.size = 9
        b = Board()
        board = b.get_board()

        # x
        # 0x
        # 00x

        board[0][0] = StoneColor.BLACK
        board[0][1] = StoneColor.BLACK
        board[1][0] = StoneColor.BLACK
        board[0][2] = StoneColor.WHITE
        board[1][1] = StoneColor.WHITE
        board[2][0] = StoneColor.WHITE

        #   00
        #  0xx0
        # 0xxx0
        # 0xxx0
        # 0000

        board[5][5] = StoneColor.BLACK
        board[6][5] = StoneColor.BLACK
        board[4][5] = StoneColor.BLACK
        board[6][6] = StoneColor.BLACK
        board[5][6] = StoneColor.BLACK
        board[4][6] = StoneColor.BLACK
        board[5][7] = StoneColor.BLACK
        board[6][7] = StoneColor.BLACK

        board[3][4] = StoneColor.WHITE
        board[3][5] = StoneColor.WHITE
        board[3][6] = StoneColor.WHITE
        board[4][4] = StoneColor.WHITE
        board[4][7] = StoneColor.WHITE
        board[5][4] = StoneColor.WHITE
        board[5][8] = StoneColor.WHITE
        board[6][4] = StoneColor.WHITE
        board[6][8] = StoneColor.WHITE
        board[7][5] = StoneColor.WHITE
        board[7][6] = StoneColor.WHITE
        board[7][7] = StoneColor.WHITE

        pos = Vector2(0, 0)
        pos2 = Vector2(5, 5)
        list1 = b.get_stones_string(pos, StoneColor.BLACK)
        list2 = b.get_stones_string(pos2, StoneColor.BLACK)

        self.assertEquals(len(list1), 3)
        self.assertEquals(len(list2), 8)
