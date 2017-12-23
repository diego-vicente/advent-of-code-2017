from collections import defaultdict

# 0 means up, incrementally clockwise
directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0),}

class Carrier:
    """A Carrier traverses the grid expanding the virus."""

    def __init__(self, pos_x, pos_y, grid):
        self.direction = 0
        self.x = pos_x
        self.y = pos_y
        self.grid = grid
        self.bursts = 0

    def move(self):
        """For a carrier in a grid, perform one move."""
        # If infected, turn right and clean the node
        if self.grid[(self.x, self.y)]:
            self.grid[(self.x, self.y)] = False
            self.direction = (self.direction + 1) % 4
        # If not infected, turn left and infect
        else:
            self.grid[(self.x, self.y)] = True
            self.bursts += 1
            self.direction = (self.direction - 1) % 4

        dx, dy = directions[self.direction]
        self.x += dx
        self.y += dy

def main():
    grid = read_grid('src/day-22.txt')
    carrier = Carrier(12, 12, grid)

    for _ in range(10000):
        carrier.move()

    print(carrier.bursts)

def read_grid(filename):
    """Return the known nodes of the grid as a dictionary.

    A default dictionary is the chosen data structure because the grid is
    infinite, so no index bounds should be applied on it. Each position is
    associated with a boolean value: True if it is infected, False otherwise.

    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    grid = defaultdict(bool)

    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            grid[(x, y)] = char == '#'

    return grid

if __name__ == '__main__':
    main()
