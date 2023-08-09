# Turtle Crossing Game

## Project Overview
The player controls a turtle and the goal is to successfully navigate the turtle across the field of cars.

## Objectives
- Create the game screen
- Create the player turtle
- Set up the player turtle with the ability to move forward on the "Up" key press
- Create the randomly appearing cars
- Detect collision with the player turtle
- Detect when the player turtle successfully crosses the game field
- Create the scoreboard that updates when the player is successful
- Cars increases speed based on the game level.

## Results

Example Game User Interface


![image](https://github.com/frantzalexander/turtle_crossing/assets/128331579/71462f16-285e-41e2-b542-c3f47db7ca10)

## Process 
The project is divided into four modules:


- Player Module

- Car Management Module


 - Scoreboard Module


 - Main Game Module

### Flowchart
```mermaid
flowchart TD
start(((START)))
player{Player Module}
car{Car Module}
scoreboard{Scoreboard Module}
main_game{Main Game Module}
player_attr[Define: Shape, Colour & Starting Position]
player_move[Set Player Forward Movement]
player_reset[Set Player Reset Position]
player_crossing[Detect Player Crossing]
car_attr[Define List of Cars & Starting Speed]
create_car[Create Each Car]
set_car[Set Car Movement Speed]
level_up_speed[Set Car Level Up Speed Increment]
scoreboard_attr[Set the Scoreboard Text, Font & Positioning]
scoreboard_update[Setup Update Screen for Scoreboard]
game_over[Set Game Over Screen]
game_screen[Setup Game Screen]
game_conditions[Setup Game Conditions]
game_level_up[Detect Player Crossing & Apply Level Up Screen]
game_over_screen[Detect Player Collision & Apply Game Over Screen]
end_game(((END))) 
start --> player
start --> car
start --> scoreboard
player --> player_attr
player_attr --> player_move
player_move --> player_reset
player_reset --> player_crossing
car --> car_attr
car_attr --> create_car
create_car --> set_car
set_car --> level_up_speed
scoreboard --> scoreboard_attr
scoreboard_attr --> scoreboard_update
scoreboard_update --> game_over
game_over --> main_game
player_crossing --> main_game
level_up_speed --> main_game
main_game --> game_screen
game_screen --> game_conditions
game_conditions --> game_level_up
game_level_up --> game_over_screen
game_over_screen --> end_game
