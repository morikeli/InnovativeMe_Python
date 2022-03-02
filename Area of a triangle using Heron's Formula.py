# Function to calculate area of a triangle with 3 sides using Heron's formula.
import math  # We import the math module to use the square root function.


def hero():
    a = int(input('Enter the length of first side (a): '))
    b = int(input('Enter the length of the second side (b): '))
    c = int(input('Enter the length of the third side (c): '))

    s = (a+b+c)/2   # All sides are added up and divided by 2.
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))   # Square root is imported from math module to calculate the area.
    print('Area of the triangle: ', round(area, 2))  # The area is rounded off to 2 decimal places.
    return


hero()
