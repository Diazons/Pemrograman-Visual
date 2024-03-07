# Membuat dua set berisi nama buah-buahan
buah_set1 = {"Apel", "Mangga", "Jeruk", "Pisang"}
buah_set2 = {"Mangga", "Anggur", "Pisang", "Durian"}

# Menampilkan tipe data set
print("Tipe data buah_set1 adalah", type(buah_set1))
print("Tipe data buah_set2 adalah", type(buah_set2))
print("Data buah_set1: ", buah_set1)
print("Data buah_set2: ", buah_set2)
print("-----------------------------------")

# Menampilkan buah-buahan yang ada di buah_set1
print("Buah-buahan di buah_set1:")
for buah in buah_set1:
    print(buah)
print("-----------------------------------")

# Menampilkan panjang buah_set1
print("Jumlah buah dalam buah_set1:", len(buah_set1))

# Memeriksa apakah sebuah buah ada di buah_set1
if "Jeruk" in buah_set1:
    print("Yes, 'Jeruk' is an item in buah_set1.")

# Menambahkan buah baru ke dalam buah_set1
buah_set1.add("Nanas")
print("Buah_set1 setelah menambahkan 'Nanas':", buah_set1)

# Menghapus buah dari buah_set1
buah_set1.remove("Mangga")
print("Buah_set1 setelah menghapus 'Mangga':", buah_set1)

# Menggabungkan dua set (union)
gabungan_buah = buah_set1.union(buah_set2)
print("Gabungan buah_set1 dan buah_set2:", gabungan_buah)

# Menyaring buah yang sama (intersection)
buah_sama = buah_set1.intersection(buah_set2)
print("Buah yang sama di buah_set1 dan buah_set2:", buah_sama)

# Menyaring buah yang unik (difference)
buah_unik = buah_set1.difference(buah_set2)
print("Buah unik di buah_set1 (tidak ada di buah_set2):", buah_unik)
