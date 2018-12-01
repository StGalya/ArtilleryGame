from tkinter import *
import random
root = Tk()
frame = Frame(root)
root.geometry('1200x700')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

h = random.randint(250,650)
for i in range (1200):
    canv.create_line(i, 700, i + 1, h, width=10, fill='green')
    x = random.randint(-5, 5)
    h = h + x


mainloop()
