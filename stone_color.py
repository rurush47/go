class StoneColor():
    EMPTY = 0
    WHITE = 1
    BLACK = 2

    enum_to_string_map= {0: 'EMPTY', 1: 'WHITE', 2: 'BLACK'}

    @staticmethod
    def get_opposite(color):
        if color is StoneColor.BLACK:
            return StoneColor.WHITE
        else:
            return StoneColor.BLACK
