import numpy as np

def main():
    with open('src/day-11.txt', 'r') as f:
        steps = f.read().replace('\n', '').split(',')

    print(hex_path(steps))

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

    for step in steps:
        current += directions[step]

    return np.abs(current).sum() / 2

if __name__ == '__main__':
   main()
