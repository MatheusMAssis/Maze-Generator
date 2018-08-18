import random as rd
import numpy as np
import matplotlib.pyplot as pyplot
from queue import PriorityQueue

#--- changing priority queue a little bit ---#
#--- the only significant change is that you enter (item, value) and receive item ---#

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


#--- Maze Generator using Randomized Prim's Algorithm ---#

#--- every point in the grid is a wall that can turn into a path ---#
#--- to do that, is easier using booleans and classes.           ---#
        
class Wall:
    
    def __init__(self, x, y):
        self.is_visited = False
        self.position = [x, y]
        self.is_path = False
        self.neighbors = []
        self.weight = rd.randint(1,100)
        self.open_neighbors = 0
    
    #--- simple function that returns all neighbors of one position in grid ---#
    
    def gen_neighbors(self, x, y, grid):    
        lines = len(grid)
        columns = len(grid[0])
        
        #--- if it's on the border of the grid, we add two or three neighbors. Else, we add four neighbors ---#
        
        if x == lines - 1:
            self.neighbors.append(grid[x - 1][y]) #--- upper ---#
        elif x == 0:
            self.neighbors.append(grid[x + 1][y]) #--- lower ---#
        else:
            self.neighbors.append(grid[x - 1][y])
            self.neighbors.append(grid[x + 1][y])
            
        if y == columns - 1:
            self.neighbors.append(grid[x][y - 1]) #--- left  ---#
        elif y == 0:
            self.neighbors.append(grid[x][y + 1]) #--- right ---#
        else:
            self.neighbors.append(grid[x][y - 1])
            self.neighbors.append(grid[x][y + 1])      
    
    #--- count the number of paths neighbors ---#
    
    def count_open_neigh(self):
        
        for neigh in self.neighbors:
            if neigh.is_path:
                self.open_neighbors += 1
    
    #--- if it's a path, returns 0; if it's a wall, return 1 ---#
    
    def draw(self):
        if self.is_path:
            return 0
        else:
            return 1
            

def make_maze(x, y):

    wall_list = MyPriorityQueue()
    
    #--- coloring the maze ---#
    
    palletes =  {"maze":  np.array([[1.0, 1.0, 1.0],     #--- 0 = white (path) ---#
                                    [0.0, 0.0, 0.0],     #--- 1 = black (wall) ---#
                                    [0.0, 1.0, 0.0],     #--- 2 = green (init) ---#
                                    [1.0, 0.0, 0.0]])}   #--- 3 = red (target) ---#
    
    def create_image(boolean_array, palette_name):
        return palletes[palette_name][boolean_array.astype(int)]
    
    #--- using three matrix, it was easier to localize whe points that I needed during the code ---#
    
    grid = [[Wall(i, j) for j in range(y)] for i in range(x)]  #---  to get track of all objects   ---#
    matrix = [[j for j in range(y)] for i in range(x)]         #---         to be drawn            ---#
    matrix_weight = [[j for j in range(y)] for i in range(x)]  #--- matrix with all objects weight ---#
    
    for i in range(x):
        for j in range(y):
            matrix_weight[i][j] = grid[i][j].weight
    
    #--- generating all neighbors for all walls on grid ---#
    
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x - 1 or j == 0 or j == y - 1: #--- if it's in the borders ---#
                grid[i][j].is_visited = True
            grid[i][j].gen_neighbors(i, j, grid)
    
    
    #--- using Randomized Prim's Algorithm to create Maze ---#
    
    first_cell = grid[1][1] #--- starting point ---#
    first_cell.is_path = True
    first_cell.is_visited = True
    
    for neigh in first_cell.neighbors:
        if not neigh.is_visited:
            wall_list.put(neigh, neigh.weight)
    
    while not wall_list.empty():
        cell = wall_list.get()
        cell.count_open_neigh()
        if cell.open_neighbors <= 1: #--- if it has less than 1 adjacent neighbor that is a path ---#
            cell.is_path = True
            cell.is_visited = True
            if cell.position[1] == 1 or cell.position[1] == y - 2:
                last_cell = cell #--- the last cell that is in the border to turn into a path is the target point in the maze ---#
            for neigh in cell.neighbors:
                if not neigh.is_visited:
                    if neigh.open_neighbors <= 1:
                        wall_list.put(neigh, neigh.weight)
        
    #--- drawing Maze as a matrix (0 - path; 1 - wall) ---#
    
    for i in range(x):
        for j in range(y):
            matrix[i][j] = grid[i][j].draw()
    
    matrix[1][0] = 2                                                   #--- entrance point = green ---#   
    if last_cell.position[1] == 1:                                     #---    exit point = red    ---#                                 
        matrix[last_cell.position[0]][last_cell.position[1] - 1] = 3
    else:
        matrix[last_cell.position[0]][last_cell.position[1] + 1] = 3
    
    #--- turning matrix into numpy array ---#
            
    maze = np.array([np.array(i) for i in matrix])
    
    #--- printing the size of maze (without the borders) ---#
    
    print("  Real Size:", x-2,"x",y-2)
    
    #--- ploting Maze ---#
    
    image = create_image(boolean_array=maze, palette_name='maze')
    pyplot.figure(figsize=(16, 8))
    pyplot.imshow(image, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()
    
    return matrix, last_cell
