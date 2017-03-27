from stone_color import StoneColor
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
        if self.in_bounds(position) and self.is_empty(position):
            if self.liberties_count(position) is not 0:
                self.board[position.x][position.y] = Stone(color, position)
            else:
                # place temporary stone to check if it's possible to take prisoners
                tmp_stone = Stone(color)
                self.board[position.x][position.y] = Stone(color, position)
            # continue
            hostile_stones_list = self.get_neighbors_of_color(position, StoneColor.get_opposite(color))
            if hostile_stones_list is not None:
                stones_to_be_deleted = set()
                for stone in hostile_stones_list:
                    stones_string = self.get_dead_stones_string(stone.position, stone.color)
                    if stones_string is not None:
                        stones_to_be_deleted.update(stones_string)
                for stone in stones_to_be_deleted:
                    self.delete_stone(stone.position)

            self.next_turn()

    def get_dead_stones_string(self, position, color):
        # if string doesn't have any liberties return it else return None
        string = set()
        string.add(self.get_stone_at_position(position))
        string.update(self.get_neighbors_of_color(position, color))
        count = len(string)
        if count is 0:
            return None
        new_stones = string.copy()
        while True:
            for stone in new_stones:
                liberties_count = self.liberties_count(stone.position)
                if liberties_count is not 0:
                    return None
            new_set = set()
            for stone in new_stones:
                new_set.update(self.get_neighbors_of_color(stone.position, color))
                string.update(new_set)
            new_count = len(string)
            if new_count == count:
                break
            new_stones = new_set
            count = new_count

        return string

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

        return stones_list

    @staticmethod
    def in_bounds(position):
        if 0 <= position.x < Board.size and 0 <= position.y < Board.size:
            return True
        else:
            return False

    def get_stone_at_position(self, position):
        if self.in_bounds(position):
            stone = self.board[position.x][position.y]
            if not isinstance(stone, Stone) or stone is None:
                return None
            else:
                return stone

    def get_board(self):
        return self.board

    def get_surrounding_points_list(self, position):
        points_to_check = [position + self.up, position + self.left, position + self.right, position + self.down]
        points_to_check = filter(lambda x: self.in_bounds(x), points_to_check)
        return points_to_check

    def delete_stone(self, position):
        self.board[position.x][position.y] = 0
