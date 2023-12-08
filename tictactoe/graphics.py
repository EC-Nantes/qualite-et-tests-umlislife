import tkinter as tk

from core import Table


class GUI:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.size = 600
        self.n = 3
        self.Canvas = tk.Canvas(
            self.fenetre, width=self.size, height=self.size, bg="white"
        )
        self.table = Table(self.n)

        self.draw()

        button = tk.Button(self.fenetre, text="reset", command=self.reset)
        button.pack()

        exit_button = tk.Button(
            self.fenetre, text="Exit", command=lambda: self.fenetre.quit()
        )
        exit_button.pack()

        self.Canvas.bind("<Button-1>", self.clic)
        self.Canvas.pack()
        self.fenetre.mainloop()

    def draw(self):
        l = self.size // self.n
        for i in range(self.n - 1):
            self.Canvas.create_line((i + 1) * l, 0, (i + 1) * l, self.size * l)
            self.Canvas.create_line(0, (i + 1) * l, self.size * l, (i + 1) * l)
        for i in range(self.n):
            for j in range(self.n):
                if self.table[i, j] == 1:
                    self.Canvas.create_line(
                        l * i + 30, l * j + 30, l * i + 170, l * j + 170
                    )
                    self.Canvas.create_line(
                        l * i + 170, l * j + 30, l * i + 30, l * j + 170
                    )
                if self.table[i, j] == -1:
                    self.Canvas.create_oval(
                        i * l + 6,
                        j * l + 6,
                        (i + 1) * l - 6,
                        (j + 1) * l - 6,
                        fill="white",
                    )

    def clic(self, event):
        l = self.size // self.n
        x = int(int(event.x) // l)
        y = int(int(event.y) // l)
        self.table.play(x, y)
        self.draw()
        winner = self.table.detect_win()
        if winner != 0:
            self.table.reset()
            self.Canvas.delete("all")
            self.Canvas.create_text(
                300,
                300,
                text=f"The winner is player {'X' if winner==1 else 'O'} !",
                fill="black",
                font=("Helvetica 30 bold"),
            )

    def reset(self):
        self.Canvas.delete("all")
        self.table.reset()
        self.draw()


if __name__ == "__main__":
    GUI()
