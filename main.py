from Grid import Grid
from Square import Square
from Frontier import Frontier
from Node import Node
import draw
import random
from settings import *

def generate_maze():
    grid = Grid()
    grid = grid_init(grid);
    draw.createGrid()
    #initialize neighbors of each cell
    for i in range(DIM + 1):
        for j in range(DIM + 1):
            if i==0:
                tuple = ("South", grid.environment[i+1][j])
                grid.environment[i][j].children.append(tuple)
                if j > 0 and j < DIM:
                    e_neighbor = ("East", grid.environment[i][j+1])
                    w_neighbor = ("West", grid.environment[i][j-1])
                    grid.environment[i][j].children.append(e_neighbor)
                    grid.environment[i][j].children.append(w_neighbor)
                elif j==0:
                    tuple = ("East",grid.environment[i][j+1])
                    grid.environment[i][j].children.append(tuple)
                else:
                    tuple = ("West",grid.environment[i][j-1])
                    grid.environment[i][j].children.append(tuple)

            elif j==0:
                tuple = ("East",grid.environment[i][j+1])
                grid.environment[i][j].children.append(tuple)
                if i > 0 and i < DIM:
                    n_neighbor = ("North",grid.environment[i-1][j])
                    s_neighbor = ("South",grid.environment[i+1][j])
                    grid.environment[i][j].children.append(n_neighbor)
                    grid.environment[i][j].children.append(s_neighbor)
                elif i ==DIM:
                    tuple = ("North",grid.environment[i-1][j])
                    grid.environment[i][j].children.append(tuple)
            elif i==DIM:
                tuple = ("North",grid.environment[i-1][j])
                grid.environment[i][j].children.append(tuple)
                if j > 0 and j < DIM:
                    e_neighbor = ("East", grid.environment[i][j+1])
                    w_neighbor = ("West", grid.environment[i][j-1])
                    grid.environment[i][j].children.append(e_neighbor)
                    grid.environment[i][j].children.append(w_neighbor)
                elif j==DIM:
                    tuple = ("West",grid.environment[i][j-1])
                    grid.environment[i][j].children.append(tuple)
            elif j==DIM:
                tuple = ("West",grid.environment[i][j-1])
                grid.environment[i][j].children.append(tuple)
                if i > 0 and i < DIM:
                    n_neighbor = ("North",grid.environment[i-1][j])
                    s_neighbor = ("South",grid.environment[i+1][j])
                    grid.environment[i][j].children.append(n_neighbor)
                    grid.environment[i][j].children.append(s_neighbor)
            else:
                n_neighbor = ("North",grid.environment[i-1][j])
                s_neighbor = ("South",grid.environment[i+1][j])
                e_neighbor = ("East",grid.environment[i][j+1])
                w_neighbor = ("West",grid.environment[i][j-1])
                grid.environment[i][j].children.append(n_neighbor)
                grid.environment[i][j].children.append(s_neighbor)
                grid.environment[i][j].children.append(e_neighbor)
                grid.environment[i][j].children.append(w_neighbor)

    visited_cells = 0
    stack = Frontier()

    #choose random initial state
    x = generate_x()
    y = generate_y()
    initial_cell = grid.environment[x][y]
    initial_cell.visited = True;
    initial_cell.blocked = False;
    index = (initial_cell.y * DIM) + initial_cell.x
    item = draw.c.find_withtag(str(index))
    draw.c.itemconfig(item, fill='green')

    neighbors = initial_cell.children
    num_of_neighbors = len(initial_cell.children)
    state = initial_cell

    while(1):

        #get neighbors of state
        neighbors = state.children

        #select a random neighboring cell
        num_of_neighbors = len(state.children)

        i = 0
        while(1):
            if(i == num_of_neighbors):
                #dead end
                print("Building...")
                state = stack.pop()
                if(stack.size == 0):
                    print("Done!")
                    draw.drawGrid()
                    return
                break
            random_cell = neighbors[random.randint(0, num_of_neighbors - 1)][1]
            if(random_cell.visited is False):
                break
            else:
                i += 1
        random_cell.visited = True

        #make cell unblocked or blocked with a probability
        rand = random.randint(1, 10)
        if(rand < 4):
            #mark as blocked
            random_cell.blocked = True
            index = (random_cell.y * DIM) + random_cell.x
            item = draw.c.find_withtag(str(index))
            draw.c.itemconfig(item, fill='black')
            state = random_cell
        else:
            #mark as unblocked
            random_cell.blocked = False
            index = (random_cell.y * DIM) + random_cell.x
            node = Node(random_cell, None)
            stack.push(node)
        state = random_cell

def generate_x():
    x = random.randint(0, DIM)
    return x

def generate_y():
    y = random.randint(0, DIM)
    return y

def grid_init(grid):
        for i in range(DIM + 1):
            for j in range(DIM + 1):
                square = Square(0, i, j)
                grid.environment[i][j] = square

        return grid


#main method
for i in range(1):
    generate_maze()
