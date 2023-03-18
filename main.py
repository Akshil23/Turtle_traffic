import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle-Traffic")
screen.tracer(0)

t = Player()
car = CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(t.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.start_moving()
    score.update_scoreboard()
    for cars in car.all_cars:
        if cars.distance(t) < 30:
            game_is_on = False
            score.game_over()

    if t.is_at_finish_line():
        t.reset()
        score.increase_level()
        car.level_up()

    screen.update()
screen.exitonclick()
