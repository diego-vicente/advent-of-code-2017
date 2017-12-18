from collections import defaultdict

def duet(instructions):
    """Execute a set of duet instructions."""
    registers = defaultdict(int)
    ic = 0
    last = 0

    while ic < len(instructions):
        instruction = instructions[ic]
        code = instruction[:3]

        if code == 'snd':
            _, reg = instruction.split(' ')
            last = registers[reg]

        elif code == 'set':
            _, reg, val = instruction.split(' ')
            try:
                registers[reg] = int(val)
            except ValueError:
                registers[reg] = registers[val]

        elif code == 'add':
            _, reg, val = instruction.split(' ')
            try:
                registers[reg] += int(val)
            except ValueError:
                registers[reg] += registers[val]

        elif code == 'mul':
            _, reg, val = instruction.split(' ')
            try:
                registers[reg] *= int(val)
            except ValueError:
                registers[reg] *= registers[val]

        elif code == 'mod':
            _, reg, val = instruction.split(' ')
            try:
                registers[reg] %= int(val)
            except ValueError:
                registers[reg] %= registers[val]

        elif code == 'rcv':
            _, reg = instruction.split(' ')
            if registers[reg] and last:
                return last

        elif code == 'jgz':
            _, reg, val = instruction.split(' ')
            if registers[reg]:
                try:
                    ic += int(val)
                except ValueError:
                    ic += registers[val]
                continue

        ic += 1

    return None

def main():
    with open('src/day-18.txt', 'r') as f:
        instructions = f.read().splitlines()

    print(duet(instructions))

if __name__ == '__main__':
    main()
