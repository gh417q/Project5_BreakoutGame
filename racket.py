from turtle import Turtle

STAMP_SIZE = 20
WIDTH = 10
HEIGHT = 0.5
COLOR = "skyBlue"
GAP = 25
STEP = 50



class Racket(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__("square")
        self.penup()
        self.color(COLOR)
        self.setheading(0)
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.screen_width = screen_width
        self.initial_location(screen_height=screen_height)

    def initial_location(self, screen_height):
        self.goto(0, -screen_height / 2 + GAP)

    def move_right(self):
        if self.xcor() < (self.screen_width - WIDTH*STAMP_SIZE)/ 2:
            self.forward(STEP)

    def move_left(self):
        if self.xcor() > (WIDTH*STAMP_SIZE - self.screen_width) / 2:
            self.backward(STEP)
