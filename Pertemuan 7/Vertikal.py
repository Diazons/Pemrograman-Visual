import numpy as np
import matplotlib.pyplot as plt

# USER ENTRIES: The user informs the coordinates of the two points for the line
x1 = 100
y1 = 200
x2 = 100
y2 = 1000

# The user decides the line width
lw = int(3)

# Calculate the half line width
hw = int(lw / 2)

# Setting the size of the canvas
col = int(1920)
row = int(1080)
print('col, row =', col, ',', row)

# Preparing the black canvas
Gambar = np.zeros((row, col, 3), dtype=np.uint8)

Gambar[:, :, :] = 255  # changing color to white

# Check if the line is vertical
if x2 != x1:
    # Calculate the slope of the line
    m = (y2 - y1) / (x2 - x1)

    # Calculate the x-intercept of the line
    c = x1 - hw

    # Draw the line
    y_start = min(y1, y2)
    y_end = max(y1, y2)
    for y in range(y_start, y_end + 1):
        x = int(m * (y - y1) + c)
        for i in range(y - hw, y + hw + 1):
            for j in range(x - hw, x + hw + 1):
                if 0 <= i < row and 0 <= j < col:
                    Gambar[i, j, :] = 0
else:
    # Draw a vertical line
    x = x1
    for y in range(y1, y2 + 1):
        for i in range(y - hw, y + hw + 1):
            for j in range(x - hw, x + hw + 1):
                if 0 <= i < row and 0 <= j < col:
                    Gambar[i, j, :] = 0

# Draw the additional points
x3 = 100
y3 = 200
x4 = 100
y4 = 1000

point_radius = int(lw * 3)  # Adjust the size of the points based on the line width

for i in range(x3 - point_radius, x3 + point_radius + 1):
    for j in range(y3 - point_radius, y3 + point_radius + 1):
        if (i - x3) ** 2 + (j - y3) ** 2 <= point_radius ** 2:
            if 0 <= i < col and 0 <= j < row:
                Gambar[j, i, :] = 0

for i in range(x4 - point_radius, x4 + point_radius + 1):
    for j in range(y4 - point_radius, y4 + point_radius + 1):
        if (i - x4) ** 2 + (j - y4) ** 2 <= point_radius ** 2:
            if 0 <= i < col and 0 <= j < row:
                Gambar[j, i, :] = 0

# Flip the image vertically
Gambar = np.flip(Gambar, axis=0)

plt.figure()
plt.imshow(Gambar)
plt.show()