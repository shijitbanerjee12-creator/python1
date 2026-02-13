import math

class Circle:
    """
    Represents a circle with methods to compute its area and perimeter.
    """
    def __init__(self, radius):
        """
        Initializes the Circle with a given radius.
        
        Args:
            radius (float or int): The radius of the circle.
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def compute_area(self):
        """
        Computes the area of the circle using the formula A = π * r^2.
        
        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def compute_perimeter(self):
    
        return 2 * math.pi * self.radius
my_circle = Circle(radius=5)
area = my_circle.compute_area()
print(f"The area of the circle with radius {my_circle.radius} is: {area:.2f}")
perimeter = my_circle.compute_perimeter()
print(f"The perimeter of the circle with radius {my_circle.radius} is: {perimeter:.2f}")
another_circle = Circle(radius=10.5)
print(f"\nThe area of the circle with radius {another_circle.radius} is: {another_circle.compute_area():.2f}")
print(f"The perimeter of the circle with radius {another_circle.radius} is: {another_circle.compute_perimeter():.2f}")
