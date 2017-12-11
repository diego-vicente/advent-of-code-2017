import re

def main():
    print('Solution to problem 1 is', locate_root('src/day-7.txt'))

def parse_line(line):
    """Process a line into tuples."""
    leaf = re.match(r"(\w+) \((\d+)\) -> (.+)", line)
    root = re.match(r"(\w+) \((\d+)\)", line)

    if leaf:
        return leaf.group(1), leaf.group(2), leaf.group(3).split(', ')
    elif root:
        return root.group(1), root.group(2)

def locate_root(filename):
    root_candidates = []
    total_leaves = []

    with open(filename, 'r') as f:
        nodes = f.readlines()

    for node in nodes:
        elements = parse_line(node)
        if len(elements) == 2:
            root, _ = elements
            leaves = None
        elif len(elements) == 3:
            root, _, leaves = elements
            for leaf in leaves:
                if leaf in root_candidates:
                    root_candidates.remove(leaf)
            total_leaves += leaves


        if root not in total_leaves:
            root_candidates.append(root)

    if len(root_candidates) == 1:
        return root_candidates[0]
    else:
        return None

if __name__ == '__main__':
    main()
