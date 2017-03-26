from Color import Color


class TurnManager:
    def __init__(self):
        self.current_turn = Color.BLACK

    def next_turn(self):
        self.current_turn = Color.WHITE if self.current_turn == Color.BLACK else self.current_turn = Color.BLACK

    def get_current_player_color(self):
        return self.current_turn
