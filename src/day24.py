def main():
    components = read_components('data/components.txt')
    start = [(0, 0)]

    bridge = find_strongest([(0, 0)], components)[1:]
    print(bridge)
    print('Solution to problem 1 is', sum([a + b for (a, b) in bridge]))

    bridge = find_longest([(0, 0)], components)[1:]
    print(bridge)
    print('Solution to problem 2 is', sum([a + b for (a, b) in bridge]))


def read_components(filename):
    """Parse the components file into tuples with their strength."""
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    components = list(map(lambda x: tuple(map(int, x.split('/'))), lines))
    components = sorted(components, key=lambda x: x[0]+x[1], reverse=True)
    return components


def find_strongest(bridge, components):
    """Recursive function to generate the strongest brige possible"""
    last = bridge[-1][-1]

    # Find all possible next pieces for the bridge
    fits = [c for c in components if last in c]

    # Termination condition if no more pieces fit
    if not fits:
        return bridge

    candidates = []
    for pos in fits:
        # Correct the order of the piece for the bridge if necessary
        add = (pos[1], pos[0]) if last == pos[1] else pos

        # Create the new bridge and call the function recursively
        branch = bridge.copy()
        branch.append(add)
        candidate = find_strongest(branch, [c for c in components if c != pos])
        candidates.append(candidate)

    # Return the stronger candidate
    strength = lambda b: sum([a + b for (a, b) in b])
    return max(candidates, key=strength)


def find_longest(bridge, components):
    """Recursive function to generate the longest brige possible"""
    last = bridge[-1][-1]

    # Find all possible next pieces for the bridge
    fits = [c for c in components if last in c]

    # Termination condition if no more pieces fit
    if not fits:
        return bridge

    candidates = []
    for pos in fits:
        # Correct the order of the piece for the bridge if necessary
        add = (pos[1], pos[0]) if last == pos[1] else pos

        # Create the new bridge and call the function recursively
        branch = bridge.copy()
        branch.append(add)
        candidate = find_longest(branch, [c for c in components if c != pos])
        candidates.append(candidate)

    # Return the longer (and then stronger) candidate
    strength = lambda b: sum([a + b for (a, b) in b])

    greatest_length = max([len(b) for b in candidates])
    longest = [b for b in candidates if len(b) == greatest_length]

    return max(longest, key=strength)


if __name__ == '__main__':
    main()
