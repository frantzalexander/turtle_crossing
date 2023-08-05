import time

from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


#Create game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

#Initializing the player turtle
player_turtle = Player()

#Create player interactions
screen.listen()
screen.onkey(player_turtle.move_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    
    if player_turtle.ycor() > 290:
        player_turtle.reset_position()


screen.exitonclick()