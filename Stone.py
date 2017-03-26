class Stone:
    def __init__(self, color):
        self.color = color
        self.to_be_deleted = False

    def get_color(self):
        return self.color
