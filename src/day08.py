from collections import defaultdict


def main():
    results, maximum = run_instructions('data/instructions.txt')
    print('Solution to problem 1 is', max(results.values()))
    print('Solution to problem 2 is', maximum)

def run_instructions(filename):
    """Run a set of instructions collected in a text file."""
    with open(filename, 'r') as f:
        instructions = f.readlines()

    registers = defaultdict(int)
    maximum = 0

    for instruction in instructions:
        target, op, value, _, lhs, cond, rhs = instruction.split(' ')

        if check_condition(registers[lhs], cond, int(rhs)):
            if op == 'inc':
                registers[target] += int(value)
            elif op == 'dec':
                registers[target] -= int(value)

        maximum = max(max(registers.values()), maximum)

    return registers, maximum

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
