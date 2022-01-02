from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.restart()

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

    def go_left(self):
        self.setx(self.xcor() - MOVE_DISTANCE)

    def go_right(self):
        self.setx(self.xcor() + MOVE_DISTANCE)




    def restart(self):
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)


