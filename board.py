from turn_manager import TurnManager
from stone import Stone
from vector2 import Vector2


class Board:
    size = 9

    up = Vector2(0, 1)
    down = Vector2(0, -1)
    right = Vector2(1, 0)
    left = Vector2(-1, 0)

    def __init__(self):
        # create 2D array
        self.board = [[0 for i in range(Board.size)] for j in range(Board.size)]
        self.turn_manager = TurnManager()

    def place_stone(self, position):
        # TODO checks
        color = self.turn_manager.get_current_player_color()
        if self.is_empty(position) and self.liberties_count(position) is not 0 and self.get_neighbors_of_color():
            try:
                self.board[position.x][position.y] = Stone(color)
                self.next_turn()
            except IndexError:
                print 'Dude board is too fucking small!'

    def next_turn(self):
        self.turn_manager.next_turn()

    def is_empty(self, position):
        return True if self.board[position.x][position.y] == 0 else False

    def liberties_count(self, position):
        count = 0

        points_to_check = self.get_surrounding_points_list(position)

        for i in points_to_check:
            if self.in_bounds(i) and self.is_empty(i):
                count += 1

        return count

    def get_neighbors_of_color(self, position, color):
        stones_list = []
        surrounding_positions = self.get_surrounding_points_list(position)

        for i in surrounding_positions:
            stone = self.get_stone_at_position(i)
            if stone is not None and stone.get_color() is color:
                stones_list.append(stone)



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

    def get_surrounding_points_list(self, position):
        points_to_check = [position + self.up, position + self.left, position + self.right, position + self.down]
        return points_to_check
