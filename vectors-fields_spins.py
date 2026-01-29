import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Canting angle (in radians)

theta = np.pi /2 # coplaner
theta = np.pi/4 # < 90 Umbrella canting structure; force the origin to 0,0,0 below. Umbrella is not useful for my case.
theta = np.pi/4 # < 90 120 degree canting structure; force the origin to S1, S2, S3 below.
theta = np.pi/4  # try changing this
# Define spin vectors
S1 = np.array([np.sin(theta), 0.0, np.cos(theta)])

S2 = np.array([-0.5 * np.sin(theta), np.sqrt(3)/2 * np.sin(theta), np.cos(theta)])

S3 = np.array([-0.5 * np.sin(theta), -np.sqrt(3)/2 * np.sin(theta), np.cos(theta)])

spins = [S1, S2, S3]
print(spins)
# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.zeros(3)

# Plot each spin as an arrow
for i, S in enumerate(spins, start=1):
    ax.quiver(
        S[0], S[1], S[2], # origin[0], origin[1], origin[2]
        S[0], S[1], S[2],
        length=1, normalize=True, linewidth=5
    )
    ax.text(S[0], S[1], S[2], f"S{i}", fontsize=12)

# Axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set equal aspect ratio
ax.set_box_aspect([1, 1, 1])

# Limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

plt.title("Three canted spins (DMI-friendly 120° structure)")
plt.show()

