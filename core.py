import numpy as np

class Table:
    def __init__(self, n=3):
        self.size = n
        self.board = np.zeros((n, n))
        self.player = 1

    def detect_win(self):
        t = self.board
        # Lignes
        for i in range(self.size):
            if all(t[i][j] == t[i][0] for j in range(self.size)) and t[i][0] != 0:
                return t[i][0]
        # Colonnes
        for j in range(self.size):
            if all(t[i][j] == t[0][j] for i in range(self.size)) and t[0][j] != 0:
                return t[0][j]
        # Diagonales
        if all(t[i][i] == t[0][0] for i in range(self.size)) and t[0][0]:
            return t[0][0]
        if all(t[self.size-i-1][i] == t[self.size-1][0] for i in range(self.size)) and t[self.size-1][0]:
            return t[self.size-1][0]
        return 0

    def play(self, x, y):
        pass
