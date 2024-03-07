import numpy as np
import matplotlib.pyplot as plt

# Garis 1
x1 = np.array([2, 6])
y1 = np.array([4, 8])

gradient1 = (y1[1] - y1[0]) / (x1[1] - x1[0])
equation1 = f'y = {gradient1:.2f}x + {y1[0] - gradient1 * x1[0]:.2f}'

# Garis 2
x2 = np.array([-3, 1])
y2 = np.array([5, 2])

gradient2 = (y2[1] - y2[0]) / (x2[1] - x2[0])
equation2 = f'y = {gradient2:.2f}x + {y2[0] - gradient2 * x2[0]:.2f}'

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(x1, y1, '-r', label=f'Garis 1: {equation1}')
plt.plot(x2, y2, '-b', label=f'Garis 2: {equation2}')
plt.scatter(x1, y1, color='red')
plt.scatter(x2, y2, color='blue')
plt.legend()
plt.grid(True)
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Dua Garis dengan Persamaan Gradien')
plt.show()
