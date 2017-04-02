import copy

from state_history import StateHistory
from stone_color import StoneColor
from turn_manager import TurnManager
from vector2 import Vector2


class Board:
    size = 19

    up = Vector2(0, 1)
    down = Vector2(0, -1)
    right = Vector2(1, 0)
    left = Vector2(-1, 0)

    def __init__(self):
        # create 2D array
        self.board = [[0 for i in range(Board.size)] for j in range(Board.size)]
        self.turn_manager = TurnManager()
        self.state_history = StateHistory()
        self.state_history.add_state(self.create_state(self.board))

    def make_move(self, position):
        color = self.turn_manager.get_current_player_color()
        if position is None:
            self.turn_manager.pass_turn()
            if self.turn_manager.pass_counter >= 2:
                self.end_game()
            return 'you passed'
        state_after_move = self.get_state(self.board, position, color, self.state_history.get_state_list())
        if state_after_move is None:
            self.load_last_state()
            return 'invalid move'
        # If the current board state is valid, add it to the history of states.
        self.board = state_after_move
        self.state_history.add_state(state_after_move)
        self.next_turn()
        return None

    # returns None if move is invalid else returns state after correct move
    @staticmethod
    def get_state(state, position, color, previous_states):
        if Board.in_bounds(state, position) and Board.is_empty(state, position):
            # Place a stone on any unoccupied space.
            state[position.x][position.y] = color
            # Check if any opposing groups are completely surrounded. If so, remove them and mark them as captured.
            hostile_stones_list = Board.get_neighbors_of_color(state, position, StoneColor.get_opposite(color))
            if hostile_stones_list is not None:
                stones_to_be_deleted = set()
                for stone in hostile_stones_list:
                    stones_string = Board.get_stones_string(state, stone, StoneColor.get_opposite(color))
                    if stones_string is not None and Board.is_string_dead(state, stones_string):
                        stones_to_be_deleted.update(stones_string)
                for stone in stones_to_be_deleted:
                    Board.delete_stone(state, stone)
            # Check if any friendly groups are completely surrounded. If so, the move is invalid.
            # Check if the current board state is in the history of states for this game. If so, the move is invalid.
            # 'ko' rule
            state = Board.create_state(state)
            friendly_string = Board.get_stones_string(state, position, color)
            if friendly_string is None or Board.is_string_dead(state, friendly_string) \
                    or state in previous_states:
                return None
            return state
        return None

    def load_last_state(self):
        self.board = copy.deepcopy(self.state_history.get_last_state())

    @staticmethod
    def get_stones_string(state, position, color):
        # if string doesn't have any liberties return it else return None
        string = set()
        string.add(position)
        string.update(Board.get_neighbors_of_color(state, position, color))
        count = len(string)
        if count is 0:
            return None
        new_stones = string.copy()
        while True:
            new_set = set()
            for stone in new_stones:
                new_set.update(Board.get_neighbors_of_color(state, stone, color))
                string.update(new_set)
            new_count = len(string)
            if new_count == count:
                break
            new_stones = new_set
            count = new_count

        return string

    @staticmethod
    def is_string_dead(state, string):
        for stone in string:
            liberties_count = Board.liberties_count(state, stone)
            if liberties_count is not 0:
                return False
        return True

    def next_turn(self):
        self.turn_manager.next_turn()

    @staticmethod
    def is_empty(state, position):
        return True if state[position.x][position.y] == StoneColor.EMPTY else False

    @staticmethod
    def liberties_count(state, position):
        count = 0

        points_to_check = Board.get_surrounding_points_list(state, position)

        for i in points_to_check:
            if Board.in_bounds(state, i) and Board.is_empty(state, i):
                count += 1

        return count

    @staticmethod
    def get_neighbors_of_color(state, position, color):
        stones_list = []
        surrounding_positions = Board.get_surrounding_points_list(state, position)

        for i in surrounding_positions:
            if state[i.x][i.y] is color:
                stones_list.append(i)
        return stones_list

    @staticmethod
    def in_bounds(state, position):
        if 0 <= position.x < len(state) and 0 <= position.y < len(state):
            return True
        else:
            return False

    @staticmethod
    def get_stone_at_position(state, position):
        if Board.in_bounds(state, position):
            stone = state[position.x][position.y]
            if stone is not StoneColor.EMPTY:
                return stone
            else:
                return None

    def get_board(self):
        return self.board

    @staticmethod
    def get_surrounding_points_list(state, position):
        points_to_check = [position + Vector2(0, 1), position + Vector2(-1, 0),
                           position + Vector2(1, 0), position + Vector2(0, -1)]
        points_to_check = filter(lambda x: Board.in_bounds(state, x), points_to_check)
        return points_to_check

    @staticmethod
    def delete_stone(state, position):
        state[position.x][position.y] = 0

    @staticmethod
    def create_state(state):
        new_state = copy.deepcopy(state)
        return new_state

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

    @staticmethod
    def valid_states_generator(state, color, previous_states):
        for i in range(Board.size):
            for j in range(Board.size):
                position = Vector2(i, j)
                state = Board.get_state(state, position, color, previous_states)
                if state is not None:
                    yield [position, state]
