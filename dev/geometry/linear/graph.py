import matplotlib.pyplot as plt
import numpy as np

# Given an equation y=mx+b, graph
def graph_linear(m, b):
    x = np.linspace(-10, 10, 100)
    y = m * x + b
    plt.plot(x, y)
    plt.savefig("linear.png")
    plt.show()
    
# Given an equation y=mx+b, return the slope
def slope(m, b):
    return m

# Given an equation y=mx+b, return the y-intercept
def y_intercept(m, b):
    return b

# Given an equation y=mx+b, return the x-intercept
def x_intercept(m, b):
    return -b / m

# Given an equation y=ax^2+bx+c, graph
def graph_quadratic(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = a * x**2 + b * x + c
    plt.plot(x, y)
    plt.savefig("quadratic.png")
    plt.show()

# Given an equation y=ax^2+bx+c, return the y-intercept
def y_intercept_quadratic(a, b, c):
    return -c / a

# Given an equation y=ax^2+bx+c, return the vertex
def vertex(a, b, c):
    return -b / (2 * a)