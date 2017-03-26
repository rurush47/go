from stone_color import StoneColor


class TurnManager:
    def __init__(self):
        self.current_turn = StoneColor.BLACK

    def next_turn(self):
        if self.current_turn is StoneColor.BLACK:
            self.current_turn = StoneColor.WHITE
        else:
            self.current_turn = StoneColor.BLACK

    def get_current_player_color(self):
        return self.current_turn
