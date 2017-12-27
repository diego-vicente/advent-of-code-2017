# Set of directions needed to move the vector.
Directions = {
    'Left': (-1, 0),
    'Right': (1, 0),
    'Up': (0, -1),
    'Down': (0, 1),
}

def main():
    with open('data/diagram.txt', 'r') as f:
        diagram = f.read().splitlines()

    path, steps = traverse_diagram(diagram)
    print('Solution to problem 1 is', str(path))
    print('Solution to problem 2 is', steps)

def traverse_diagram(diagram):
    """Return the nodes by traversing the diagram."""
    direction = 'Down'
    dead_end = False
    path = []
    steps = 0

    # Find the starting point
    x, y = (diagram[0].index('|'), 0)

    while not dead_end:
        steps += 1
        move = Directions[direction]
        x, y = x + move[0], y + move[1]
        next_step = diagram[y][x]

        if next_step == '|' or next_step == '-':
            continue
        elif next_step == '+':
            if direction == 'Left' or direction == 'Right':
                try:
                    direction = 'Down' if diagram[y + 1][x] == '|' else 'Up'
                except IndexError:
                    direction = 'Up'
            elif direction == 'Down' or direction == 'Up':
                try:
                    direction = 'Right' if diagram[y][x + 1] == '-' else 'Left'
                except IndexError:
                    direction = 'Left'
        elif next_step.isalpha():
            path.append(next_step)
        else:
            dead_end = True

    return path, steps





if __name__ == '__main__':
    main()
