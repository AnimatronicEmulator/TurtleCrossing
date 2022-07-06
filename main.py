import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

frogger = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=frogger.move)
count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate another car approximately every 0.6 seconds
    if count % 6 == 0:
        cars.car_generator()
    count += 1

    # Get cars to perpetually move and delete "old" cars
    cars.move()
    cars.car_popper()

    # Level incrementing
    if frogger.ycor() >= frogger.finish_line_y:
        frogger.player_reset()
        cars.level += 1
        scoreboard.level += 1
        scoreboard.update()

    # Frogger collision with cars check
    for car in cars.cars_list:
        if frogger.distance(car) < 30:
            if abs(frogger.ycor() - car.ycor()) < 20:
                cars.level = 0
                scoreboard.game_over()
                game_is_on = False

screen.exitonclick()
