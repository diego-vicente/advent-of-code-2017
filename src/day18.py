from collections import defaultdict

class Program:
    def __init__(self, instructions, pid):
        self.instructions = instructions
        self.pid = pid
        self.registers = defaultdict(int)
        self.registers['p'] = pid
        self.ic = 0
        self.last = 0
        self.waiting = False
        self.terminated = False
        self.queue = []

    def run_instruction(self):
        if not self.ic < len(self.instructions):
            self.terminated = True
            return

        instruction = self.instructions[self.ic]
        code = instruction[:3]

        if code == 'snd':
            _, reg = instruction.split(' ')
            self.ic += 1
            return self.registers[reg]

        elif code == 'set':
            _, reg, val = instruction.split(' ')
            try:
                self.registers[reg] = int(val)
            except ValueError:
                self.registers[reg] = self.registers[val]

        elif code == 'add':
            _, reg, val = instruction.split(' ')
            try:
                self.registers[reg] += int(val)
            except ValueError:
                self.registers[reg] += self.registers[val]

        elif code == 'mul':
            _, reg, val = instruction.split(' ')
            try:
                self.registers[reg] *= int(val)
            except ValueError:
                self.registers[reg] *= self.registers[val]

        elif code == 'mod':
            _, reg, val = instruction.split(' ')
            try:
                self.registers[reg] %= int(val)
            except ValueError:
                self.registers[reg] %= self.registers[val]

        elif code == 'rcv':
            _, reg = instruction.split(' ')
            if self.queue:
                self.registers[reg] = self.queue.pop(0)
                self.waiting = False
            else:
                self.waiting = True
                return None

        elif code == 'jgz':
            _, reg, val = instruction.split(' ')
            try:
                condition = int(reg)
            except ValueError:
                condition = self.registers[reg]

            if condition > 0:
                try:
                    self.ic += int(val)
                except ValueError:
                    self.ic += self.registers[val]
                return None

        self.ic += 1

def proper_duet(instructions):
    """Execute the real duet instructions."""
    program_a = Program(instructions, 0)
    program_b = Program(instructions, 1)

    count = 0

    while not program_a.terminated and not program_b.terminated:
        send_a = program_a.run_instruction()

        if send_a:
            program_b.queue.append(send_a)

        send_b = program_b.run_instruction()

        if send_b:
            program_a.queue.append(send_b)
            count += 1

        if program_a.waiting and program_b.waiting:
            program_a.terminated = True
            program_b.terminated = True
        elif program_a.waiting and program_b.terminated:
            program_a.terminated = True
        elif program_b.waiting and program_a.terminated:
            program_b.terminated = True

    return count


def naive_duet(instructions):
    """Execute a set of duet instructions without reading the docs."""
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

    print('Solution to problem 1 is', naive_duet(instructions))
    print('Solution to problem 2 is', proper_duet(instructions))

if __name__ == '__main__':
    main()
