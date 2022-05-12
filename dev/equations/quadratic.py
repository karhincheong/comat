import math

# Given a quadratic equation with the format ax^2+bx+c=0, return the roots
def quadratic_equation(a, b, c):
    return (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a), (
        -b - math.sqrt(b**2 - 4 * a * c)
    ) / (2 * a)

# Given a quadratic equation with the format ax^2+bx+c=0, return the discriminant
def discriminant(a, b, c):
    return b**2 - 4 * a * c