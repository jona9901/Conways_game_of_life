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

fp = None

input_file = 'configs/config1.txt' 
output_file = 'outputs/output1.txt'
now = datetime.today().strftime('%Y-%m-%d')

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
        self.out = output_file 

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

            
            fp.write(f"Simulation at {now}\n")
            fp.write(f"Universe size {self.N} x {self.M}\n")

            # Generate empty grid of N * M
            #self.grid = randomGrid(self.N, self.M)
            self.grid = np.zeros(self.N * self.M, dtype=np.int32).reshape(self.M, self.N)

            # Get generations
            self.gens = int(f.readline())
            for line in f:
                s = line.split()
                i, j = int(s[0]), int(s[1])
                self.grid[i, j] = ON
            
    def rules(self):
        if (self.actual_gen < self.gens):
            self.actual_gen += 1
            print(f'Gen: {self.actual_gen}')
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
            self.report()

            self.write_to_file()
            
            self.grid[:] = new_grid[:]
            
    def write_to_file(self):
        fp.write(f'Iteration: {self.actual_gen}\n')
        fp.write('------------------------------------\n')
        if(self.total_count!=0):
            fp.write(tabulate([['Block', self.block_count, self.block_count*100/self.total_count], ['Beehive', self.beehive_count, self.beehive_count*100/self.total_count], ['Loaf', self.loaf_count, self.loaf_count*100/self.total_count], ['Boat', self.boat_count, self.boat_count*100/self.total_count], ['Tub', self.tub_count, self.tub_count*100/self.total_count], ['Blinker', self.blink_count, self.blink_count*100/self.total_count], ['Toad', self.toad_count, self.toad_count*100/self.total_count], ['Beacon', self.beacon_count, self.beacon_count*100/self.total_count], ['Glider', self.glider_count, self.glider_count*100/self.total_count], ['LG sp ship', self.spaceship_count, self.spaceship_count*100/self.total_count]], headers=[' ','Count', 'Percent'], tablefmt='orgtbl'))
        else:
            fp.write(tabulate([['Block', self.block_count, 0], ['Beehive', self.beehive_count, 0], ['Loaf', self.loaf_count, 0], ['Boat', self.boat_count, 0], ['Tub', self.tub_count, 0], ['Blinker', self.blink_count, 0], ['Toad', self.toad_count, 0], ['Beacon', self.beacon_count, 0], ['Glider', self.glider_count, 0], ['LG sp ship', self.spaceship_count, 0]], headers=[' ','Count', 'Percent'], tablefmt='orgtbl'))
        fp.write('\n')
        fp.write('------------------------------------\n')

    def report(self):
        for i in range(0, self.N):
            for j in range(0, self.M):
                # Still lifes
                #block
                if(np.array_equal(self.grid[i:i+4, j:j+4] , block, equal_nan=True) ):
                    self.block_count+=1
                    self.total_count+=1
                    continue
                # beehive
                if(np.array_equal(self.grid[i:i+5, j:j+6] , beehive, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+5] , np.rot90(beehive), equal_nan=True)):
                    self.beehive_count+=1
                    self.total_count+=1
                    continue
                # loaf
                if(np.array_equal(self.grid[i:i+6, j:j+6] , loaf, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf), equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf, 2), equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(loaf, 3), equal_nan=True)):
                    self.loaf_count+=1
                    self.total_count+=1
                    continue
                # boat
                if(np.array_equal(self.grid[i:i+5, j:j+5] , boat, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(boat, 3), equal_nan=True)):
                    self.boat_count+=1
                    self.total_count+=1
                    continue
                # tub
                if(np.array_equal(self.grid[i:i+5, j:j+5] , tub, equal_nan=True) ):
                    self.tub_count+=1
                    self.total_count+=1
                    continue

                # Spaceships
                # Glider
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider1, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider1, 3), equal_nan=True)):
                    self.glider_count+=1
                    self.total_count+=1
                    continue
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider2, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider2, 3), equal_nan=True)):
                    self.glider_count+=1
                    self.total_count+=1
                    continue
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider3, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider3, 3), equal_nan=True)):
                    self.glider_count+=1
                    self.total_count+=1
                    continue
                if(np.array_equal(self.grid[i:i+5, j:j+5] , glider4, equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4, 2), equal_nan=True) or np.array_equal(self.grid[i:i+5, j:j+5] , np.rot90(glider4, 3), equal_nan=True)):
                    self.glider_count+=1
                    self.total_count+=1
                    continue

                # Light weight spaceship
                if(np.array_equal(self.grid[i:i+6, j:j+7] , lws1, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(lws1), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(lws1, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(lws1, 3), equal_nan=True)):
                    self.spaceship_count +=1
                    self.total_count+=1
                    continue
                if(np.array_equal(self.grid[i:i+6, j:j+7] , lws2, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(lws2), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(lws2, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(lws2, 3), equal_nan=True)):
                    self.spaceship_count +=1
                    self.total_count+=1
                    continue
                if(np.array_equal(self.grid[i:i+6, j:j+7] , lws3, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(lws3), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(lws3, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(lws3, 3), equal_nan=True)):
                    self.spaceship_count +=1
                    self.total_count+=1
                    continue
                if(np.array_equal(self.grid[i:i+6, j:j+7] , lws4, equal_nan=True) or np.array_equal(self.grid[i:i+7, j:j+6] , np.rot90(lws4), equal_nan=True) or np.array_equal( self.grid[i:i+6, j:j+7] , np.rot90(lws4, 2), equal_nan=True) or np.array_equal( self.grid[i:i+7, j:j+6] , np.rot90(lws4, 3), equal_nan=True)):
                    self.spaceship_count +=1
                    self.total_count+=1
                    continue

                #Oscilators
                # blinker
                if(np.array_equal(self.grid[i:i+5, j:j+3] , blinker1, equal_nan=True) or np.array_equal(self.grid[i:i+3, j:j+5] , blinker2, equal_nan=True)):
                    self.blink_count+=1
                    self.total_count+=1
                    continue
                #toad
                if(np.array_equal(self.grid[i:i+6, j:j+6] , toad1, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(toad1), equal_nan=True)):
                    self.toad_count+=1
                    self.total_count+=1
                    continue
                if(np.array_equal(self.grid[i:i+4, j:j+6] , toad2, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+4] , np.rot90(toad2), equal_nan=True)):
                    self.toad_count+=1
                    self.total_count+=1
                    continue
                # beacon
                if(np.array_equal(self.grid[i:i+6, j:j+6] , beacon1, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(beacon1), equal_nan=True)):
                    self.beacon_count+=1
                    self.total_count+=1
                    continue
                if(np.array_equal(self.grid[i:i+6, j:j+6] , beacon2, equal_nan=True) or np.array_equal(self.grid[i:i+6, j:j+6] , np.rot90(beacon2), equal_nan=True)):
                    self.beacon_count+=1
                    self.total_count+=1
                    continue
	



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
    global fp
    global parser
    

    args_buff = None
    if(len(sys.argv) > 1):
        args_buff = sys.argv[1:]

    cw = Conway(input_file, args_buff)
    fp = open(cw.out, "w")
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
    fp.close()

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
