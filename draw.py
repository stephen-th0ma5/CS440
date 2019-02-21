import tkinter as tk
import random
from settings import *

root = tk.Tk()
height = 700
width = 800
mazeList = ["Maze 1", "Maze 2", "Maze 3", "Maze 4", "Maze 5", "Maze 6", "Maze 7", "Maze 8", "Maze 9", "Maze 10",
"Maze 11", "Maze 12", "Maze 13", "Maze 14", "Maze 15", "Maze 16", "Maze 17", "Maze 18", "Maze 19", "Maze 20",
"Maze 21", "Maze 22", "Maze 23", "Maze 24", "Maze 25", "Maze 26", "Maze 27", "Maze 28", "Maze 29", "Maze 30",
"Maze 31", "Maze 32", "Maze 33", "Maze 34", "Maze 35", "Maze 36", "Maze 37", "Maze 38", "Maze 39", "Maze 40",
"Maze 41", "Maze 42", "Maze 43", "Maze 44", "Maze 45", "Maze 46", "Maze 47", "Maze 48", "Maze 49", "Maze 40"]
c = tk.Canvas(root, height=height, width=width)
variable = tk.StringVar(root)
variable.set("Maze 1")
w = tk.OptionMenu(root, variable, *mazeList)
w.pack()

def drawGrid():
    root.mainloop()

def createGrid():
    dim = DIM
    w_const = width / dim
    h_const = height / dim
    x1 = 0
    y1 = 0
    x2 = w_const
    y2 = h_const
    tag = 0
    for i in range(dim):
        for j in range(dim):
            rect = c.create_rectangle(x1, y1, x2, y2, fill="white", outline = 'black', tags=(str(tag)))
            tag += 1
            x1 += w_const
            x2 += w_const
        y2 += h_const
        x2 = w_const
        x1 = 0
        y1 += h_const
    c.pack()
    root.title("Maze World")
