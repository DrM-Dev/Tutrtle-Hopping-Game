from turtle import Turtle
#--------------------------------#Global Constants\\
FONT = ("Courier", 20, "bold")
#=================================================

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        #
        self.penup()
        self.hideturtle()
        #
        self.color("black")
        self.goto(-250,265)

    def print_level(self):
        self.clear()
        self.goto(-250, 265)
        self.hideturtle()
        #--------------#
        self.write(f"LEVEL {self.current_level}", font=FONT)
