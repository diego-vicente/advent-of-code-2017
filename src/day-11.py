import numpy as np

def main():
    with open('src/day-11.txt', 'r') as f:
        steps = f.read().replace('\n', '').split(',')

    a, b = hex_path(steps)
    print('Solution to problem 1 is', a)
    print('Solution to problem 2 is', b)

def hex_path(steps):
    """Walk a hex-grid path and return the final distance from the origin."""
    current = np.array([0, 0, 0])

    directions = {
        'n'  : np.array([0, 1, -1]),
        's'  : np.array([0, -1, 1]),
        'ne' : np.array([1, 0, -1]),
        'se' : np.array([1, -1, 0]),
        'nw' : np.array([-1, 1, 0]),
        'sw' : np.array([-1, 0, 1]),
    }

    distances = []

    for step in steps:
        current += directions[step]
        distances.append(np.abs(current).sum() / 2)

    return distances[-1], max(distances)

if __name__ == '__main__':
   main()
