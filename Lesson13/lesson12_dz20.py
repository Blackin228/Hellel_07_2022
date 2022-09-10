import time


class Auto(object):
    brand = None
    age = 0
    color = None
    mark = None
    weight = 0

    def __init__(self, brand, age, mark, color="black", weight=1500):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"""Brand: {self.brand}
Age: {self.age}
Color: {self.color}
Mark: {self.mark}
Weight: {self.weight}"""

    def move(self):
        print("Move")

    def stop(self):
        print("Stop")

    def birthday(self):
        self.age += 1
        print(f"Ваша машина на рік стала старшою. Її вже {self.age} років")


class Truck(Auto):
    max_load = None

    def __str__(self):
        return f"""Brand: {self.brand}
                    Age: {self.age}
                    Color: {self.color}
                    Mark: {self.mark}
                    Weight: {self.weight}
                    Max_load: {self.max_load}"""

    def __init__(self, brand, age, mark, max_load, color="black", weight=1500):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    max_speed = None

    def __str__(self):
        return f"""Brand: {self.brand}
                    Age: {self.age}
                    Color: {self.color}
                    Mark: {self.mark}
                    Weight: {self.weight}
                    Max_load: {self.max_speed}"""

    def __init__(self, brand, age, mark, max_speed, color="black", weight=1500):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


truck_1 = Truck("Scania", 3, "R425", 300000, weight=15000)
print(truck_1)
truck_1.load()
truck_1.move()
truck_1.stop()
truck_1.birthday()

print("-" * 50)

truck_2 = Truck("DAF", 4, "XF", 300000, weight=15000)
print(truck_1)
truck_2.load()
truck_2.move()
truck_2.stop()
truck_2.birthday()

print("-" * 50)

car_1 = Car("BMW", 4, "525", 220)
print(car_1)
car_1.move()
car_1.stop()
car_1.birthday()

print("-" * 50)

car_2 = Car("Audi", 5, "A5", 250)
print(car_2)
car_2.move()
car_2.stop()
car_2.birthday()
