from turtle import Turtle
from random import randint

STAMP_SIZE = 20
COLORS = ["red", "orange", "yellow", "green"]
WIDTH_MIN = 2
WIDTH_STEP = 0.4
WIDTH_LIMIT = 5
WIDTH_MAX_LIMIT = WIDTH_MIN + WIDTH_STEP*WIDTH_LIMIT  # to intercept remainder of space not larger than the largest block
HEIGHT = 2
GAP = 4
START_Y = HEIGHT * 3.5 * STAMP_SIZE


class BlockManager:

    def __init__(self, screen_width, screen_height, background):
        self.background = background
        self.blocks = []
        self.transparent_blocks = 0
        for color_index in range(0, len(COLORS)):
            self.build_row(color_index=color_index, screen_width=screen_width, screen_height=screen_height)

    def build_row(self, color_index: int, screen_width: int, screen_height: int):
        start_x = -screen_width//2
        start_y = screen_height // 2 - START_Y - (HEIGHT * STAMP_SIZE + GAP) * color_index
        last2_limit = screen_width // 2 - (WIDTH_MAX_LIMIT + WIDTH_MIN) * STAMP_SIZE
        # print(f"Last 2 limit: {last2_limit}")
        # print(f"START Y: {start_y}")
        while True:  # start_x < screen_width//2:
            if start_x > last2_limit:
                self.build_last_two(start_x=start_x, start_y=start_y, limit=screen_width // 2, color_index=color_index)
                break
            block = Turtle(shape="square")
            block.color(COLORS[color_index])
            block.pensize(color_index)  # will be used to restore colors when starting new game
            width = WIDTH_MIN + WIDTH_STEP*randint(0, WIDTH_LIMIT)
            block.shapesize(stretch_wid=HEIGHT, stretch_len=width)
            block.penup()
            block.goto(start_x + width * STAMP_SIZE // 2, start_y)
            self.blocks.append(block)
            # print(f"START X: {start_x + width*SHAPE_SIZE//2}, WIDTH: {width}")
            start_x += width * STAMP_SIZE + GAP

    def build_last_two(self, start_x: int, start_y: int, limit: int, color_index: int):
        if limit - start_x <= WIDTH_MAX_LIMIT*STAMP_SIZE:  # build one fitting the remaining space
            block = Turtle(shape="square")
            block.color(COLORS[color_index])
            block.pensize(color_index)  # will be used to restore colors when starting new game
            block.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH_MAX_LIMIT)
            block.penup()
            block.goto(start_x + WIDTH_MAX_LIMIT * STAMP_SIZE // 2, start_y)
            self.blocks.append(block)
        else:  # build one min and one fitting the remaining space
            block = Turtle(shape="square")
            block.color(COLORS[color_index])
            block.pensize(color_index)  # will be used to restore colors when starting new game
            block.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH_MIN)
            block.penup()
            block.goto(start_x + WIDTH_MIN * STAMP_SIZE // 2, start_y)
            self.blocks.append(block)
            start_x += WIDTH_MIN * STAMP_SIZE + GAP
            block = Turtle(shape="square")
            block.color(COLORS[color_index])
            block.pensize(color_index)  # will be used to restore colors when starting new game
            block.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH_MAX_LIMIT)
            block.penup()
            block.goto(start_x + WIDTH_MAX_LIMIT * STAMP_SIZE // 2, start_y)
            self.blocks.append(block)

    def remove_block(self, block: Turtle) -> bool:
        # self.blocks.remove(block)
        block.color(self.background)
        self.transparent_blocks += 1
        return len(self.blocks) == self.transparent_blocks


    def restore_blocks(self):
        for block in self.blocks:
            block.color(COLORS[block.pensize()])
        self.transparent_blocks = 0



