from turtle import Turtle
import random
COLORS = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.level = 1

    def car_generator(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-250, 280))
        self.cars_list.append(new_car)

    def move(self):
        speed = STARTING_MOVE_DISTANCE + (self.level - 1) * MOVE_INCREMENT
        if self.level != 0:
            for car in self.cars_list:
                car.forward(speed)

    def car_popper(self):
        for car in self.cars_list:
            if car.xcor() <= -300:
                car.hideturtle()
                self.cars_list.remove(car)