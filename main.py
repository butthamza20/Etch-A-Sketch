from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()


def forwards():
    tim.forward(50)


def backwards():
    tim.backward(50)


def anti_clock():
    tim.left(45)


def clock():
    tim.right(45)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="b", fun=backwards)
screen.onkey(key="a", fun=anti_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
