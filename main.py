from Grid import Grid
from Square import Square
from Frontier import Frontier
from Node import Node
import random

def generate_maze():
    grid = Grid()
    grid = grid_init(grid);

    #initialize neighbors of each cell
    for i in range(101):
        for j in range(101):
            #print("Inserting at i = " +str(i) +" j = " + str(j))
            if i==0:
                tuple = ("South", grid.environment[i+1][j])
                grid.environment[i][j].children.append(tuple)
                if j > 0 and j < 100:
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
                if i > 0 and i < 100:
                    n_neighbor = ("North",grid.environment[i-1][j])
                    s_neighbor = ("South",grid.environment[i+1][j])
                    grid.environment[i][j].children.append(n_neighbor)
                    grid.environment[i][j].children.append(s_neighbor)
                elif i ==100:
                    tuple = ("North",grid.environment[i-1][j])
                    grid.environment[i][j].children.append(tuple)
            elif i==100:
                tuple = ("North",grid.environment[i-1][j])
                grid.environment[i][j].children.append(tuple)
                if j > 0 and j < 100:
                    e_neighbor = ("East", grid.environment[i][j+1])
                    w_neighbor = ("West", grid.environment[i][j-1])
                    grid.environment[i][j].children.append(e_neighbor)
                    grid.environment[i][j].children.append(w_neighbor)
                elif j==100:
                    tuple = ("West",grid.environment[i][j-1])
                    grid.environment[i][j].children.append(tuple)
            elif j==100:
                tuple = ("West",grid.environment[i][j-1])
                grid.environment[i][j].children.append(tuple)
                if i > 0 and i < 100:
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


    print(len(grid.environment[0][0].children))
    print(len(grid.environment[0][67].children))
    print(len(grid.environment[25][25].children))

    visited_cells = 0

    while visited_cells < 10201:
        x = generate_x()
        y = generate_y()
        if visited_cells == 0:
            visited_cells+=1;
            grid.environment[x][y].visited = True;
            grid.environment[x][y].blocked = False;
        else:
            if grid.environment[x][y].visited = False:
                grid.environment[x][y].visited = True
                visited_cells+=1
                probability = random.randint(1,11)
                if probability <= 3:
                    #blocked
                    grid.environment[x][y].blocked = True


        rand_int = random.randint(0,len(grid.environment[x][y].children))
        explore = grid.environment[x][y].children[rand_int].[1]


def generate_x():
    x = random.randint(0,101)
    return x

def generate_y():
    y = random.randint(0,101)
    return y

def grid_init(grid):
        for i in range(101):
            for j in range(101):
                square = Square(0)
                grid.environment[i][j] = square

        return grid


#main method
for i in range(1):
    generate_maze()
