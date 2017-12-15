import numpy as np

from day10 import knot_hash

def main():
    grid = generate_grid('stpzcrnm')
    print('Solution to problem 1 is', grid.sum())

def generate_grid(grid_hash):
    """Create a 128x128 grid from a given knot-hash."""
    grid = []
    for i in range(128):
        grid.append(generate_row(i, grid_hash))
    return np.array(grid)

def generate_row(row, grid_hash):
    """Generate a single row from a hash."""
    row_hash = '{}-{}'.format(grid_hash, row)
    return list(map(int, knot_hash(row_hash, output='bin')))

    
if __name__ == '__main__':
   main()
