import time
from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

l_pong = Pong(-350,0)
r_pong = Pong(350,0)
screen.listen()
screen.onkey(r_pong.up,key="Up")
screen.onkey(r_pong.down,key="Down")
screen.onkey(l_pong.up,key="w")
screen.onkey(l_pong.down,key="s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <=-280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_pong) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_pong) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect out of bounds
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()