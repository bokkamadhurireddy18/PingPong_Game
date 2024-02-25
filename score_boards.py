from turtle import Turtle

ALIGNMENT = "center"
FONT= ('Arial', 40, 'normal')
class ScoreBoards(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score= 0
        self.color("white")
        self.penup()
        self.goto(pos)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"{self.score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score_board()
