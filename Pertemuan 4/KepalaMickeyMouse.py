import numpy as np
import matplotlib.pyplot as plt

# Bersihkan layar konsol
print("\033c")

x = np.linspace(-8, 8, 10000)
plt.figure(figsize=(7, 6.5))

# Tentukan persamaan matematika yang diinginkan
y1 = (25 - x**2)**0.5
y2 = -(25 - x**2)**0.5

y3 = 5 + (4 - (x - 4)**2)**0.5
y4 = 5 - (4 - (x - 4)**2)**0.5

y5 = 5 + (4 - (x + 4)**2)**0.5
y6 = 5 - (4 - (x + 4)**2)**0.5

# Plot kurva-kurva
plt.plot(x, y1, '-k', label='y1, y2')
plt.plot(x, y2, '-k')  # Tengah
plt.plot(x, y3, '-k', label='y3, y4')
plt.plot(x, y4, '-k')
plt.plot(x, y5, '-k', label='y5, y6')
plt.plot(x, y6, '-k')

# Tambahkan fill between
plt.fill_between(x, y1, y2, color='black')
plt.fill_between(x, y3, y4, color='black')
plt.fill_between(x, y5, y6, color='black')

plt.legend(loc='upper center')
plt.show()
