from turtle import Turtle

#--------------------------------#Global Constants\\
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 320
#
WON = False
#=================================================

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        #
        self.shape("turtle")
        self.color("green")

    #______________________________________________
    def restart_player(self):
        super().__init__()
        self.clear()
        #
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        #
        self.shape("turtle")
        self.color("green")

    #______________________________________________
    def move_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if self.ycor() > -290:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)
