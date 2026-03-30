from turtle import Turtle
import random
#--------------------------------#Global Constants\\
COLORS = ["red", "orange", "cyan", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 270
MOVE_INCREMENT = 0 #TAKE SPSEED FROM THE MAIN COD AT TurtleHop_V2 as "General Speed" :)
#=================================================
#=================================================

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.startup_car()
        self.shapesize(stretch_len=1.5)

    def startup_car(self):
        self.penup()
        self.shape("square")
        self.setheading(180)
        #
        self.color(random.choice(COLORS))
        #
        self.x_start_cor = random.randint(300, 1000)
        self.y_start_cor = random.randint(-230, 260)
        self.goto(self.x_start_cor, self.y_start_cor)
        #
        #--------------------------------------------
        #self.start_moving() #-->this will be taken from the while loop of the main game


    def start_moving(self):
        #_________________________________
        current_x_cor = self.xcor()
        # ------------
        self.forward(MOVE_INCREMENT + random.randint(1,10))
        #
        if current_x_cor <= -270:
            self.MOVE_INCREMENT = 60
        if current_x_cor <= -400:
            self.startup_car()


    #______________________________________________
    def remove_player(self):
        self.clear()
        self.penup()
        self.goto(900,900)
        self.setheading(0)
        self.MOVE_INCREMENT = 0
        #
        self.hideturtle()
