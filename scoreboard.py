from turtle import Turtle, left

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto((-280, 270))
        self.write(f"Level {self.level}", align="left", font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def gameover(self):
        self.goto((0, 0))
        self.clear()
        self.write(f"GAMEOVER", align="center", font=FONT)
