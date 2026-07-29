class Polygon:
    def __init__(self, sides: int):
        self.sides = sides

    def describe(self):
        print(f"I'm a polygon with {self.sides} sides")


class Rectangle(Polygon):
    def __init__(self, length: float, breadth: float):
        super().__init__(sides=4)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Square(Rectangle):
    def __init__(self, length: float):
        super().__init__(length=length, breadth=length)




rect = Rectangle(40, 20)
print(rect.area())
print(rect.describe())

sqr = Square(10)
print(sqr.area())
print(sqr.perimeter())
sqr.describe()