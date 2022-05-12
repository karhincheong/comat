import math

# Given the radius of a circle, return the area of the circle
def area_of_circle(r):
    return math.pi * r**2


# Given the radius of a circle, return the circumference of the circle
def circumference_of_circle(r):
    return 2 * math.pi * r


# Given the radius of a circle, return the diameter of the circle
def diameter_of_circle(r):
    return 2 * r


# Given the circumference of a circle, return the radius of the circle
def radius_of_circle_from_circumference(c):
    return c / (2 * math.pi)


# Given the area of a circle, return the radius of the circle
def radius_of_circle_from_area(a):
    return math.sqrt(a / math.pi)


# Given the circumference of a circle, return the area of the circle
def area_of_circle_from_circumference(c):
    return math.pi * c**2 / 4

# Given the equation of a circle (x-a)^2+(y-b)^2=r^2, graph
def graph_circle(a, b, r):
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    for i in range(len(x)):
        for j in range(len(y)):
            if (x[i] - a)**2 + (y[j] - b)**2 == r**2:
                plt.plot(x[i], y[j], "ro")
    plt.savefig("circle.png")
    plt.show()
