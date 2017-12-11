def main():
    score, garbage = compute_score('src/day-9.txt')
    print('Solution for Problem 1 is', score)
    print('Solution for Problem 2 is', garbage)

def compute_score(filename):
    """Read a file containing a stream of characters and return its score."""
    with open(filename, 'r') as f:
        stream = f.read()

    depth = 0
    score = 0
    garbage = 0
    in_garbage = False
    ignore = False

    for character in stream:
        if ignore:
            ignore = False
        elif character == '!':
            ignore = True
        elif character == '>' and in_garbage:
            in_garbage = False
        elif character == '<' and not in_garbage:
            in_garbage = True
        elif in_garbage:
            garbage += 1
            continue
        elif character == '{' and not in_garbage:
            score += 1 + depth
            depth += 1
        elif character == '}':
            depth -= 1

    return score, garbage


if __name__ == '__main__':
    main()
