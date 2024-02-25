import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_boards import ScoreBoards
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle= Paddle((-350, 0))
r_paddle= Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

l_score= ScoreBoards((-30, 250))
r_score= ScoreBoards((60, 250))
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #top and bottom walls collision
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.xcor()>380:
        ball.reset()
        l_score.increase_score()
    if ball.xcor() < -380:
        ball.reset()
        r_score.increase_score()

    #collision with left paddle
    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        l_score.increase_score()
        l_score.update_score_board()
        ball.bounce_x()

    #collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        r_score.increase_score()
        r_score.update_score_board()
        ball.bounce_x()

screen.exitonclick()