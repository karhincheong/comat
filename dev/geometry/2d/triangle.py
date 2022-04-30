import math;

# Given 3 sides of a triangle, return the type of triangle
def type_of_triangle(x, y, z):
    if x + y <= z or x + z <= y or y + z <= x:
        return "Not a triangle"
    elif x == y == z:
        return "Equilateral"
    elif x == y or y == z or x == z:
        return "Isosceles"
    else:
        return "Scalene"

# Given 3 sides of a triangle, return if it is a right triangle
def is_right_triangle(x, y, z):
    if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        return True
    else:
        return False

# Given 3 sides of a triangle, return the perimeter of the triangle
def perimeter_of_triangle(x, y, z):
    return x + y + z

# Given 3 sides of a triangle, return the angle opposite the longest side
def angle_opposite_longest_side(x, y, z):
    if x > y and x > z:
        return math.degrees(math.acos((y**2 + z**2 - x**2) / (2 * y * z)))
    elif y > x and y > z:
        return math.degrees(math.acos((x**2 + z**2 - y**2) / (2 * x * z)))
    else:
        return math.degrees(math.acos((x**2 + y**2 - z**2) / (2 * x * y)))

# Given 2 sides and the angle between the 2 sides of a triangle, return the last side of the triangle
def last_side_of_triangle(x, y, z):
    return math.sqrt(x**2 + y**2 - 2 * x * y * math.cos(math.radians(z)))