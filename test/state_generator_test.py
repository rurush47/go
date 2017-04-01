from unittest import TestCase

from board import Board
from stone_color import StoneColor
from vector2 import Vector2


class TestBoard(TestCase):
    def test_valid_states_generator(self):
        Board.size = 2
        b = Board()

        generator = b.valid_states_generator(StoneColor.BLACK)

        move1 = generator.next()
        move2 = generator.next()

        self.assertEqual(move1[0], Vector2(0, 0))
        self.assertEqual(move2[0], Vector2(0, 1))
