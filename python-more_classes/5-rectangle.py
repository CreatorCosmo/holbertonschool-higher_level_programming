#!/usr/bin/python3
""" This module contains a class
    named Rectangle
"""

class Rectangle:
    """ Class that is defining Rectangle """

    def __init__(self, width=0, height=0):
        "Initiation for rectangle"
        self.width = width
        self.height = height


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
        size = "#" * self.__width
        rect = []
        
        for index in range(self.__height):
            rect.append(size)
        return "\n".join(rect)
    
    def __repr__(self):
        " Returns representation of the rectangle "
        return"{}({}, {})".format((type(self).__name__), self.__width,
                                  self.__height)
    
    def __del__(self):
        "Deletes instance and prints message"
        print("Bye rectangle...")