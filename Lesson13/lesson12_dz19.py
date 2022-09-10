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


auto_1 = Auto("BMW", 4, "525")
auto_1.move()
auto_1.stop()
print(auto_1)
auto_1.birthday()
