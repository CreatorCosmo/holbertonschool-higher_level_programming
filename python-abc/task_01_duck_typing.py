from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    An abstract base class that defines a blueprint for geometric shapes.
    
    This class should not be instantiated directly but instead used to enforce
    the implementation of the area and perimeter methods in subclasses.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        
        Returns:
        float -- The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        
        Returns:
        float -- The perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    A concrete implementation of Shape for a circle, identified by its radius.
    """
    def __init__(self, radius):
        """
        Initialize a new Circle instance with the given radius.
        
        Parameters:
        radius (float): The radius of the circle.
        """
    if radius < 0:
            raise ValueError("Radius cannot be negative")
    self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


    def area(self):
        """
        Calculate the area of the circle using the formula πr^2.
        
        Returns:
        float -- The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle using the formula 2πr.
        
        Returns:
        float -- The perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    A concrete implementation of Shape for a rectangle, identified by its width and height.
    """
    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance with the given width and height.
        
        Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle using the formula width * height.
        
        Returns:
        float -- The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle using the formula 2(width + height).
        
        Returns:
        float -- The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Prints the area and perimeter of a given shape using duck typing.
    
    Parameters:
    shape (Shape): The shape whose area and perimeter are to be printed.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Testing
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

shape_info(circle)
shape_info(rectangle)
