class Car:
    def __init__(self, brand : str, color : str, speed : int):
        self.brand = brand
        self.color = color
        self.speed = speed

    def __str__(self):
        return f"a {self.color} {self.brand}"

    def change_color(self, new_color : str):
        self.color = new_color


volovo1 = Car("volvo", "black", 2000)
print(volovo1.color)
volovo1.change_color("white")
print(volovo1)