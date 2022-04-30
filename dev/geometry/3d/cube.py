import math;

# Given a side in the cube, return the volume of the cube
def volume_of_cube(x):
    return x**3

# Given a side in the cube, return the surface area of the cube
def surface_area_of_cube(x):
    return 6 * x**2

# Given a side in the cube, return the diagonal of the cube
def diagonal_of_cube(x):
    return math.sqrt(3) * x

# Given the volume of a cube, return the side of the cube
def side_of_cube_from_volume(x):
    return math.cbrt(x)

# Given the surface area of a cube, return the side of the cube
def side_of_cube_from_surface_area(x):
    return math.sqrt(x / 6)

# Given the diagonal of a cube, return the volume of the cube
def volume_of_cube_from_diagonal(x):
    return x**3 / 3