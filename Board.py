from Vector2 import Vector2
from Stone import Stone


class Board:
    size = 9

    def __init__(self):
        # create 2D array
        self.board = [[0 for i in range(Board.size)] for j in range(Board.size)]

    def place_stone(self, position, color):
        # TODO checks
        try:
            self.board[position.x][position.y] = Stone(color)
        except IndexError:
            print 'Dude board is too fucking small!'

    def is_empty(self, position):
        return True if self.board[position.x][position.y] == 0 else False

    def liberties_count(self, position, color):
        #TODO
        pass

    @staticmethod
    def in_bounds(position):
        if 0 <= position.x < Board.size and 0 <= position.y < Board.size:
            return True
        else:
            return False

    def get_stone_at_position(self, position):
        if self.in_bounds(position):
            stone = self.board[position.x][position.y]
            if type(stone) is not Stone or stone is None:
                return None
            else:
                return stone