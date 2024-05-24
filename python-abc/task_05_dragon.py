class SwimMixin:
    """
    Mixin class providing swimming behavior.
    """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """
    Mixin class providing flying behavior.
    """
    def fly(self):
        print("The creature flies!")
class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits behaviors from SwimMixin and FlyMixin.
    This class demonstrates the ability of a dragon to swim, fly, and roar.
    """
    def roar(self):
        print("The dragon roars!")

# Instantiate the Dragon
draco = Dragon()

# Demonstrate Draco's abilities
draco.swim()    # Output: The creature swims!
draco.fly()     # Output: The creature flies!
draco.roar()    # Output: The dragon roars!
