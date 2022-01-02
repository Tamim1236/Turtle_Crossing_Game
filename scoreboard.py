FONT = ("Courier", 20, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.display_scoreboard()

    def display_scoreboard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.display_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)


