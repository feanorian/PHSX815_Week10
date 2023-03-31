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


def f(xy):
    return 2*(xy[0])**2 + xy[1]**2 + 2

x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

# Evaluate the function at each point in the meshgrid
Z = f([X, Y])

# Finds the minimum of the function 
x0 = [0, 0] # Initial guess for the minimum
optimize = minimize(f, x0)
print(f"Minimum found at x = {optimize.x[0]}, y = {optimize.x[1]}, z = {f(optimize.x)}" )

# Plot the function as a 3D surface and the minimum
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap='cool')

ax.scatter(optimize.x[0], optimize.x[1], f(optimize.x), c='red', s=50)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.set_title(f"Minimum found at x = {optimize.x[0]}, y = {optimize.x[1]}, z = {f(optimize.x)}")
plt.show()
