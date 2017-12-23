from collections import defaultdict
from math import ceil, sqrt

class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = defaultdict(int)
        self.ic = 0
        self.mul_count = 0
        self.terminated = False

    def run_instruction(self):
        if not self.ic < len(self.instructions):
            self.terminated = True
            return

        instruction = self.instructions[self.ic]
        code = instruction[:3]

        if code == 'set':
            _, reg, val = instruction.split(' ')
            try:
                self.registers[reg] = int(val)
            except ValueError:
                self.registers[reg] = self.registers[val]

        elif code == 'sub':
            _, reg, val = instruction.split(' ')
            try:
                self.registers[reg] -= int(val)
            except ValueError:
                self.registers[reg] -= self.registers[val]


        elif code == 'mul':
            _, reg, val = instruction.split(' ')
            try:
                self.registers[reg] *= int(val)
            except ValueError:
                self.registers[reg] *= self.registers[val]
            self.mul_count += 1

        elif code == 'jnz':
            _, reg, val = instruction.split(' ')
            try:
                condition = int(reg)
            except ValueError:
                condition = self.registers[reg]

            if condition != 0:
                try:
                    self.ic += int(val)
                except ValueError:
                    self.ic += self.registers[val]
                return

        self.ic += 1

def main():
    with open('src/day-23.txt', 'r') as f:
        instructions = f.read().splitlines()

    program = Program(instructions)

    while not program.terminated:
        program.run_instruction()

    print('Solution to problem 1 is', program.mul_count)

if __name__ == '__main__':
    main()
