import math;

# Convert degrees to radians
def degrees_to_radians(n):
    return n * math.pi / 180

# Convert radians to degrees
def radians_to_degrees(n):
    return n * 180 / math.pi

# Given an angle n (in rad), return the sine of the angle
def sine(n):
    return math.sin(n)

# Given an angle n (in rad), return the cosine of the angle
def cosine(n):
    return math.cos(n)

# Given an angle n (in rad), return the tangent of the angle
def tangent(n):
    return math.tan(n)

# Given an angle n (in rad), return the arcsine of the angle
def arcsine(n):
    return math.asin(n)

# Given an angle n (in rad), return the arccosine of the angle
def arccosine(n):
    return math.acos(n)

# Given an angle n (in rad), return the arctangent of the angle
def arctangent(n):
    return math.atan(n)