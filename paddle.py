from turtle import Turtle
DISTANCE= 20
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.goto(pos)

    def up(self):
        self.forward(DISTANCE)
    def down(self):
        self.backward(DISTANCE)

