import math;

# Given a side in a square, return the area of the square
def area_of_square(x):
    return x**2

# Given a side in a square, return the perimeter of the square
def perimeter_of_square(x):
    return 4 * x

# Given a side in a square, return the diagonal of the square
def diagonal_of_square(x):
    return math.sqrt(2 * x**2)

# Given the diagonal of a square, return the side of the square
def side_of_square_from_diagonal(x):
    return math.sqrt(2 * x**2)

# Given the area of a square, return the side of the square
def side_of_square_from_area(x):
    return math.sqrt(x / math.pi)

# Given the perimeter of a square, return the side of the square
def side_of_square_from_perimeter(x):
    return x / 4

# Given the diagonal of a square, return the area of the square
def area_of_square_from_diagonal(x):
    return x**2 / 2