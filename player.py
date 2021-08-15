from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_back_to_start_pos()
        self.setheading(90)

    def go_up(self):
        self.goto((0, self.ycor() + MOVE_DISTANCE))

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_back_to_start_pos(self):
        self.goto(STARTING_POSITION)
