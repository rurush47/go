from aenum import Enum


class StoneColor(Enum):
    WHITE = 1
    BLACK = 2

    @staticmethod
    def get_opposite(color):
        if color is StoneColor.BLACK:
            return StoneColor.WHITE
        else:
            return StoneColor.BLACK
