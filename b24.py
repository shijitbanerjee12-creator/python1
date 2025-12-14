def perimeter_square(side_length):
    """
    Calculates the perimeter of a square.
    Formula: Perimeter = 4 * side
    """
    perimeter = 4 * side_length
    return perimeter

def perimeter_rectangle(length, width):
    """
    Calculates the perimeter of a rectangle.
    Formula: Perimeter = 2 * (length + width)
    """
    perimeter = 2 * (length + width)
    return perimeter
side = float(input("Enter the side length of the square: "))
square_perimeter = perimeter_square(side)
print(f"The perimeter of the square is: {square_perimeter}")
print("-" * 20) 
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_perimeter = perimeter_rectangle(length, width)
print(f"The perimeter of the rectangle is: {rectangle_perimeter}")
import math

def calculate_circumference(radius):
    """
    Calculates the circumference of a circle given its radius.

    Args:
        radius (float or int): The radius of the circle.

    Returns:
        float: The calculated circumference.
    """
    circumference = 2 * math.pi * radius
    return circumference
circle_radius = 5.0
result_circumference = calculate_circumference(circle_radius)
print(f"The radius of the circle is: {circle_radius}")
print(f"The circumference of the circle is: {result_circumference:.2f}")
radius_2 = 10
print(f"\nFor a circle with radius {radius_2}, the circumference is: {calculate_circumference(radius_2):.2f}")
