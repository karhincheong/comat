import math

# Given 2 sides of a rectangle, return the area of the rectangle
def area_of_rectangle(x, y):
    return x * y


# Given 2 sides of a rectangle, return the perimeter of the rectangle
def perimeter_of_rectangle(x, y):
    return 2 * (x + y)


# Given 2 sides of a rectangle, return the diagonal of the rectangle
def diagonal_of_rectangle(x, y):
    return math.sqrt(2 * x**2 + 2 * y**2)
