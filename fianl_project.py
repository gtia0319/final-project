class Gomoku:
    def __init__(self, size=10):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self