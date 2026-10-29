# 02: Polygon_hierarchy 

# ------ For Execution --------
# cd ads_lab 
# pwd
# python polygon_hierarchy.py


from abc import ABC, abstractmethod
import math

class Polygon(ABC):
    def area(self) -> float:
        raise NotImplementedError
    def perimeter(self) -> float:
        raise NotImplementedError
    def describe(self) -> str:
        return(f"{self.__class__.__name__}:"f"area = {self.area():.2f},perimeter = {self.perimeter():.2f}")
    
class Traingle(Polygon):
    def __init__(self, side_a: float, side_b: float, side_c: float) :
        if(side_a + side_b <= side_c or side_b + side_c <= side_a or side_a + side_c <= side_b):
            raise ValueError("The given Sides do not form a vaild traingle.")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    def area(self) -> float:
        s = self.perimeter()/2
        return math.sqrt(s * (s - self.side_a) * (s- self.side_b) * (s - self.side_c))
    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c
    
class Quadrilateral(Polygon):
    def __init__(self, length:float, width: float):
        self.length = length
        self.width = width
    def area(self) -> float:
        return self.length * self.width
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
class Pentagon(Polygon):
    def __init__(self, side: float):
        self.side = side
    def area(self) -> float:
        return 0.25 * math.sqrt(5 * (5+2 * math.sqrt(5))) * (self.side ** 2)
    def perimeter(self) -> float:
        return 5 * self.side

def _read_float(prompt: str) -> float:
    while True:
        try:
            return float (input(prompt))
        except ValueError:
            print("please enter a valid Number.")

def create_polygon_interactively() -> Polygon:
    print("\nChoose a polygon type:")
    print(" 1. Triangle (3 sides)")
    print(" 2. Quadrilateral (length X width)")
    print(" 3. Pentagon (regular,1 side)")
    choice = input(" Enter choice (1/2/3):").strip()
    if choice == "1":
        a = _read_float("Side A:")
        b = _read_float("Side B:")
        c = _read_float("Side C:")
        return Traingle(a,b,c) 
    elif choice == "2":
        length = _read_float("length: ")
        width = _read_float("width:")
        return Quadrilateral (length, width)
    elif choice == "3":
        side = _read_float("side length:")
        return Pentagon(side)
    else:
        raise ValueError("Invalid choice. please choose 1,2 or 3.")
def demo():
    print("=== Demo mode (sample polygons) ===")
    shapes = [Traingle(3,4,5), Quadrilateral(6,4), Pentagon(5)]
    for shape in shapes:
        print(shape.describe())

def main():
    demo()
    print("\n===Interactive Mode ===")
    answer = input(" would you like to create your own polygon(s)? (y/n) : ").strip().lower()
    while answer == "y":
        try:
            polygon = create_polygon_interactively()
            print(polygon.describe())
        except ValueError as e:
            print(f"Error: {e}")
        answer = input("\n Create another polygon? (y/n):").strip().lower()
    print("Good Bye!")
if __name__== "__main__":
    main()
