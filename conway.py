"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

class Conway:
    def __init__(self, file_name, args):
        self.file_name = file_name
        self.args = args
        self.cells_allive = list()

    class Cell:
        def __init__(self, i, j):
            self.i = i
            self.j = j
        def __str__(self):
            print("i: %d, j: %d" % (self.i, self.j))
        def graph(self, grid):
            grid[self.i, self.j] = 1
        def neighbour_sum(self, grid, N, M):
            i = self.i
            j = self.j

            total = int((grid[i, (j-1)%M] + grid[i, (j+1)%M] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%M] + grid[(i-1)%N, (j+1)%M] +
                         grid[(i+1)%N, (j-1)%M] + grid[(i+1)%N, (j+1)%M]))
            return total

    # read config file
    def config(self):
        with open(self.file_name) as f:
            if (self.args):
                self.N = int(self.args[0])
                self.M = int(self.args[1])

                f.readline().split()
            else:
                s = f.readline().split()

                # Read widht and height
                self.N = int(s[0])
                self.M = int(s[1])

            # Get generations
            self.gens = f.readline()
            for line in f:
                s = line.split()
                cell = self.Cell(int(s[0]),int(s[1]))
                self.cells_allive.append(cell)

            # Generate empty grid of N * M
            #self.grid = randomGrid(self.N, self.M)
            self.grid = np.zeros(self.N * self.M).reshape(self.M, self.N)
            
            # Graph cells allive
            for cell in self.cells_allive:
                cell.graph(self.grid)

    def rules(self):
        for cell in self.cells_allive:
            print('neighbour sum: %d' % cell.neighbour_sum(self.grid, self.N, self.M))

def randomGrid(N, M):
    """returns a grid of NxM random values"""
    return np.random.choice(vals, N*M, p=[0.2, 0.8]).reshape(N, M)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)""" 
    glider = np.array([[0,    0, 255], 
                        [255,  0, 255], 
                        [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    args_buff = None
    if(len(sys.argv) > 1):
        args_buff = sys.argv[1:]
    
    cw = Conway('config.txt', args_buff)
    cw.config()
    cw.rules()

    # set animation update interval
    updateInterval = 50

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(cw.grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, cw.grid, cw.N,),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()

    """
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    
    # set grid size
    N = 100
    M = 100
        
    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    grid = randomGrid(N,M)
    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #WaddGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()
    """

# call main
if __name__ == '__main__':
    main()
