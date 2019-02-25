from Grid import Grid
from Square import Square
from Frontier import Frontier
from Node import Node
from MinHeap import MinHeap
import draw
import random
from settings import *
import time
import math

def generate_start_and_finish():
    #choose initial cell
    x1 = generate_x()
    y1 = generate_y()
    index = (x1 * DIM) + y1
    item = draw.c.find_withtag(str(index + 1))
    draw.c.itemconfig(item, fill='green')
    pointA = (x1,y1)

    #choose target cell
    x2 = generate_x()
    y2 = generate_y()
    index = (x2 * DIM) + y2
    item = draw.c.find_withtag(str(index + 1))
    draw.c.itemconfig(item, fill='red')
    pointB = (x2,y2);

    return [pointA, pointB];

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
    cord_arr = generate_start_and_finish()
    startIndex = cord_arr[0]
    endIndex = cord_arr[1]
    grid = grid_init(grid, endIndex);

    grid.environment[startIndex[0]][startIndex[1]].startBlock = True
    grid.environment[endIndex[0]][endIndex[1]].endBlock = True

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
            if(neighbor[1].visited is False and neighbor[1].startBlock is False and neighbor[1].endBlock is False):
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
            break

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
            #random_cell.h_value = float("inf")
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
    forward_a_star(grid, startIndex)

def generate_x():
    x = random.randint(0, DIM - 1)
    return x

def generate_y():
    y = random.randint(0, DIM - 1)
    return y

def grid_init(grid, endIndex):
        for i in range(DIM):
            for j in range(DIM):
                square = Square(0, i, j)
                grid.environment[i][j] = square
                grid.environment[i][j].g_value = 0
                grid.environment[i][j].h_value = manhattan_distance(i, j, endIndex[0], endIndex[1])
                grid.environment[i][j].f_value = grid.environment[i][j].g_value + grid.environment[i][j].h_value
        return grid

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def move_agent(closed_list):
    prev = None
    for node in closed_list:
        if(node.blocked):
            node.h_value = float("inf")
            return prev
        index = (node.x * DIM) + node.y
        item = draw.c.find_withtag(str(index + 1))
        draw.c.itemconfig(item, fill='green')
        time.sleep(TIME)
        draw.c.update()
        prev = node

def forward_a_star(grid, startIndex):
    closed_list = a_star(grid, startIndex)
    while(1):
        new_cell = move_agent(closed_list)
        #AttributeError: 'NoneType' object has no attribute 'x' for following line
        if(new_cell is None):
            break
        newIndex = (new_cell.x, new_cell.y)
        print("start again from x:(" + str(new_cell.x) + ", " + str(new_cell.y) + ")")
        closed_list = a_star(grid, newIndex)

def a_star(grid, startIndex):
    #initialize open and closed list
    open_list = MinHeap()
    closed_list = []
    startingSquare = grid.environment[startIndex[0]][startIndex[1]]
    open_list.insert(startingSquare)


    while(open_list.size is not 0):
        #pop square from open list
        square = open_list.pop()
        #add to closed list
        closed_list.append(square)

        index = (square.x * DIM) + square.y
        item = draw.c.find_withtag(str(index + 1))
        draw.c.itemconfig(item, fill='orange')
        time.sleep(TIME)
        draw.c.update()

        for neighbor in square.children:
            if(neighbor[1].endBlock):
                print("found")
                return closed_list
            #set g value to current g value + 1
            '''index = (neighbor[1].x * DIM) + neighbor[1].y
            item = draw.c.find_withtag(str(index + 1))
            draw.c.itemconfig(item, fill='purple')
            time.sleep(TIME)
            draw.c.update()'''

            neighbor[1].g_value = square.value + 1
            neighbor[1].parent = square
            if(open_list.get(neighbor[1]) is not -1):
                open_list.delete(neighbor[1])
            neighbor[1].f_value = neighbor[1].g_value + neighbor[1].h_value
            open_list.insert(neighbor[1])

    print("not found")
    return None
    '''neighbor[1].g_value = square.g_value + 1
    f_val = neighbor[1].g_value + neighbor[1].h_value
    n_f_value = open_list.get(neighbor[1])
    if(neighbor[1] not in closed_list or n_f_value is not -1 and f_val < n_f_value):
    neighbor[1].f_value = f_val
    open_list.insert(neighbor[1])'''

#main method
for i in range(1):
    draw.createGrid()
    generate_maze()
    draw.drawGrid()
    draw.root.after(500, generate_maze)
    #draw.drawGrid()
