import copy

from state_history import StateHistory
from stone_color import StoneColor
from turn_manager import TurnManager
from vector2 import Vector2


class Board:
    size = 6

    up = Vector2(0, 1)
    down = Vector2(0, -1)
    right = Vector2(1, 0)
    left = Vector2(-1, 0)

    def __init__(self):
        # create 2D array
        self.board = [[0 for i in range(Board.size)] for j in range(Board.size)]
        self.turn_manager = TurnManager()
        self.state_history = StateHistory()
        self.state_history.add_state(self.create_state())

    def make_move(self, position):
        color = self.turn_manager.get_current_player_color()
        if position is None:
            self.turn_manager.pass_turn()
            if self.turn_manager.pass_counter >= 2:
                self.end_game()
            return 'you passed'
        state_after_move = self.get_state(position, color)
        if state_after_move is None:
            return 'invalid move'
        # If the current board state is valid, add it to the history of states.
        self.state_history.add_state(state_after_move)
        self.next_turn()
        return None

    # returns None if move is invalid else returns state after correct move
    def get_state(self, position, color):
        if self.in_bounds(position) and self.is_empty(position):
            # Place a stone on any unoccupied space.
            self.board[position.x][position.y] = color
            # Check if any opposing groups are completely surrounded. If so, remove them and mark them as captured.
            hostile_stones_list = self.get_neighbors_of_color(position, StoneColor.get_opposite(color))
            if hostile_stones_list is not None:
                stones_to_be_deleted = set()
                for stone in hostile_stones_list:
                    stones_string = self.get_stones_string(stone, StoneColor.get_opposite(color))
                    if stones_string is not None and self.is_string_dead(stones_string):
                        stones_to_be_deleted.update(stones_string)
                for stone in stones_to_be_deleted:
                    self.delete_stone(stone)
            # Check if any friendly groups are completely surrounded. If so, the move is invalid.
            # Check if the current board state is in the history of states for this game. If so, the move is invalid.
            # 'ko' rule
            state = self.create_state()
            friendly_string = self.get_stones_string(position, color)
            if friendly_string is None or self.is_string_dead(friendly_string) \
                    or self.state_history.is_already_in_history(state):
                self.load_last_state()
                return None
            return state
        return None

    def load_last_state(self):
        self.board = copy.deepcopy(self.state_history.get_last_state())

    def get_stones_string(self, position, color):
        # if string doesn't have any liberties return it else return None
        string = set()
        string.add(position)
        string.update(self.get_neighbors_of_color(position, color))
        count = len(string)
        if count is 0:
            return None
        new_stones = string.copy()
        while True:
            new_set = set()
            for stone in new_stones:
                new_set.update(self.get_neighbors_of_color(stone, color))
                string.update(new_set)
            new_count = len(string)
            if new_count == count:
                break
            new_stones = new_set
            count = new_count

        return string

    def is_string_dead(self, string):
        for stone in string:
            liberties_count = self.liberties_count(stone)
            if liberties_count is not 0:
                return False
        return True

    def next_turn(self):
        self.turn_manager.next_turn()

    def is_empty(self, position):
        return True if self.board[position.x][position.y] == StoneColor.EMPTY else False

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
            if self.board[i.x][i.y] is color:
                stones_list.append(i)
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
            if stone is not StoneColor.EMPTY:
                return stone
            else:
                return None

    def get_board(self):
        return self.board

    def get_surrounding_points_list(self, position):
        points_to_check = [position + self.up, position + self.left, position + self.right, position + self.down]
        points_to_check = filter(lambda x: self.in_bounds(x), points_to_check)
        return points_to_check

    def delete_stone(self, position):
        self.board[position.x][position.y] = 0

    def reverse_removal(self, stones):
        for stone in stones:
            pos = stone.position
            self.board[pos.x][pos.y] = stone

    def create_state(self):
        state = copy.deepcopy(self.board)
        return state

    def end_game(self):
        pass

    def count_score(self):
        white_score = 0
        black_score = 0
        for i in range(Board.size):
            for j in range(Board.size):
                stone = self.board[i][j]
                if stone is StoneColor.WHITE:
                    white_score += 1
                elif stone is StoneColor.BLACK:
                    black_score += 1
        return [black_score, white_score]

    def valid_states_generator(self, color):
        for i in range(Board.size):
            for j in range(Board.size):
                position = Vector2(i, j)
                state = self.get_state(position, color)
                self.load_last_state()
                if state is not None:
                    yield [position, state]
