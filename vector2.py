class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if self.x is other.x and self.y is other.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.x + self.y)
