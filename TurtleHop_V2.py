import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
import tkinter as tk
#--------------------------------#
from player import FINISH_LINE_Y
#--------------------------------#
from scoreboard import Scoreboard
#--------------------------------#
TRAFFIC_STATE = 0
CARS = []
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@important:
GENERAL_SPEED = 10
car_manager.MOVE_INCREMENT = GENERAL_SPEED
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#=================================================SCREEN SETUP:
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Hop v2.0  -  Dr.M-Dev")
#
game_starts = True
if game_starts:
    try:
        screen.bgpic("HighWay_Background.png")
    except FileNotFoundError: #for file not found
        screen.bgcolor("white")
    except tk.TclError: #for file not found
        screen.bgcolor("white")

#=================================================GAME SETUP:
#_____________________
the_level_counter = Scoreboard()
the_level_counter.current_level = 1
#
the_turtle = Player()
cars_WAVE = [] #GLOBAL

# _____________________#_____________________#_____________________#
def increase_difficulty():
    global cars_WAVE
    global game_is_on
    global GENERAL_SPEED
    ################
    # =============================
    the_turtle.hideturtle()
    the_turtle.restart_player()
    game_is_on = True
    # ~~~~~~~~~~~~~~~#
    # level-2
    the_level_counter.print_level()
    # ++++++++
    for old_cars in cars_WAVE:
        old_cars.hideturtle()
    # ++++++++
    cars_WAVE.clear()
    #======================================================
    #INCREASE SPEED:
    GENERAL_SPEED += 2
    car_manager.MOVE_INCREMENT = GENERAL_SPEED
    print(GENERAL_SPEED)
    #__________________
    # INCREASE CARS:
    for _ in range(2, 20):#the_level_counter.current_level):
        cars = CarManager()
        cars_WAVE.append(cars)

#_________________________________
def level_setup():
    global cars_WAVE
    global game_is_on
    car_number = 0 #DEBUG
    ################
    if the_level_counter.current_level == 1:
        #level-1
        the_level_counter.print_level()
        #++++++++
        cars_WAVE = []
        for _ in range(10,20):
            cars = CarManager()
            cars_WAVE.append(cars)
            # print(f"CAR GENERATED-{car_number}")  # DEBUG
            car_number +=1  #DEBUG
    #=======================================
    if the_level_counter.current_level > 1:
        increase_difficulty()
    # _____________________#_____________________#_____________________#

def game_over():
    global cars_WAVE
    global game_is_on
    ################
    # =============================
    the_turtle.hideturtle()
    # ~~~~~~~~~~~~~~~#
    for old_cars in cars_WAVE:
        old_cars.remove_player()
    # ++++++++
    cars_WAVE.clear()
    ## =============================
    if 1>0:
        try:
            screen.bgpic("GameOver_Background.png")
        except FileNotFoundError:  # for file not found
            screen.bgcolor("red")
        except tk.TclError:  # for file not found
            screen.bgcolor("red")
    ## =============================
    # game_is_on = False #case the remaining cars to stay visible



#####################__________CAR WAVES:
#____________________Player Controls
screen.listen()
screen.onkeypress(key="w", fun=the_turtle.move_forward)
screen.onkeypress(key="Up", fun=the_turtle.move_forward)
#
screen.onkeypress(key="s", fun=the_turtle.move_backward)
screen.onkeypress(key="Down", fun=the_turtle.move_backward)



#=================================================MAIN CODE:
game_is_on = True
level_setup()#only for the first time (startup) :)
#################
while game_is_on:
    # global cars_WAVE
    # global current_level #MAIN-WHILE LOOPS on first indentation, doesn't require any global-declaration
    ###############
    time.sleep(0.1)
    screen.update()
    #______________________________________
    for generated_cars in cars_WAVE:
        generated_cars.start_moving()
        # print("Car Moves")#DEBUG
        #______________________________________losing_condition
        if the_turtle.distance(generated_cars) < 10:
            # print("YOU LOSE")  # DEBUG
            # generated_cars.hideturtle()
            # game_is_on = False
            # ++++++++
            game_over()

    #______________________________________winning_condition
    if the_turtle.ycor() >= FINISH_LINE_Y:
        the_level_counter.current_level += 1
        # print("YOU WON!!")  # DEBUG
        the_turtle.hideturtle()
        game_is_on = False
        #RESTART:
        level_setup()

#=================================================Keeping The Game On:
screen.mainloop()
