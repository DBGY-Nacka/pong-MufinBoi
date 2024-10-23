from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("green")
screen.title("Klong")
screen.tracer(0)

left_paddle = Paddle((-400, 0))
right_paddle = Paddle((400, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard(0, 265)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Ball.move()


game_over = False
game_rules = {"max_points": 3, "ball_speed": 3}


def main():
    pass


if __name__ == "__main__":
    main()
