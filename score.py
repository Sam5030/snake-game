from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.Score = 0

        with open('data.txt','r') as file:
            self.highscore =  int(file.read())

        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.write(f'Score : {self.Score}  High Score : {self.highscore}',align="center",font = ("Arial",20,"normal"))
    def reset(self):
        if self.Score > self.highscore:
            self.highscore = self.Score
            with open('data.txt','w') as file:
                file.write(str  (self.highscore))
        self.Score = 0
        self.clear()
        self.write(f'Score : {self.Score}  High Score : {self.highscore}',align="center",font = ("Arial",20,"normal"))



    def increase(self):

        self.Score+=1
        self.clear()
        self.write(f'Score : {self.Score}  High Score : {self.highscore}', align="center", font=("Arial", 20, "normal"))


