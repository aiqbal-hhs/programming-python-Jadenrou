from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("green")

### total degrees in circle = 360
### turn left must be a divisor of 360 (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90) NOTE: some divisors do not work as well
degrees = 360
turn_left = 12
total_circles = int(degrees / turn_left)
tim.pensize(3)
tim.speed(0)


def circle_colour1():
    ### choose your colour here:
    tim.pencolor("pink")
    tim.circle(-100)
    tim.left(turn_left)


def circle_colour2():
    ### choose your colour here:
    tim.pencolor("grey")
    tim.circle(-100)
    tim.left(turn_left)


for _ in range(0, int(total_circles / 2)):
    circle_colour1()
    circle_colour2()


screen = Screen()
screen.exitonclick()
