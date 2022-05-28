import math

# Given the radius in a sphere, return the volume of the sphere
def volume_of_sphere(r):
    return (4 / 3) * math.pi * r**3


# Given the radius in a sphere, return the surface area of the sphere
def surface_area_of_sphere(r):
    return 4 * math.pi * r**2


# Given the radius in a sphere, return the diameter of the sphere
def diameter_of_sphere(r):
    return 2 * r


# Given the volume of a sphere, return the radius of the sphere
def radius_of_sphere_from_volume(v):
    return math.cbrt(v / (4 / 3 * math.pi))


# Given the surface area of a sphere, return the radius of the sphere
def radius_of_sphere_from_surface_area(a):
    return math.sqrt(a / (4 * math.pi))