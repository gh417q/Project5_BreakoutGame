from turtle import Screen
from block_manager import BlockManager
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

WIDTH = 1000
HEIGHT = 600
SLEEP = 0.01
PAUSE = 2
BACKGROUND_COLOR = "black"

game_on = True

def stop_game():
    global game_on
    game_on = False

def reset_game():
    sleep(PAUSE*2)
    scoreboard.reset_score()
    block_manager.restore_blocks()
    ball.faceoff(reset_speed=True)
    pad.initial_location(screen_height=HEIGHT)


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Breakout")
screen.tracer(0)

block_manager = BlockManager(screen_width=WIDTH, screen_height=HEIGHT, background=BACKGROUND_COLOR)
pad = Racket(screen_width=WIDTH, screen_height=HEIGHT)
ball = Ball(screen_width=WIDTH, screen_height=HEIGHT, screen_background=BACKGROUND_COLOR)
scoreboard = Scoreboard(screen_height=HEIGHT)
screen.update()

screen.listen()
screen.onkey(pad.move_right, "Right")
screen.onkey(pad.move_left, "Left")
screen.onkey(stop_game, "p")
# screen.onkey(new_game, "n")

while game_on:
    sleep(SLEEP)
    if ball.move():  # True if hit screen bottom line
        if scoreboard.lost_ball():  # no balls left if True
            screen.update()
            reset_game()
        else:
            sleep(PAUSE)
            ball.faceoff(reset_speed=False)
            pad.initial_location(screen_height=HEIGHT)
    else:
        if not ball.hit_racket(racket=pad):
            block = ball.hit_block(block_manager.blocks)
            if block is not None:
                if block_manager.remove_block(block):
                    scoreboard.game_over()
                    screen.update()
                    reset_game()
                else:
                    if scoreboard.scored():
                        ball.increase_speed()
    screen.update()

screen.exitonclick()
