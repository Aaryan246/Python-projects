from turtle import Turtle

class Pong(Turtle):
    def __init__(self,X,Y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5,1)
        self.color("white")
        self.setpos(X,Y)

    def up(self):
        x = self.xcor()
        y = self.ycor() + 20
        self.goto(x,y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        self.goto(x,y)