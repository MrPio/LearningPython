import math


class Shape:
    index = 0

    def __init__(self) -> None:
        self.index = ++Shape.index

    def get_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius, center) -> None:
        super().__init__()
        self.radius = radius
        self.center = center

    def get_area(self) -> float:
        return self.radius ** 2 * math.pi


class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height


class Square(Rectangle):

    def __init__(self, side) -> None:
        super().__init__(side, side)
        self.side = side


class Triangle(Shape):

    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    def get_area(self) -> float:
        return self.side ** 2 * math.sin(math.radians(60)) / 2


# shape = Circle(2, (0, 0))
# shape = Rectangle(8, 4)
# shape = Square(3)
shape = Triangle(2)
print(shape.get_area())
