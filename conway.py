#!/usr/bin/env python3
"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

from datetime import datetime
from tabulate import tabulate

from patterns import *

ON = 255
OFF = 0
vals = [ON, OFF]

class Cell:
    def __init__(self, i, j, pos):
        self.i = i
        self.j = j
        self.pos = pos
    def __str__(self):
        print("i: %d, j: %d" % (self.i, self.j))
    def ij(self):
        return [self.i, self.j]
    def kill_cell(self, grid, cells_alive):
        grid[self.i, self.j] = OFF
        cells_alive.remove(self)

    @staticmethod
    def graph(i, j, grid):
        grid[i, j] = ON
        
    @staticmethod
    def neighbour_sum(i, j, grid, N, M):
        total = int((grid[i, (j-1)%M] + grid[i, (j+1)%M] +
                     grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                     grid[(i-1)%N, (j-1)%M] + grid[(i-1)%N, (j+1)%M] +
                     grid[(i+1)%N, (j-1)%M] + grid[(i+1)%N, (j+1)%M]))
        return total // ON

class Conway:
    def __init__(self, file_name, args):
        self.file_name = file_name
        self.args = args
        self.cells_allive = list()
        self.actual_gen = 0

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
            self.gens = int(f.readline())
            for line in f:
                s = line.split()
                cell = Cell(int(s[0]),int(s[1]), len(self.cells_allive) - 1)
                self.cells_allive.append(cell)

            # Generate empty grid of N * M
            #self.grid = randomGrid(self.N, self.M)
            self.grid = np.zeros(self.N * self.M).reshape(self.M, self.N)
            
            # Graph cells allive
            for cell in self.cells_allive:
                i, j = cell.ij()
                Cell.graph(i, j, self.grid)

    def rules(self):
        if (self.actual_gen < self.gens):
            self.actual_gen += 1
            for cell in self.cells_allive:
                i, j = cell.ij()
                ns = cell.neighbour_sum(i, j, self.grid, self.N, self.M)
                if (ns < 2):                # Rule 1    
                    cell.kill_cell(self.grid, self.cells_allive)
                elif (ns > 3):              # Rule 3
                    cell.kill_cell(self.grid, self.cells_allive)
            for i in range(0, self.N):
                for j in range(0, self.M):
                    if (self.grid[i, j] == OFF):
                        ns = cell.neighbour_sum(i, j, self.grid, self.N, self.M)
                        if(ns == 3):
                            cell = Cell(i, j, len(self.cells_allive) - 1)
                            self.cells_allive.append(cell)
                            Cell.graph(i, j, self.grid)

def randomGrid(N, M):
    """returns a grid of NxM random values"""
    return np.random.choice(vals, N*M, p=[0.2, 0.8]).reshape(N, M)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)""" 
    glider = np.array([[0,    0, 255], 
                        [255,  0, 255], 
                        [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, cw):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 

    cw.rules()
    newGrid = cw.grid.copy()
    # TODO: Implement the rules of Conway's Game of Life

    # update data
    img.set_data(newGrid)
    cw.grid[:] = newGrid[:]
    return img,

# main() function
def main():
    osci = Oscilator()
    glid = Glider()
    lws = LWS()

    args_buff = None
    if(len(sys.argv) > 1):
        args_buff = sys.argv[1:]
    
    cw = Conway('config.txt', args_buff)
    cw.config()

    # set animation update interval
    updateInterval = 50

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(cw.grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, cw),
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
