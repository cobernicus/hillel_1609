from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def get_area(self):
        s = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(s * (s - self.__side_a) * (s - self.__side_b) * (s - self.__side_c))

    def get_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

# Creating shape objects
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

# Shapes in a list
figures = [circle, rectangle, triangle]

# Calculating and printing the area and perimeter of each shape
for figure in figures:
    print(f"Shape: {type(figure).__name__}")
    print(f"Area: {figure.get_area()}")
    print(f"Perimeter: {figure.get_perimeter()}")
    print("------------")
