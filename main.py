from turtle import Screen
import time
from player import Player
from carmanagment import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

player = Player()
car_manager = CarManager

screen.listen()
screen.onkey(player.move_up, 'Up')



game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()










screen.exitonclick()