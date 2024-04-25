from tkinter import *
from tkinter import messagebox

def helloCallBack():
    messagebox.showinfo("Hello Python", "Hello World")

root = Tk()
root.geometry("800x400")

# Program 1 (Kiri)
frame1 = Frame(root)
frame1.pack(side=LEFT, padx=10, pady=10)

title_label1 = Label(frame1, text="Program 1", font=("Helvetica", 16))
title_label1.pack()

button1 = Button(frame1, text="Hello", command=helloCallBack)
button1.pack(pady=10)

# Spasi ke bawah antara Program 1 dan Program 2
spacer1 = Frame(root, height=20)
spacer1.pack()

# Program 2 (Kanan)
frame2 = Frame(root, bg='blue')
frame2.pack(side=LEFT, padx=10, pady=10)

title_label2 = Label(frame2, text="Program 2", font=("Helvetica", 16), fg='white', bg='blue')
title_label2.pack()

button2 = Button(frame2, text="Tes Tombol", bg='gray', fg='red')
button2.pack()

entry = Entry(frame2, bg='green')
entry.pack()

# Spasi ke bawah antara Program 2 dan Program 3
spacer2 = Frame(root, height=20)
spacer2.pack()

# Program 3 (Kiri)
frame3 = Frame(root)
frame3.pack(side=LEFT, padx=10, pady=10)

title_label3 = Label(frame3, text="Program 3", font=("Helvetica", 16))
title_label3.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
checkbox1 = Checkbutton(frame3, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
checkbox2 = Checkbutton(frame3, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)
checkbox1.pack()
checkbox2.pack()

# Spasi ke bawah antara Program 3 dan Program 4
spacer3 = Frame(root, height=20)
spacer3.pack()

# Program 4 (Kanan)
frame4 = Frame(root)
frame4.pack(side=LEFT, padx=10, pady=10)

title_label4 = Label(frame4, text="Program 4", font=("Helvetica", 16))
title_label4.pack()

label1 = Label(frame4, text="User Name")
label1.pack(side=LEFT)
entry1 = Entry(frame4, bd=5)
entry1.pack(side=RIGHT)

# Spasi ke bawah antara Program 4 dan Program 5
spacer4 = Frame(root, height=20)
spacer4.pack()

# Program 5 (Kiri)
frame5 = Frame(root)
frame5.pack(side=LEFT, padx=10, pady=10)

title_label5 = Label(frame5, text="Program 5", font=("Helvetica", 16))
title_label5.pack()

frame6 = Frame(frame5)
frame6.pack()

button_red = Button(frame6, text="Red", fg="red")
button_green = Button(frame6, text="Brown", fg="brown")
button_blue = Button(frame6, text="Blue", fg="blue")
button_black = Button(frame5, text="Black", fg="black")

button_red.pack(side=LEFT)
button_green.pack(side=LEFT)
button_blue.pack(side=LEFT)
button_black.pack(side=BOTTOM)

# Spasi ke bawah antara Program 5 dan Program 6
spacer5 = Frame(root, height=20)
spacer5.pack()

# Program 6 (Kanan)
frame7 = Frame(root)
frame7.pack(side=LEFT, padx=10, pady=10)

title_label6 = Label(frame7, text="Program 6", font=("Helvetica", 16))
title_label6.pack()

var = StringVar()
label = Label(frame7, textvariable=var, relief=RAISED)
var.set("Hey!? How are you doing?")
label.pack()

# Spasi ke bawah antara Program 6 dan Program 7
spacer6 = Frame(root, height=20)
spacer6.pack()

# Program 7 (Kiri)
frame8 = Frame(root)
frame8.pack(side=LEFT, padx=10, pady=10)

title_label7 = Label(frame8, text="Program 7", font=("Helvetica", 16))
title_label7.pack()

top = Tk()

Lb1 = Listbox(frame8)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()


# Program 8 (Kanan)
frame9 = Frame(root)
frame9.pack(side=LEFT, padx=10, pady=10)

title_label8 = Label(frame9, text="Program 8", font=("Helvetica", 16))
title_label8.pack()

mb_frame = Frame(frame9)  # Buat frame baru untuk Menubutton
mb_frame.pack()

mb = Menubutton(mb_frame, text="condiments", relief=RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)
mb.pack()

root.mainloop()