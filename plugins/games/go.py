

class Go:
    def __init__(self, way, katago=False):
        self.way = way
        self.board = [[0 for _ in range(way)] for _ in range(way)]

    def reset_board(self):
        self.board = [[0 for _ in range(self.way)] for _ in range(self.way)]

    def get_board(self):
        return self.board

    def flush_borad(self):
        pass
