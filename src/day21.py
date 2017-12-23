import numpy as np

def main():
    rules = read_rules('src/day-21.txt')
    string = '.#./..#/###'
    image = np.array(list(map(list, string.split('/'))))
    for _ in range(5):
        image = expand(rules, image)

    unique, counts = np.unique(image, return_counts=True)
    counts = dict(zip(unique, counts))

    print('Solution to problem 1 is', counts['#'])

    for _ in range(13):
        image = expand(rules, image)

    unique, counts = np.unique(image, return_counts=True)
    counts = dict(zip(unique, counts))

    print('Solution to problem 2 is', counts['#'])

def read_rules(filename):
    """Process the file containing the rules."""
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    rules = {}
    for line in lines:
        # Parse each line to obtain the key and value
        key, value = line.split(' => ')
        value = np.array(list(map(list, value.split('/'))))
        key = np.array(list(map(list, key.split('/'))))

        # Add to the rules all the possible substitutions
        for k in [0, 1, 2, 3]:
            mat = np.rot90(key, k=k)
            rules[tuple(mat.flatten())] = value
            rules[tuple(np.flipud(mat).flatten())] = value

    return rules

def substitution(rules, matrix):
    """Get the substitution of a matrix."""
    return rules[tuple(matrix.flatten())]

def expand(rules, image):
    """Expand an image using the rules"""
    size = image.shape[0]
    cs = 2 if size % 2 == 0 else 3
    n_chunks = size // cs

    next_image = []
    for i in range(n_chunks):
        row = []
        for j in range(n_chunks):
            window = image[i*cs : (i+1)*cs, j*cs : (j+1)*cs]
            subs = substitution(rules, window)
            row.append(subs)
        next_image.append(np.hstack(row))

    return np.vstack(next_image)


if __name__ == '__main__':
   main()
