from copy import copy

def main():
    with open('data/maze.txt', 'r') as f:
        maze = list(map(int, f.readlines()))

    print('Solution to problem 1 is', steps_1(copy(maze)))
    print('Solution to problem 2 is', steps_2(maze))

def steps_1(maze):
    """Steps taken to solve the maze using rules in problem 1."""
    current = 0
    steps = 0

    while current < len(maze):
        offset = maze[current]
        maze[current] += 1
        current += offset
        steps += 1

    return steps

def steps_2(maze):
    """Steps taken to solve the maze using rules in problem 2."""
    current = 0
    steps = 0
    offset = 0

    while current < len(maze):
        offset = maze[current]
        if maze[current] >= 3:
            maze[current] -= 1
        else:
            maze[current] += 1
        current += offset
        steps += 1

    return steps


if __name__ == '__main__':
    main()
