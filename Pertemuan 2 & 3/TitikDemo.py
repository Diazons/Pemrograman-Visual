import numpy as np
import matplotlib.pyplot as plt

# USER ENTRIES: The user informs the coordinates of the two points for the line
x1 = 100
y1 = 200
x2 = 700
y2 = 700

# The user decides the line width
lw = int(10)

# Calculate the half line width
hw = int(lw / 2)

# Setting the size of the canvas
col = int(800)
row = int(800)
# col = int(5/7*1920)
# row = int(5/7*1080)
print('col, row =', col, ',', row)

# Preparing the black canvas
Gambar = np.zeros((row, col, 3), dtype=np.uint8)  # Corrected 'shape' to '(row, col, 3)'

Gambar[:, :, :] = 255  # changing color to white

# Drawing points with one pixel (Too small)
Gambar[y1, x1, :] = 0  # For a white screen
Gambar[y2, x2, :] = 0
Gambar[y1, x1, 0] = 255
Gambar[y2, x2, 0] = 255  # Corrected typo: 'Gambar[y2, x2, :] = 255' to 'Gambar[y2, x2, 0] = 255'

for i in range(x1 - hw, x1 + hw):
    for j in range(y1 - hw, y1 + hw):
        if ((i - x1) ** 2 + (j - y1) ** 2) < hw ** 2:
            Gambar[j, i, :] = 0
            Gambar[j, i, 0] = 255

for i in range(x2 - hw, x2 + hw):
    for j in range(y2 - hw, y2 + hw):
        if ((i - x2) ** 2 + (j - y2) ** 2) < hw ** 2:
            Gambar[j, i, :] = 0
            Gambar[j, i, 0] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()
