#!/usr/bin/python3
""" This module contains a class
    named Rectangle
"""

class Rectangle:
    """ Class that is defining Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        "Initiation for rectangle"
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        "Property to retrieve the width"
        return self.__width
    
    @width.setter
    def width(self, value):
        "Property to set the width"
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        
        elif value < 0:
            raise TypeError('width must be >= 0')
        else:
            self.__width = value
    
    @property
    def height(self):
        "Property to retrieve height"
        return self.__height
    
    @height.setter
    def height (self, value):
        "Property to set the heigth"
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise TypeError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        "Public instance that returns area"
        return self.width * self.height
    
    def perimeter(self):
        "Public instance that returns perimeter"
        if self.height and self.width == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        rect = ""
        if self.height == 0 or self.width == 0:
            return ""
        size = str(self.print_symbol) * self.__width
        rect = []
        
        for index in range(self.__height):
            rect.append(size)
        return "\n".join(rect)
    
    def __repr__(self):
        " Returns representation of the rectangle "
        return"{:s}({:d}, {:d})".format((type(self).__name__), self.__width,
                                  self.__height)
    
    def __del__(self):
        "Deletes instance and decreases instance count"
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the larger rectangle after comparing"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        """initializes a new square instance"""
        return cls(size, size)