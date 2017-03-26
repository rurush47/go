class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

Vector2.up = Vector2(0, 1)
Vector2.down = Vector2(0, -1)
Vector2.right = Vector2(1, 0)
Vector2.left = Vector2(-1, 0)
