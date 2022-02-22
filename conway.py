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

now = datetime.today().strftime('%Y-%m-%d')
file = None

class Cell:        
    @staticmethod
    def neighbour_sum(i, j, grid, N, M):
        total = int((grid[i, (j-1)%M] + grid[i, (j+1)%M] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%M] + grid[(i-1)%N, (j+1)%M] +
                         grid[(i+1)%N, (j-1)%M] + grid[(i+1)%N, (j+1)%M])/ON)
        return total

    @staticmethod
    def find(cell, i, j):
        if(cell.i == i and cell.j == j):
            return True
        return False

class Conway:
    def __init__(self, file_name, args):
        self.file_name = file_name
        self.args = args
        self.cells_allive = list()
        self.actual_gen = 0
        self.out = 'output.txt'

        self.total_count = 0
        self.glider_count = 0
        self.spaceship_count = 0
        self.blink_count = 0
        self.toad_count = 0
        self.beacon_count = 0
        self.block_count = 0
        self.beehive_count = 0
        self.loaf_count = 0
        self.boat_count = 0
        self.tub_count = 0

        file = open(self.out, "w")

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

            # Generate empty grid of N * M
            #self.grid = randomGrid(self.N, self.M)
            self.grid = np.zeros(self.N * self.M, dtype=np.int32).reshape(self.M, self.N)

            # Get generations
            self.gens = int(f.readline())
            for line in f:
                s = line.split()
                i, j = int(s[0]), int(s[1])
                self.grid[i, j] = ON
            
            # Open file
            #file.write(f'Simulation at {now}\n')
            #file.write(f'Universe size {self.N} x {self.M}\n')



    def rules(self):
        if (self.actual_gen < self.gens):
            self.actual_gen += 1
            new_grid = self.grid.copy()
            
            for i in range(0, self.N):
                for j in range(0, self.M):
                    ns = Cell.neighbour_sum(i, j, self.grid, self.N, self.M)
                    if (self.grid[i, j] == OFF):
                        if (ns == 3):
                            new_grid[i, j] = ON
                    else:
                        if (ns < 2 or ns > 3):
                            new_grid[i, j] = OFF
            #self.report()
            self.grid[:] = new_grid[:]
            

"""
    def report(self):
        for i in range(0, self.N):
            for j in range(0, self.M):
                # Still lifes
                #block
                if(np.array_equal(self.grid[i:i+4, j:j+4] , block1, equal_nan=True) ):
                    self.block_count+=1
                    total+=1
                # beehive
                if(np.array_equal(self.grid[i:i+5, j:j+6] , beehive1, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+5] , np.rot90(beehive1), equal_nan=True)):
                    self.beehive_count+=1
                    total+=1
                # loaf
                if(np.array_equal(self.grid[i:i+6, j:j+6] , loaf1, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf1), equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf1, 2), equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf1, 3), equal_nan=True)):
                    self.loag_count+=1
                    total+=1
                # boat
                if(np.array_equal(self.grid[i:i+5, j:j+5] , boat1, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat1), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat1, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat1, 3), equal_nan=True)):
                    self.boat_count+=1
                    total+=1
                # tub
                if(np.array_equal(self.grid[i:i+5, j:j+5] , tub1, equal_nan=True) ):
                    self.tub_count+=1
                    total+=1

                # Spaceships
                # Glider
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider1, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1, 3), equal_nan=True)):
                    self.glider_count+=1
                    total+=1
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider2, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2, 3), equal_nan=True)):
                    self.glider_count+=1
                    total+=1
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider3, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3, 3), equal_nan=True)):
                    self.glider_count+=1
                    total+=1
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider4, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4, 3), equal_nan=True)):
                    self.glider_count+=1
                    total+=1

                # Light weight spaceship
                if(np.array_equal(self.grid[i:i+6, j:j+7] , LWS1, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(LWS1), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(LWS1, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(LWS1, 3), equal_nan=True)):
                    self.spaceship_count +=1
                    total+=1
                if(np.array_equal(self.grid[i:i+6, j:j+7] , LWS2, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(LWS2), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(LWS2, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(LWS2, 3), equal_nan=True)):
                    self.spaceship_count +=1
                    total+=1
                if(np.array_equal(self.grid[i:i+6, j:j+7] , LWS3, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(LWS3), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(LWS3, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(LWS3, 3), equal_nan=True)):
                    self.spaceship_count +=1
                    total+=1
                if(np.array_equal(self.grid[i:i+6, j:j+7] , LWS4, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(LWS4), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(LWS4, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(LWS4, 3), equal_nan=True)):
                    self.spaceship_count +=1
                    total+=1

                #Oscilators
                # blinker
                if(np.array_equal(self.grid[i:i+5, j:j+3] , blinker1, equal_nan=True) or np.array_equal(self.grid[i:i+3, j:j+5] , blinker2, equal_nan=True)):
                    self.blink_count+=1
                    total+=1
                #toad
                if(np.array_equal(self.grid[i:i+6, j:j+6] , toad1, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(toad1), equal_nan=True)):
                    self.toad_count+=1
                    total+=1
                if(np.array_equal(self.grid[i:i+4, j:j+6] , toad2, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+4] , np.rot90(toad2), equal_nan=True)):
                    self.toad_count+=1
                    total+=1
                # beacon
                if(np.array_equal(self.grid[i:i+6, j:j+6] , beacon1, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(beacon1), equal_nan=True)):
                    self.beacon_count+=1
                    total+=1
                if(np.array_equal(self.grid[i:i+6, j:j+6] , beacon2, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(beacon2), equal_nan=True)):
                    self.beacon_count+=1
                    total+=1
                
"""



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
    args_buff = None
    if(len(sys.argv) > 1):
        args_buff = sys.argv[1:]

    cw = Conway('config.txt', args_buff)
    cw.config()
    #cw.report()

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
    file.close()

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
"""
cell = Cell(i, j, len(self.cells_allive) - 1)
self.cells_allive.append(cell)
Cell.graph(i, j, self.grid)
"""
