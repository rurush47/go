from turn_manager import TurnManager
from vector2 import Vector2
from stone import Stone


class Board:
    size = 9

    def __init__(self):
        # create 2D array
        self.board = [[0 for i in range(Board.size)] for j in range(Board.size)]
        self.turn_manager = TurnManager()

    def place_stone(self, position):
        # TODO checks
        try:
            self.board[position.x][position.y] = Stone(self.turn_manager.get_current_player_color())
            self.next_turn()
        except IndexError:
            print 'Dude board is too fucking small!'

    def next_turn(self):
        self.turn_manager.next_turn()

    def is_empty(self, position):
        return True if self.board[position.x][position.y] == 0 else False

    def liberties_count(self, position, color):
        # TODO
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

    def get_board(self):
        return self.board
