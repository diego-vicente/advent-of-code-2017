from collections import defaultdict


def main():
    results = run_instructions('src/day-8.txt')
    print('Solution to problem 1 is', max(results.values()))

def run_instructions(filename):
    """Run a set of instructions collected in a text file."""
    with open(filename, 'r') as f:
        instructions = f.readlines()

    registers = defaultdict(int)

    for instruction in instructions:
        target, op, value, _, lhs, cond, rhs = instruction.split(' ')

        if check_condition(registers[lhs], cond, int(rhs)):
            if op == 'inc':
                registers[target] += int(value)
            elif op == 'dec':
                registers[target] -= int(value)

    return registers

def check_condition(lhs, cond, rhs):
    """Check if a given condition is true."""
    if cond == '>':
        return lhs > rhs
    if cond == '<':
        return lhs < rhs
    if cond == '>=':
        return lhs >= rhs
    if cond == '<=':
        return lhs <= rhs
    if cond == '==':
        return lhs == rhs
    if cond == '!=':
        return lhs != rhs

if __name__ == '__main__':
    main()
