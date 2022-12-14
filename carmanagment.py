from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.speed_car = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_cars = Turtle('square')
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_cars.goto(300, random_y)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed_car)
        
    def level_up(self):
        self.speed_car += MOVE_INCREMENT

        