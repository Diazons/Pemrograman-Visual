
#Case 1
print("Case 1")
#Data bertipe Boolean yang kita Deklarasikan (Cara Standar)
f = bool(True)
g = bool(False)
print(f)
print(g)
print("============================================")

#Case 2
print("Case 2")
#Data bertipe Boolean Dalam Berbagai Konteks
#Tercatat Dengan Sendirinya oleh Komputer tanpa Deklarasi
print(3>2)
print(3+2==5)
print(3<2)
print("============================================")

#Case 3
print("Case 3")
#Data Bertipe Boolean dalam berbagai konteks
#Tercatat dengan sendirinya oleh komputer tanpa deklarasi
Penghasilan = 2000000
PenghasilanTanpaPajak = 4000000
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak yang harus anda bayar: Rp ", PajakYangHarusDibayar)

#PART 2
#Case 4
print("Case 4")
#Semua data yang tidak nol (kosong) memiliki nilai boolean True
a = 3
b = "Ini data string"
c = ("laptop", "buku", "ballpen")
d = ["laptop", "buku", "ballpen"]
e = {"laptop":"asus", "buku":"buku_teks", "ballpen": "arrow"}
f = {1, 2, 3, 4, 5}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("============================================")

#PART 3
#Case 5
print("Case 5")
#Semua data yang tidak nol (kosong) memiliki nilai boolean True
a = 0
b = ""
c = ()
d = []
e = {}

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("============================================")

#Case 6
print("Case 6")
#Variabel yang panjangnya nol memiliki nilai boolean false
class myclass():
    def __len__(self):
        return 0
print(bool(myclass()))
print("============================================")