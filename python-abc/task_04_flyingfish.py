"""
This Python module defines three classes that demonstrate
 the concept of multiple inheritance. It includes classes 
 representing Fish, Bird, and a hybrid FlyingFish 
 that inherits behaviors from both parent classes.
"""
class Fish:
    """
    The Fish class represents generic fish behavior,
    focusing on swimming and their habitat in water.
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
    The Bird class represents generic bird behavior,
    focusing on flying and their habitat in the sky.
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
        """
        The FlyingFish class combines the characteristics
        of both Fish and Bird through multiple inheritance.
        It overrides certain behaviors.
        """
        def fly(self):
            print("The flying fish is soaring!")

        def swim(self):
            print("The flying fish is swimming!")

        def habitat(self):
            print("The flying fish lives both in water and the sky!")

if __name__ == "__main__":
    """
    The class testing and MRO exploration help understand 
    how the methods are resolved when an instance of 
    FlyingFish is utilized, showcasing the method 
    lookup order due to multiple inheritance.
    """
    
    flying_fish = FlyingFish()
    
    flying_fish.fly()       # Outputs: The flying fish is soaring!
    flying_fish.swim()      # Outputs: The flying fish is swimming!
    flying_fish.habitat()   # Outputs: The flying fish lives both in water and the sky!
    
    # Investigate the Method Resolution Order (MRO)
    print(FlyingFish.mro()) # Prints the MRO list showing the order of method resolution
