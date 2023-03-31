import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

# Define the 3D function to plot
def f(x):
    return (2*x[0])**2 + x[1]**2 + 2

# Create a meshgrid of x and y values
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

# Evaluate the function at each point in the meshgrid
Z = f([X, Y])

# Plot the function as a 3D surface
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Find the minimum of the function using the minimize function from SciPy
x0 = [0, 0] # Initial guess for the minimum
res = minimize(f, x0)
print(f"Minimum found at x = {res.x[0]}, y = {res.x[1]}, z = {f(res.x)}" )

# Plot the minimum as a red dot
ax.scatter(res.x[0], res.x[1], f(res.x), c='orange')

# Set the axis labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.set_title(f"Minimum found at x = {res.x[0]}, y = {res.x[1]}, z = {f(res.x)}")

for angle in range(0, 360):
    ax.view_init(100, angle)
    plt.draw()
    plt.pause(.001)


# Show the plot
plt.show()