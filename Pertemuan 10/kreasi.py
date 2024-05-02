import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter import messagebox

def draw_circle():
    canvas.delete("all")  # Menghapus bangun ruang yang lain
    radius = askinteger("Ukuran Lingkaran", "Masukkan Jari-Jari Lingkaran:")
    canvas.create_oval(100 - radius, 100 - radius, 100 + radius, 100 + radius, outline="black", fill="red")
    luas = 3.14 * radius * radius
    messagebox.showinfo("Hasil", f"Luas lingkaran adalah: {luas}")

def draw_rectangle():
    canvas.delete("all")  # Menghapus bangun ruang yang lain
    width = askinteger("Ukuran Segiempat", "Masukkan Lebar Segiempat:")
    height = askinteger("Ukuran Segiempat", "Masukkan Tinggi Segiempat:")
    canvas.create_rectangle(100 - width / 2, 100 - height / 2, 100 + width / 2, 100 + height / 2, outline="black", fill="blue")
    luas = width * height
    messagebox.showinfo("Hasil", f"Luas Segiempat Adalah: {luas}")

def draw_triangle():
    canvas.delete("all")  # Menghapus bangun ruang yang lain
    base = askinteger("Ukuran Segitiga", "Masukkan Lebar Segitiga:")
    height = askinteger("Ukuran Segitiga", "Masukkan Tinggi Segitiga:")
    canvas.create_polygon(100 - base / 2, 100 + height / 2, 100 + base / 2, 100 + height / 2, 100, 100 - height / 2, outline="black", fill="green")
    luas = 0.5 * base * height
    messagebox.showinfo("Hasil", f"Luas Segitiga adalah: {luas}")

def draw_parallelogram():
    canvas.delete("all")  # Menghapus bangun ruang yang lain
    base = askinteger("Ukuran Jajargenjang", "Masukkan Lebar Jajargenjang:")
    height = askinteger("Ukuran Jajargenjang", "Masukkan Tinggi Jajargenjang:")
    canvas.create_polygon(100 - base / 2, 100 + height / 2, 100 + base / 2, 100 + height / 2, 100 + base / 2 - 50, 100 - height / 2, 100 - base / 2 - 50, 100 - height / 2, outline="black", fill="yellow")
    luas = base * height
    messagebox.showinfo("Hasil", f"Luas Jajargenjang Adalah: {luas}")

root = tk.Tk()
root.title("Aplikasi Menggambar Objek 2 Dimensi")

# Membuat tata letak dan gaya tampilan yang lebih menarik
title_label = tk.Label(root, text="Aplikasi Menggambar Objek 2 Dimensi", font=("Helvetica", 16))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

canvas = tk.Canvas(frame, width=300, height=300, bg="white")
canvas.pack(side="left", padx=10)

scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

draw_frame = tk.Frame(root)
draw_frame.pack(pady=10)

circle_button = tk.Button(draw_frame, text="Lingkaran", command=draw_circle, padx=10)
circle_button.pack(side="left", padx=5)

rectangle_button = tk.Button(draw_frame, text="Segiempat", command=draw_rectangle, padx=10)
rectangle_button.pack(side="left", padx=5)

triangle_button = tk.Button(draw_frame, text="Segitiga", command=draw_triangle, padx=10)
triangle_button.pack(side="left", padx=5)

parallelogram_button = tk.Button(draw_frame, text="Jajargenjang", command=draw_parallelogram, padx=10)
parallelogram_button.pack(side="left", padx=5)

root.mainloop()