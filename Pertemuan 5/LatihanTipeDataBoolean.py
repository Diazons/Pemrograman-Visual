# Program Contoh Data Boolean - Kreatifitas Anda Sendiri

# Case 11: Data Boolean dalam Konteks Pemilihan Warna
print("Case 11:")
warna_preferensi = "merah"
warna_dipilih = "merah"
warna_cocok = warna_preferensi == warna_dipilih
print(f"Apakah warna dipilih ({warna_dipilih}) cocok dengan preferensi ({warna_preferensi})? {warna_cocok}")
print("============================================")

# Case 12: Data Boolean dalam Konteks Status Pemesanan Online
print("Case 12:")
status_pesanan = "dikirim"
pesanan_diterima = status_pesanan == "diterima"
print(f"Apakah pesanan telah diterima? {pesanan_diterima}")
print("============================================")

# Case 13: Data Boolean dalam Konteks Keanggotaan Klub
print("Case 13:")
klub_anggota = {"John", "Alice", "Bob"}
nama_peserta = "Alice"
anggota_klub = nama_peserta in klub_anggota
print(f"Apakah {nama_peserta} merupakan anggota klub? {anggota_klub}")
print("============================================")

# Case 14: Data Boolean dalam Konteks Ketersediaan Stok
print("Case 14:")
stok_barang = 10
jumlah_pesanan = 15
stok_tersedia = stok_barang >= jumlah_pesanan
print(f"Apakah stok barang cukup untuk pesanan ({jumlah_pesanan})? {stok_tersedia}")
print("============================================")

# Case 15: Data Boolean dalam Konteks Login Pengguna
print("Case 15:")
username = "user123"
password = "pass123"
login_berhasil = username == "user123" and password == "pass123"
print(f"Apakah login berhasil? {login_berhasil}")
print("============================================")
