from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("normal")
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def move(self):
        new_x= self.xcor()+self.x_move
        new_y= self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move*= -1

    def bounce_x(self):
        self.x_move*= -1
        self.move_speed *= 0.9 #increase speed each time it gets hit by a paddle

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1 #reset speed
        self.bounce_x() #start moving in opposite direction this time.
