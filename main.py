from Grid import Grid
from Square import Square
from Frontier import Frontier
from Node import Node
import random

def generate_maze():
    grid = Grid()
    #grid.print_grid()
    #initialize neighbors of each cell
    for i in range(3):
        for j in range(3):
            if i==0:
                tuple = ("South", "mommy")
                square = Square(0)
                square.children.append(1)
                grid.environment[i][j] = square
                #if j > 0 and j < 100:
                    #e_neighbor = ("East", grid.environment[i][j+1])
                    #w_neighbor = ("West", grid.environment[i][j-1])

            '''elif j==0:
                tuple = ("East",grid.environment[i][j+1])
                grid.environment[i][j].children.append(tuple)
                if i > 0 and i < 100:
                    n_neighbor = ("North",grid.environment[i-1][j])
                    s_neighbor = ("South",grid.environment[i+1][j])
            elif i==100:
                tuple = ("North",grid.environment[i-1][j])
                grid.environment[i][j].children.append(tuple)
                if j > 0 and j < 100:
                    e_neighbor = ("East", grid.environment[i][j+1])
                    w_neighbor = ("West", grid.environment[i][j-1])
            elif j==100:
                tuple = ("West",grid.environment[i][j-1])
                grid.environment[i][j].children.append(tuple)
                if i > 0 and i < 100:
                    n_neighbor = ("North",grid.environment[i-1][j])
                    s_neighbor = ("South",grid.environment[i+1][j])
            else:
                n_neighbor = ("North",grid.environment[i-1][j])
                s_neighbor = ("South",grid.environment[i+1][j])
                e_neighbor = ("East",grid.environment[i][j+1])
                w_neighbor = ("West",grid.environment[i][j-1])
                grid.environment[i][j].children.append(n_neighbor)
                grid.environment[i][j].children.append(s_neighbor)
                grid.environment[i][j].children.append(e_neighbor)
                grid.environment[i][j].children.append(w_neighbor)'''

    print(grid.environment[0][0].children)
    '''

    visited_cells = 0
    print(grid.environment[0][0].children)

    x = generate_x()
    y = generate_y()
    #grid.environment[x][y].visited = True


    #iterate from start cell
    if grid.environment[x][y].visited == False:
        probability = random.randint(1,11)
        if probability <= 3:
            #blocked
            grid.environment[x][y].blocked = True
            grid.environment[x][y].visited = True
        else:
            #unblocked
            grid.environment[x][y].visited = True'''

def generate_x():
    x = random.randint(0,101)
    return x

def generate_y():
    y = random.randint(0,101)
    return y


#main method
for i in range(1):
    generate_maze()
