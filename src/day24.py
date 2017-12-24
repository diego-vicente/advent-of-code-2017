def main():
    components = read_components('src/day-24.txt')
    bridge = build_bridge(components)
    strength = sum([a + b for (a, b) in bridge])
    print('Solution to problem 1 is', strength(bridge))

def read_components(filename):
    """Parse the components file into tuples with their strength."""
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    components = list(map(lambda x: tuple(map(int, x.split('/'))), lines))
    components = sorted(components, key=lambda x: x[0]+x[1], reverse=True)
    return components

def build_bridge(components):
    """Build the stronger bridge possible with a given set of pieces."""
    start = [(0, 0)]

    # Recursively build the bridge
    bridge = find_stronger(start, components)

    return bridge[1:]

def find_stronger(bridge, components):
    """Recursive function to generate the stronger brige possible"""
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
        candidate = find_stronger(branch, [c for c in components if c != pos])
        candidates.append(candidate)

    # Return the stronger candidate
    strength = lambda b: sum([a + b for (a, b) in b])
    return max(candidates, key=strength)


if __name__ == '__main__':
    main()
