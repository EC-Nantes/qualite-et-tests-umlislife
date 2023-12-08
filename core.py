import numpy as np


class Table:
    def __init__(self, n=3):
        if n < 1:
            raise ValueError("Size cannot be smaller than 1!")
        self.size = int(n)
        self.board = np.zeros((self.size, self.size))
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
        if (
            all(t[self.size - i - 1][i] == t[self.size - 1][0] for i in range(self.size))
            and t[self.size - 1][0]
        ):
            return t[self.size - 1][0]
        return 0

    def play(self, x, y):
        if x >= self.size or y >= self.size:
            raise ValueError("Coordinates given are out of bounds.")
        if self.board[x][y] != 0:
            raise ValueError("Selected cell is not empty.")
        self.board[x][y] = self.player
        self.player *= -1

    def reset(self):
        self.board = np.zeros((self.size, self.size))
        self.player = 1
