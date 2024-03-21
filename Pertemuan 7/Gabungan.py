import numpy as np
import matplotlib.pyplot as plt

# USER ENTRIES: The user informs the coordinates of the two points for the lines
x1 = 100
y1 = 200
x2 = 100
y2 = 1000

x3 = 100
y3 = 200
x4 = 1800
y4 = 200

x5 = 500
y5 = 900
x6 = 1700
y6 = 900

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

# Draw the vertical line
if x2 != x1:
    m1 = (y2 - y1) / (x2 - x1)
    c1 = x1 - hw

    y_start = min(y1, y2)
    y_end = max(y1, y2)
    for y in range(y_start, y_end + 1):
        x = int(m1 * (y - y1) + c1)
        for i in range(y - hw, y + hw + 1):
            for j in range(x - hw, x + hw + 1):
                if 0 <= i < row and 0 <= j < col:
                    Gambar[i, j, :] = 0
else:
    x = x1
    for y in range(y1, y2 + 1):
        for i in range(y - hw, y + hw + 1):
            for j in range(x - hw, x + hw + 1):
                if 0 <= i < row and 0 <= j < col:
                    Gambar[i, j, :] = 0

# Draw the horizontal line
if y4 != y3:
    m2 = (x4 - x3) / (y4 - y3)
    c2 = x3 - hw

    x_start = min(x3, x4)
    x_end = max(x3, x4)
    for x in range(x_start, x_end + 1):
        y = int(m2 * (x - x3) + c2)
        for i in range(y - hw, y + hw + 1):
            for j in range(x - hw, x + hw + 1):
                if 0 <= i < row and 0 <= j < col:
                    Gambar[i, j, :] = 0
else:
    y = y3
    for x in range(x3, x4 + 1):
        for i in range(y - hw, y + hw + 1):
            for j in range(x - hw, x + hw + 1):
                if 0 <= i < row and 0 <= j < col:
                    Gambar[i, j, :] = 0

# Draw the slightly upward sloping line
if y6 != y5:
    m3 = (x6 - x5) / (y6 - y5)
    c3 = x5 - hw

    x_start = min(x5, x6)
    x_end = max(x5, x6)
    for x in range(x_start, x_end + 1):
        y = int(m3 * (x - x5) + c3)
        for i in range(y - hw, y + hw + 1):
            for j in range(x - hw, x + hw + 1):
                if 0 <= i < row and 0 <= j < col:
                    Gambar[i, j, :] = 0
else:
    y = y5
    for x in range(x5, x6 + 1):
        for i in range(y - hw, y + hw + 1):
            for j in range(x - hw, x + hw + 1):
                if 0 <= i < row and 0 <= j < col:
                    Gambar[i, j, :] = 0

# Draw the additional points
point_radius = int(lw * 3)  # Adjust the size of the points based on the line width

for i in range(x1 - point_radius, x1 + point_radius + 1):
    for j in range(y1 - point_radius, y1 + point_radius + 1):
        if (i - x1) ** 2 + (j - y1) ** 2 <= point_radius ** 2:
            if 0 <= i < col and 0 <= j < row:
                Gambar[j, i, :] = 0

for i in range(x2 - point_radius, x2 + point_radius + 1):
    for j in range(y2 - point_radius, y2 + point_radius + 1):
        if (i - x2) ** 2 + (j - y2) ** 2 <= point_radius ** 2:
            if 0 <= i < col and 0 <= j < row:
                Gambar[j, i, :] = 0

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

for i in range(x5 - point_radius, x5 + point_radius + 1):
    for j in range(y5 - point_radius, y5 + point_radius + 1):
        if (i - x5) ** 2 + (j - y5) ** 2 <= point_radius ** 2:
            if 0 <= i < col and 0 <= j < row:
                Gambar[j, i, :] = 0

for i in range(x6 - point_radius, x6 + point_radius + 1):
    for j in range(y6 - point_radius, y6 + point_radius + 1):
        if (i - x6) ** 2 + (j - y6) ** 2 <= point_radius ** 2:
            if 0 <= i < col and 0 <= j < row:
                Gambar[j, i, :] = 0

# Flip the image vertically
Gambar = np.flip(Gambar, axis=0)

plt.figure()
plt.imshow(Gambar)
plt.show()