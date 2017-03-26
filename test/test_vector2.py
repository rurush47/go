from unittest import TestCase

from vector2 import Vector2


class TestVector2(TestCase):
    def add_test(self):
        vector1 = Vector2(1, 1)
        vector2 = Vector2(2, 3)

        vector3 = vector1 + vector2
        self.assertEqual(vector3.x, 3)
        self.assertEqual(vector3.y, 4)
