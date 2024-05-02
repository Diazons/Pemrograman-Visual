import tkinter as tk

def create_rectangle():
    width = int(entry_width.get())
    height = int(entry_height.get())
    canvas.create_rectangle(10, 10, 10 + width, 10 + height, fill="red")

def create_oval():
    width = int(entry_width.get())
    height = int(entry_height.get())
    canvas.create_oval(10, 10, 10 + width, 10 + height, fill="blue")

def create_triangle():
    width = int(entry_width.get())
    height = int(entry_height.get())
    canvas.create_polygon(10, 10, 10 + width, 10, 10 + width/2, 10 + height, fill="green")

def reset_canvas():
    canvas.delete("all")

root = tk.Tk()
root.title("Bentuk Geometri")
root.configure(bg="#f1f1f1")

# Frame utama
main_frame = tk.Frame(root, bg="#f1f1f1")
main_frame.pack(padx=20, pady=20)

# Label dan entry untuk lebar
label_width = tk.Label(main_frame, text="Lebar:", bg="#f1f1f1")
label_width.grid(row=0, column=0, sticky="w")
entry_width = tk.Entry(main_frame)
entry_width.grid(row=0, column=1, padx=5, pady=5)

# Label dan entry untuk tinggi
label_height = tk.Label(main_frame, text="Tinggi:", bg="#f1f1f1")
label_height.grid(row=1, column=0, sticky="w")
entry_height = tk.Entry(main_frame)
entry_height.grid(row=1, column=1, padx=5, pady=5)

# Frame untuk tombol
button_frame = tk.Frame(main_frame, bg="#f1f1f1")
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

# Tombol untuk membuat persegi panjang
button_rectangle = tk.Button(button_frame, text="Persegi Panjang", command=create_rectangle, width=15)
button_rectangle.grid(row=0, column=0, padx=5)

# Tombol untuk membuat lingkaran
button_oval = tk.Button(button_frame, text="Lingkaran", command=create_oval, width=15)
button_oval.grid(row=0, column=1, padx=5)

# Tombol untuk membuat segitiga
button_triangle = tk.Button(button_frame, text="Segitiga", command=create_triangle, width=15)
button_triangle.grid(row=0, column=2, padx=5)

# Tombol untuk mereset canvas
button_reset = tk.Button(main_frame, text="Reset", command=reset_canvas, width=15)
button_reset.grid(row=3, column=0, columnspan=2, pady=10)

# Canvas untuk menampilkan objek-objek
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

root.mainloop()