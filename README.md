#The Game Of Life
1The game of life is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

The game is a zero-player game. It's evolution is determined by its initial state, requiring no furder input.

One interacts with the game of life by creating a initial configuration and observing how it evolves.

##RULES

The universe of GoL is an infinite, two-dimensional orthogonbal grid of square cells, each of which is in one of two possible states, alive or dead.
Every cell interacts with its eight neighbours (cells that are horizontally, vertically or diagonally adjacent), at each step in time.
The following transitions occur:
    # Any live cell with fewer than two live neighbours dies, underpopulation.
    # Any live cell with two orthree live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, overpopulation.
    # Any cell with exactly three live neighbours becomes a live cell, reproduction.


These rules can be considered into the following:
    # Any live cell with two or three neighbors survives.
    # Any dead cell with three live neighbor becomes a live cell.
    # All other lvie cells die in the next generation. Similarly, all other dead cells stay dead.


##CONFIGURATIONS

Common patter types:

    # Still lifes   -   Do not change from one generation to the next.
    # Oscillators   -   Return to their initial state after a finite number of generations.
    # Spaceships    -   Translate themselves across the grid.


##How to use:

python3 conawys.py N M

where N and M are the widht and height

or 

python3 conways.py


The second option takes the N and M values from the 'config.txt' file
