from  turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        retio = random.randint(1,6)
        if retio == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_axis = random.randint(-250, 250)
            new_car.goto(300, y_axis)
            self.all_cars.append(new_car)

    def car_speed(self):
            self.speed += MOVE_INCREMENT
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)