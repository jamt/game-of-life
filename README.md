# game-of-life
Implementation for the Game of Life problem

This is written in Python 2.7.

Run with:
python game-of-life.py [input file path] [number of games] 

Each line of the input file is a grid row.
Ex)
00011000
00000000
11000000

Dead cells are represented by a 0 and live cells are a 1.

The output is a grid printed to the console.

Additional features:
-Support for arbitrary grid sizes.
-Support for multiple generations.

The file TestGame.py contains unit tests for the "rules" and "neighbors" functions.
The "rules" function takes the input grid, the output grid, and a row and column value and calls
the "neighbors" function to get a live neighbor count which is used to apply the game rules for the given cell
and update the output grid.

Run this with:
python TestGame.py
