import re


class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

def main():
    root = build_tree('data/tree.txt')
    print('Solution to problem 1 is', root.name)
    balance_weigths(root)


def build_tree(filename):
    """Parse a text file and build the associated tree."""
    root_candidates = []
    total_leaves = []
    node_dict = {}

    # Read file
    with open(filename, 'r') as f:
        raw_nodes = f.readlines()

    # Parse lines and locate root
    for raw_node in raw_nodes:
        elements = parse_line(raw_node)
        if len(elements) == 2:
            name, weight = elements
            leaves = None
        elif len(elements) == 3:
            name, weight, leaves = elements
            for leaf in leaves:
                if leaf in root_candidates:
                    root_candidates.remove(leaf)
            total_leaves += leaves

        if name not in total_leaves:
            root_candidates.append(name)

        node_dict[name] = Node(name, int(weight), leaves)

    # Build tree recursively from root
    root = node_dict[root_candidates[0]]
    connect_children(root, node_dict)

    return root


def connect_children(father, node_dict):
    """Recursively build a tree from parsed lines."""
    if father.children:
        father.children = list(
            map(lambda x: node_dict[x], father.children)
        )

        for child in father.children:
            connect_children(child, node_dict)


def parse_line(line):
    """Process a line into tuples."""
    leaf = re.match(r"(\w+) \((\d+)\) -> (.+)", line)
    name = re.match(r"(\w+) \((\d+)\)", line)

    if leaf:
        return leaf.group(1), leaf.group(2), leaf.group(3).split(', ')
    elif name:
        return name.group(1), name.group(2)


def balance_weigths(node):
    """Locate the the problematic node and fix the weights recursively."""
    weights = []
    if not node.children:
        return node.weight

    for child in node.children:
        weights.append(balance_weigths(child))

    if not len(set(weights)) == 1:
        print('Unbalanced node: ', weights)
        print(list(map(lambda x: x.weight, node.children)))
        return node.weight + sorted(weights)[0] * len(weights)

    return node.weight + sum(weights)

if __name__ == '__main__':
    main()
