from shell import *
from cannon import *
from ground import *

from tkinter import *


def start_game():
    root = Tk()
    frame = Frame(root)
    root.geometry('1200x700')
    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)

    ground = Ground(canv)
    ground.draw()

    mainloop()
