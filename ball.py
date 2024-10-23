import turtle

ball = turtle.Turtle


class Ball(turtle):
    def __init__(self):
        super().__init__()
        self.speed(40)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)


hit_ball = ball()

while True:
    hit_ball.move()
