from itertools import product

# Set of directions needed to move the vector.
Directions = {
    'Left': (-1, 0),
    'Right': (1, 0),
    'Down': (0, -1),
    'Up': (0, 1),
}

class Vector:
    """A vector of this class moves one step forming a spiral."""
    def __init__(self):
        self.x = 0
        self.y = 0

        self.max_y = 0
        self.min_y = 0
        self.max_x = 0
        self.min_x = 0

        self.value = 1
        self.direction = 'Right'

    def move(self):
        """Move one more step forming a spiral."""
        # Check if the next move has to be left
        if self.x > self.max_x:
            self.direction = 'Up'
            self.max_x = self.x
        # Check if the next move has to be up
        elif self.y > self.max_y:
            self.direction = 'Left'
            self.max_y = self.y
        # Check if the next move has to be l
        elif self.x < self.min_x:
            self.direction = 'Down'
            self.min_x = self.x
        # Check if the next move has to be left
        elif self.y < self.min_y:
            self.direction = 'Right'
            self.min_y = self.y

        self._apply_direction()

    def _apply_direction(self):
        """Move to the direction that the vector is pointing to."""
        # Move the vector
        delta_x, delta_y = Directions[self.direction]
        self.x, self.y = self.x + delta_x, self.y + delta_y

    def distance(self):
        """Return the Manhattan distance of the current vector."""
        return abs(self.x) + abs(self.y)

def main():
    vec = Vector()

    # First problem's solution is to move the vector n times in a spiral.
    n = 361527
    for _ in range(n - 1):
        vec.move()

    print('Solution to the first problem is', vec.distance())

    # Next problem is to sum the adjacent squares in the value.
    squares = {(0, 0): 1}
    vec = Vector()
    while vec.value < n:
        vec.move()
        value = 0
        for adjacent in product((-1, 0, 1), repeat=2):
            square = (vec.x + adjacent[0], vec.y + adjacent[1])
            try:
                value += squares[square]
            except KeyError:
                pass
        vec.value = value
        squares[(vec.x, vec.y)] = value

    print('Solution to the second problem is', vec.value)


if __name__ == '__main__':
    main()
