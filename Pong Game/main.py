from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Score()

# Track which keys are pressed
keys_pressed = set()

def key_down(key):
    keys_pressed.add(key)

def key_up(key):
    if key in keys_pressed:
        keys_pressed.remove(key)

screen.listen()
screen.onkeypress(lambda: key_down("Up"), "Up")
screen.onkeyrelease(lambda: key_up("Up"), "Up")
screen.onkeypress(lambda: key_down("Down"), "Down")
screen.onkeyrelease(lambda: key_up("Down"), "Down")
screen.onkeypress(lambda: key_down("w"), "w")
screen.onkeyrelease(lambda: key_up("w"), "w")
screen.onkeypress(lambda: key_down("s"), "s")
screen.onkeyrelease(lambda: key_up("s"), "s")

def update_paddles():
    if "Up" in keys_pressed:
        r_paddle.go_up()
    if "Down" in keys_pressed:
        r_paddle.go_down()
    if "w" in keys_pressed:
        l_paddle.go_up()
    if "s" in keys_pressed:
        l_paddle.go_down()
    screen.ontimer(update_paddles, 20)

update_paddles()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision of the wall - Height goes from -300 TO 0 TO 300 since height of screen is 600
    # 280 because ball size is 20x20
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the right paddle
    # The distance of ball is measured from center of paddle. So if ball is near top of paddle, distance is not 20, will be higher.
    # Therefore, we use an approximate of 50.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect when right paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()