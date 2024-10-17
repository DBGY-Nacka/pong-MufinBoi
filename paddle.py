from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        pass


left_pad = Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
