from turtle import Turtle
from random import randint

STAMP_SIZE = 20
SIZE = 20
INIT_MOVE = 5
UP = 0
DOWN = 1



class Ball(Turtle):

    def __init__(self, screen_width, screen_height, screen_background):
        super().__init__("circle")
        self.color("gray")
        self.penup()
        self.shapesize(SIZE / STAMP_SIZE)
        self.screen_border_x = screen_width / 2
        self.screen_border_y = screen_height / 2
        self.screen_background = screen_background  # only to recognize "transparent" blocks
        self.faceoff(reset_speed=True)


    def hit_wall(self):
        if self.xcor() >= self.screen_border_x - SIZE / 2 - 4 and (self.heading() < 90 or self.heading() > 270):
            self.setheading(180 - self.heading())
        elif self.xcor() <= -self.screen_border_x + SIZE / 2 and 90 < self.heading() < 270:
            self.setheading(180 - self.heading())
        elif self.ycor() >= self.screen_border_y - SIZE / 2:
            self.setheading(360 - self.heading())

    def check_hit_line(self):
        return self.ycor() <= -self.screen_border_y + SIZE / 2

    def hit_racket(self, racket):
        # Set random heading if hit
        racket_half_width = racket.shapesize()[1] * STAMP_SIZE // 2
        if racket.xcor() - racket_half_width - SIZE / 2 < self.xcor() < racket.xcor() + racket_half_width + SIZE / 2:
            if racket.ycor() + racket.shapesize()[0] * STAMP_SIZE // 2 >= self.ycor() - SIZE / 2:
                self.setheading(randint(20, 70) + 90 * randint(0, 1))
                return True
        return False


    def hit_block(self, blocks):
        # print(f"Block[0]: half width {blocks[0].shapesize()[1] * STAMP_SIZE // 2}, half height {blocks[0].shapesize()[0] * STAMP_SIZE // 2}")
        for block in blocks:
            if block.color()[0] == self.screen_background:
                continue
            block_half_width = block.shapesize()[1] * STAMP_SIZE // 2
            block_half_height = block.shapesize()[0] * STAMP_SIZE // 2
            if block.xcor() - block_half_width - SIZE / 2 < self.xcor() < block.xcor() + block_half_width + SIZE / 2:
                if block.ycor() + block_half_height <= self.ycor() <= block.ycor() + block_half_height + SIZE / 2:
                    self.setheading(randint(20, 70) + 90 * randint(0, 1))
                    return block
                if block.ycor() - block_half_height - SIZE / 2 <= self.ycor() <= block.ycor() - block_half_height:
                    self.setheading(randint(200, 250) + 90 * randint(0, 1))
                    return block
            if block.ycor() - block_half_height - SIZE / 2 < self.ycor() < block.ycor() + block_half_height + SIZE / 2:
                if block.xcor() + block_half_width <= self.xcor() <= block.xcor() + block_half_width + SIZE / 2:
                    self.setheading(randint(20, 70) + 270 * randint(0, 1))
                    return block
                if block.xcor() - block_half_width - SIZE / 2 <= self.xcor() <= block.xcor() - block_half_width:
                    self.setheading(randint(110, 160) + 90 * randint(0, 1))
                    return block
        return None

    def move(self):
        self.forward(self.speed)
        self.hit_wall()
        return self.check_hit_line()

    def increase_speed(self):
        self.speed += 1

    def faceoff(self, reset_speed):
        if reset_speed:
            self.speed = INIT_MOVE
        self.goto(0, SIZE - self.screen_border_y)
        self.setheading(randint(20, 70) + 90 * randint(0, 1))
        # self.init_heading(direction=direction)
