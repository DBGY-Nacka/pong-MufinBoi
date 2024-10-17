from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# din screen bör vara rektanguljär, ex. 800x600

Screen = Screen()
Screen.setup(700, 700)
Screen.bgcolor("green")
Screen.title("Klong")
Screen.tracer(0)

if __name__ == "__main__":
    game_is_on = True
    paddle = Paddle()
    ball = Ball()
    scoreboard = Scoreboard()

    while game_is_on:
        # Update screen and move every tick.
        Screen.update()
        time.sleep(0.1)


def main():
    pass


if __name__ == "__main__":
    main()
