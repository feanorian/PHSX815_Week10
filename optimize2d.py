"""
Name: Craig Brooks
PHSX 815 Spring 2023
HW # 10
Due Date 3/30/2023
This code optimizes a pre-defined 2D function using the minimize method from scipy.optimize
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

# Define the 3D function to plot
def f(xy):
    return (2*xy[0])**2 + xy[1]**2 + 2

# Create a meshgrid of x and y values
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

# Evaluate the function at each point in the meshgrid
Z = f([X, Y])

# Plot the function as a 3D surface
fig = plt.figure()
ax = fig.add_subplots(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Find the minimum of the function using the minimize function from SciPy
x0 = [0, 0] # Initial guess for the minimum
optimize = minimize(f, x0)
print(f"Minimum found at x = {optimize.x[0]}, y = {optimize.x[1]}, z = {f(optimize.x)}" )

# Plot the minimum as a red dot
ax.scatter(optimize.x[0], optimize.x[1], f(optimize.x), c='red', s=50)

# Set the axis labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.set_title(f"Minimum found at x = {optimize.x[0]}, y = {optimize.x[1]}, z = {f(optimize.x)}")

# Show the plot
plt.show()
