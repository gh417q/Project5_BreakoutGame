from turtle import Turtle

STYLE = ('Courier', 16, 'bold')
ALIGN = "center"
INIT_BALLS = 4


class Scoreboard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.penup()
        self.goto(0, int(screen_height / 2) - 40)
        self.hideturtle()
        self.reset_score()

    def show_score(self):
        self.clear()
        self.write(f"Balls left: {self.balls}    Score: {self.score}", font=STYLE, align=ALIGN)


    def lost_ball(self) -> bool:
        self.balls -= 1
        self.show_score()
        if self.balls == 0:
            self.clear()
            self.write(f"No balls left!    Score: {self.score}", font=STYLE, align=ALIGN)
            return True
        return False


    def scored(self) -> bool:
        self.score += 1
        self.show_score()
        return self.score%10 == 0


    def game_over(self):
        self.clear()
        self.color("orange")
        self.write(f"You win!  Score: {self.score},  balls lost: {INIT_BALLS - self.balls}.", font=STYLE, align=ALIGN)


    def reset_score(self):
        self.color("lightGray")
        self.score = 0
        self.balls = INIT_BALLS
        self.show_score()
