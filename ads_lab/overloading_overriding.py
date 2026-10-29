# 3: Method Overloading and Method Overriding

# ------ For Execution --------
# cd ads_lab 
# pwd
# python overloading_overriding.py


import math

class Shape:
    def area(self, *dimensions):
        if len(dimensions) == 1:
            radius = dimensions[0]
            return math.pi * radius ** 2
        elif len(dimensions) == 2:
            length, width = dimensions
            return length * width
        elif len(dimensions) == 3:
            a, b, c = dimensions
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        else:
            raise ValueError("area() supports 1, 2, or 3 dimensions only.")
        
    def describe(self) -> str:
        """Default description; subclasses OVERRIDE this method."""
        return "I am a generic shape."
    
class Circle(Shape):
    """A circle - overrides describe() from Shape."""
    def __init__(self, radius: float):
        self.radius = radius
    def describe(self) -> str:
        """Override: provide a circle-specific description."""
        return f"I am a Circle with radius {self.radius} and area {self.area(self.radius):.2f}."

class Rectangle(Shape):
    """A rectangle - overrides describe() from Shape."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    def describe(self) -> str:
        """Override: provide a rectangle-specific description."""
        return (f"I am a Rectangle {self.length}x{self.width} "
                f"with area {self.area(self.length, self.width):.2f}.")

def main():
    """Demonstrate both overloading (via *args) and overriding (via subclasses)."""
    print("=== Method Overloading Demo (single area() method, variable args) ===")
    shape = Shape()
    print(f"area(5) -> circle area : {shape.area(5):.2f}")
    print(f"area(4, 6) -> rectangle area : {shape.area(4, 6):.2f}")
    print(f"area(3, 4, 5) -> triangle area : {shape.area(3, 4, 5):.2f}")
    print("\n=== Method Overriding Demo (subclasses override describe()) ===")
    shapes = [Shape(), Circle(5), Rectangle(4, 6)]
    for s in shapes:
        # The SAME method call, describe(), produces different output
        # depending on the actual (runtime) type of the object -
        # this is polymorphism enabled by method overriding.
        print(s.describe())

if __name__ == "__main__":
    main()
