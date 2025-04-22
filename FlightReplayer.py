import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PositionParser import dictPoses

# for dictPoses
x_coords = []
y_coords = []
z_coords = []

for position in dictPoses.values():
    x, y, z = position  # unpack the coordinates
    x_coords.append(x)
    y_coords.append(z)
    z_coords.append(y)

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the first point in red
ax.scatter(x_coords[0], y_coords[0], z_coords[0], c='r', marker='o', s=100, label='Start Point')

# Plot the line from the first point to all subsequent points in blue
ax.plot(x_coords, y_coords, z_coords, c='b', marker='o')

# Set labels
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Z Coordinate')
ax.set_zlabel('Altitude (Y)')

# Set the limits to fit the data
ax.set_xlim(min(x_coords) - 10, max(x_coords) + 10)
ax.set_ylim(min(y_coords) - 10, max(y_coords) + 10)
ax.set_zlim(min(z_coords) - 10, max(z_coords) + 10)

# Show the plot
plt.legend()
plt.show()
