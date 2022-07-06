from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(0, 0, 0)
        self.goto(-290, 260)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Final Level: {self.level}", align="left", font=FONT)
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)