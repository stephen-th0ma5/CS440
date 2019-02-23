import tkinter as tk
import random
from settings import *

root = tk.Tk()
height = 700
width = 700
mazeList = ["Maze 1", "Maze 2", "Maze 3", "Maze 4", "Maze 5", "Maze 6", "Maze 7", "Maze 8", "Maze 9", "Maze 10",
"Maze 11", "Maze 12", "Maze 13", "Maze 14", "Maze 15", "Maze 16", "Maze 17", "Maze 18", "Maze 19", "Maze 20",
"Maze 21", "Maze 22", "Maze 23", "Maze 24", "Maze 25", "Maze 26", "Maze 27", "Maze 28", "Maze 29", "Maze 30",
"Maze 31", "Maze 32", "Maze 33", "Maze 34", "Maze 35", "Maze 36", "Maze 37", "Maze 38", "Maze 39", "Maze 40",
"Maze 41", "Maze 42", "Maze 43", "Maze 44", "Maze 45", "Maze 46", "Maze 47", "Maze 48", "Maze 49", "Maze 50"]
c = tk.Canvas(root, height=height, width=width)
variable = tk.StringVar(root)
variable.set("Maze 1")
w = tk.OptionMenu(root, variable, *mazeList)
w.pack()

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
