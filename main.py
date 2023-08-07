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


player_turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Create player interactions
screen.listen()
screen.onkey(player_turtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    #Detect Car Collision
    for car in car_manager.all_cars:
        if car.distance(player_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    #Detect a successful Crossing
    if player_turtle.is_at_finish_line():
        player_turtle.reset_position()
        car_manager.car_level_up()
        scoreboard.increase_level()


screen.exitonclick()