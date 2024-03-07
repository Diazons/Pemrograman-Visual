import numpy as np
import cv2
import matplotlib.pyplot as plt

# Titik-titik
ya, xa = 200, 200
yb, xb = 200, 600
yc, xc = 600, 600
yd, xd = 600, 200

# Warna dan lebar garis
pd, lw = int(8), int(8)
pr, pg, pb = 255, 0, 255  # Warna magenta
lr, lg, lb = 255, 0, 255  # Warna magenta

# Ukuran gambar
col, row = int(800), int(800)
print('col - row', col, ',', row)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    # Membuat gambar kosong
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2 - y1
    dx = x2 - x1

    # Buat titik pertama
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if (i - x1) ** 2 + (j - y1) ** 2 < hd ** 2:
                Gambar[j, i] = [pr, pg, pb]

    # Buat titik kedua
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if (i - x2) ** 2 + (j - y2) ** 2 < hd ** 2:
                Gambar[j, i] = [pr, pg, pb]

    # Buat garis cendrung horizontal
    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i - x1) + y1)
            x, y = i, j
            print('x,y =', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x) ** 2 + (j - y) ** 2 < hw ** 2:
                        Gambar[j, i] = [lr, lg, lb]

    # Buat garis cendrung vertikal
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x, y = i, j
            print('x,y =', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x) ** 2 + (j - y) ** 2 < hw ** 2:
                        Gambar[j, i] = [lr, lg, lb]

    return Gambar

hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)

# Menampilkan gambar
plt.figure()
plt.imshow(hasil)
plt.show()