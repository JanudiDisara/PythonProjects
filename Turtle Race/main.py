from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_loop in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    # If screen width is 500, then the leftmost point is -250, center is 0 and rightmost is 250.
    # If screen height is 400, then the highest point is 200, center is 0 and the lowest is -200.
    new_turtle.penup()
    new_turtle.color(colors[turtle_loop])
    new_turtle.goto(x = -230, y = y_positions[turtle_loop])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
    # For turtle to reach end it will be 250. But turtle is 40x40. So 250-(40/2) = 230
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()