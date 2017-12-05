def main():
    with open('src/maze.txt', 'r') as f:
        maze = map(int, f.readlines())

    print('Solution to problem 1 is', steps_1(list(maze)))

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


if __name__ == '__main__':
    main()
