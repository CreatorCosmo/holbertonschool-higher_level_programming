# Importing the necessary classes and decorators from the abc module
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    An abstract base class that defines a blueprint for animal objects.
    
    This class is not intended to be instantiated directly. It requires subclasses
    to provide implementations for the abstract methods defined within it.
    
    Methods:
    --------
    sound() : Abstract method that should be implemented by all subclasses to 
              return the sound made by the animal.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses to return the sound made by the animal.
        
        Returns:
        --------
        str
            A string representing the sound made by the animal.
        """
        pass

class Dog(Animal):
    """
    A subclass of Animal that represents a dog.
    
    This class provides a specific implementation for the sound method, returning
    the typical sound made by a dog.
    
    Methods:
    --------
    sound() : Overrides the abstract method from Animal to provide a specific 
              sound for dogs.
    """
    def sound(self):
        """
        Return the sound made by a dog.
        
        Overrides the abstract method from the Animal class.
        
        Returns:
        --------
        str
            The string 'Bark' representing the sound made by a dog.
        """
        return "Bark"

class Cat(Animal):
    """
    A subclass of Animal that represents a cat.
    
    This class provides a specific implementation for the sound method, returning
    the typical sound made by a cat.
    
    Methods:
    --------
    sound() : Overrides the abstract method from Animal to provide a specific 
              sound for cats.
    """
    def sound(self):
        """
        Return the sound made by a cat.
        
        Overrides the abstract method from the Animal class.
        
        Returns:
        --------
        str
            The string 'Meow' representing the sound made by a cat.
        """
        return "Meow"

# Testing the classes
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
