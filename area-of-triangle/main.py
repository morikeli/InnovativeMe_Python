# Function to calculate area of a triangle with 3 sides using Heron's formula.
import math  # We import the math module to use the square root function.

def calculate_area_using_heron(a, b, c):
    """ This is a function to calculate area of a triangle using Heron's formula. """

    s = (a + b + c) / 2   # All sides are added up and divided by 2.
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))   # Square root is imported from math module to calculate the area.
    return round(area, 2)


if __name__ == '__main__':
    a = int(input('Enter the length of first side (a): '))
    b = int(input('Enter the length of the second side (b): '))
    c = int(input('Enter the length of the third side (c): '))
    
    calculated_area = calculate_area_using_heron(a, b, c)
    print(f'Area of the triangle: {calculated_area}')   # The area is rounded off to 2 decimal places.