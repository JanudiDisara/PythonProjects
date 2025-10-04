import turtle as turtle_module

tim = turtle_module.Turtle()
screen = turtle_module.Screen()

def forward():
    tim.forward(50)

def backward():
    tim.backward(50)

def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # OR tim.left(10)

def clockwise():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun = forward, key = "w")
screen.onkey(fun = forward, key = "s")
screen.onkey(fun = counter_clockwise, key = "a")
screen.onkey(fun = clockwise, key = "d")
screen.onkey(fun = clear_drawing, key = "c")

screen.exitonclick()