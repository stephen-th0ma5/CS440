import tkinter as tk
import random
from settings import *

root = tk.Tk()
height = 700
width = 700
c = tk.Canvas(root, height = height, width = width)

def drawGrid():
    root.mainloop()

def createGrid():
    w_const = (width - 10) / DIM
    h_const = (height - 10) / DIM
    x1 = 5
    y1 = 5
    x2 = w_const + 5
    y2 = h_const + 5
    for i in range(DIM):
        for j in range(DIM):
            rect = c.create_rectangle(x1, y1, x2, y2, fill="white", outline = 'black')
            x1 = x2
            x2 += h_const
        y1 += h_const
        y2 += h_const
        x2 = w_const + 5
        x1 = 5
    c.pack()
    root.title("Maze World")
