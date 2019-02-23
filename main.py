from Grid import Grid
from Square import Square
from Frontier import Frontier
from Node import Node
import draw
import random
from settings import *
import time

def generate_start_and_finish():
    #choose initial cell
    index = (generate_x() * DIM) + generate_y()
    item = draw.c.find_withtag(str(index + 1))
    draw.c.itemconfig(item, fill='green')

    #choose target cell
    index = (generate_x() * DIM) + generate_y()
    item = draw.c.find_withtag(str(index + 1))
    draw.c.itemconfig(item, fill='red')

#highlights neighbors of specific cell
def show_neighbors(i, j, grid):
    children = grid.environment[i][j].children
    for child in children:
        index = (child[1].x * DIM) + child[1].y
        item = draw.c.find_withtag(str(index + 1))
        draw.c.itemconfig(item, fill='blue')
        draw.c.update()

#unhighlights neighbors of specific cell
def hide_neighbors(i, j, grid):
    children = grid.environment[i][j].children
    for child in children:
        index = (child[1].x * DIM) + child[1].y
        item = draw.c.find_withtag(str(index + 1))
        draw.c.itemconfig(item, fill='white')
        draw.c.update()

#highlights specific cell with index
def show_index(index):
    item = draw.c.find_withtag(str(index))
    draw.c.itemconfig(item, fill='blue')
    draw.c.update()

#animates traversal through the grid
def traverse_maze():
    index = 0
    for i in range(DIM):
        for j in range(DIM):
            item = draw.c.find_withtag(str(index))
            draw.c.itemconfig(item, fill='red')
            time.sleep(TIME)
            draw.c.update()
            index += 1

def generate_maze():
    grid = Grid()
    grid = grid_init(grid);

    #initialize neighbors of each cell
    for i in range(DIM):
        for j in range(DIM):
            if i == 0:
                tuple = ("South", grid.environment[i+1][j])
                grid.environment[i][j].children.append(tuple)
                if j > 0 and j < DIM - 1:
                    e_neighbor = ("East", grid.environment[i][j+1])
                    w_neighbor = ("West", grid.environment[i][j-1])
                    grid.environment[i][j].children.append(e_neighbor)
                    grid.environment[i][j].children.append(w_neighbor)
                elif j == 0:
                    tuple = ("East",grid.environment[i][j+1])
                    grid.environment[i][j].children.append(tuple)
                else:
                    tuple = ("West",grid.environment[i][j-1])
                    grid.environment[i][j].children.append(tuple)

            elif j == 0:
                tuple = ("East",grid.environment[i][j+1])
                grid.environment[i][j].children.append(tuple)
                if i > 0 and i < DIM - 1:
                    n_neighbor = ("North",grid.environment[i-1][j])
                    s_neighbor = ("South",grid.environment[i+1][j])
                    grid.environment[i][j].children.append(n_neighbor)
                    grid.environment[i][j].children.append(s_neighbor)
                elif i == DIM - 1:
                    tuple = ("North",grid.environment[i-1][j])
                    grid.environment[i][j].children.append(tuple)
            elif i == DIM - 1:
                tuple = ("North",grid.environment[i-1][j])
                grid.environment[i][j].children.append(tuple)
                if j > 0 and j < DIM - 1:
                    e_neighbor = ("East", grid.environment[i][j+1])
                    w_neighbor = ("West", grid.environment[i][j-1])
                    grid.environment[i][j].children.append(e_neighbor)
                    grid.environment[i][j].children.append(w_neighbor)
                elif j==DIM - 1:
                    tuple = ("West",grid.environment[i][j-1])
                    grid.environment[i][j].children.append(tuple)
            elif j == DIM - 1:
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

    #animation to show neighbors for each cell
    '''
    for i in range(DIM):
        for j in range(DIM):
            show_neighbors(i, j, grid)
            time.sleep(1)
            hide_neighbors(i, j, grid)
    '''

    stack = Frontier()

    #choose random initial state
    x = generate_x()
    y = generate_y()
    initial_cell = grid.environment[x][y]
    initial_cell.visited = True;
    initial_cell.blocked = False;
    '''
    index = (initial_cell.x * DIM) + initial_cell.y
    item = draw.c.find_withtag(str(index + 1))
    draw.c.itemconfig(item, fill='green')
    #draw.c.update()
    #time.sleep(TIME)
    '''
    neighbors = initial_cell.children
    num_of_neighbors = len(initial_cell.children)
    state = initial_cell


    while(1):

        #get neighbors of state
        neighbors = state.children

        #add neighbors to stack and mark as visited
        for neighbor in neighbors:
            if(neighbor[1].visited is False):
                node = Node(neighbor[1], None)
                '''
                index = (neighbor[1].x * DIM) + neighbor[1].y
                item = draw.c.find_withtag(str(index + 1))
                draw.c.itemconfig(item, fill='red')
                time.sleep(TIME)
                draw.c.update()
                '''
                neighbor[1].visited = True
                stack.push(node)

        #stack is empty return
        if(stack.size == 0):
            print("Done!")
            return

        #else pop from stack
        random_cell = stack.pop().value
        '''
        index = (random_cell.x * DIM) + random_cell.y
        item = draw.c.find_withtag(str(index + 1))
        draw.c.itemconfig(item, fill='yellow')
        time.sleep(TIME)
        draw.c.update()
        '''

        #make cell unblocked or blocked with a probability
        rand = random.randint(1, 10)
        if(rand < 4):
            #mark as blocked
            random_cell.blocked = True
            index = (random_cell.x * DIM) + random_cell.y
            item = draw.c.find_withtag(str(index + 1))
            draw.c.itemconfig(item, fill='black')
            #time.sleep(TIME)
            #draw.c.update()
        else:
            #mark as unblocked
            random_cell.blocked = False
            '''
            index = (random_cell.x * DIM) + random_cell.y
            item = draw.c.find_withtag(str(index + 1))
            draw.c.itemconfig(item, fill='blue')
            time.sleep(TIME)
            draw.c.update()
            '''

        #move state to neighbor
        state = random_cell


def generate_x():
    x = random.randint(0, DIM - 1)
    return x

def generate_y():
    y = random.randint(0, DIM - 1)
    return y

def grid_init(grid):
        for i in range(DIM):
            for j in range(DIM):
                square = Square(0, i, j)
                grid.environment[i][j] = square

        return grid

#main method
for i in range(1):
    draw.createGrid()
    generate_maze()
    generate_start_and_finish()
    draw.drawGrid()
    #draw.root.after(500, generate_maze)
    #draw.drawGrid()
