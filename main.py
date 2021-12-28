import numpy as np
import random

''' 
DONE:
- Make grid object with printing abilities
- Randomly load in existing map

TODO:
- GUI (pygame) to show grid
- user filling in the grid
- check solution 
'''

class Grid():
    def __init__(self):
        self.grid = np.zeros((9,9))

    # file formatted as 81 characters per line, 0 means blank
    def load_grid_from_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            puzzle = lines[random.randint(1,len(lines)-1)].strip("\n")
            puzzle = [list(puzzle[i:i+9]) for i in range(0,len(puzzle),9)]
            self.grid = np.array(puzzle, dtype=np.int8)
    
    # print the grid
    def __repr__(self):
        return str(self.grid)

a = Grid()
print(a)
a.load_grid_from_file("all_17_clue_sudokus.txt")
print(a)

