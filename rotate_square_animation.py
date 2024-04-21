import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the cube corners in each octant
cube = np.array([[1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1],
                 [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1]])

# Define the connections between the corners to form the cube
connections = [(0, 1), (1, 2), (2, 3), (3, 0),
               (4, 5), (5, 6), (6, 7), (7, 4),
               (0, 4), (1, 5), (2, 6), (3, 7)]

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Initialize the cube plot
lines = [ax.plot([], [], [], 'b-')[0] for _ in range(len(connections))]

# Define the angle increment for each frame so that we achieve rotation
angle_increment = 0.05

def update(frame):
    # Calculate the rotation matrix around the y-axis
    theta = frame * angle_increment
    rot_matrix_y = np.array([[np.cos(theta), 0, np.sin(theta)],
                              [0, 1, 0],
                              [-np.sin(theta), 0, np.cos(theta)]])

    # Apply the rotation matrix to the cube
    rotated_cube = cube.dot(rot_matrix_y)

    # Update the plot
    for i, (start, end) in enumerate(connections):
        lines[i].set_xdata([rotated_cube[start, 0], rotated_cube[end, 0]])
        lines[i].set_ydata([rotated_cube[start, 1], rotated_cube[end, 1]])
        lines[i].set_3d_properties([rotated_cube[start, 2], rotated_cube[end, 2]])

    return lines

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 100), interval=50, blit=True)

# Display the animation
plt.show()

# hi
