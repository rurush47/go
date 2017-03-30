from stone_color import StoneColor


class TurnManager:
    def __init__(self):
        self.current_turn = StoneColor.BLACK
        self.pass_counter = 0

    def next_turn(self):
        self.switch_player()
        self.pass_counter = 0

    def switch_player(self):
        if self.current_turn is StoneColor.BLACK:
            self.current_turn = StoneColor.WHITE
        else:
            self.current_turn = StoneColor.BLACK

    def pass_turn(self):
        self.switch_player()
        self.pass_counter += 1

    def get_current_player_color(self):
        return self.current_turn
