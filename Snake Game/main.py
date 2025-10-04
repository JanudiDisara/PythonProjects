from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
score = Score()

screen.listen()
# The keys are case sensitive
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # range(start, stop, step)

    snake.move()

    # Detect collision with food - food size is 10x10
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    # Detect collision with a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with a tail
    for segment in snake.segments[1:]:
        # Instead of this IF, we can use slicing to say to omit the first item in list which is head
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()