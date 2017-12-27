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
    with open('data/code.txt', 'r') as f:
        instructions = f.read().splitlines()

    program = Program(instructions)

    while not program.terminated:
        program.run_instruction()

    print('Solution to problem 1 is', program.mul_count)
    print('Solution to problem 2 is', program_optimized())

def program_translated():
    """Python equivalent of the Duet code.

    Just never run this code. It is not going to stop. However, it is enough to
    understand that its purpose is to count the number of composite numbers in
    [b, c, 17].

    """
    b = 100 * 67 + 100000
    c = b + 17000
    h = 0

    while True:
        d = 2
        while d != b:
            e = 2
            while e != b:
                if d * e == b:
                    h += 1
                    break
                e += 1
            d += 1
        if b == c:
            return h
        b += 17

def program_optimized():
    """The real Pythonic way to compute the problem 2.

    Compute efficiently the primes up to c, then substract those to get the
    number of composite numbers.

    """
    b = 100 * 67 + 100000
    c = b + 17000

    h = 0
    for n in range(b, c+1, 17):
        for k in range(2 , ceil(sqrt(n))):
            if n % k == 0:
                h += 1
                break

    return h




if __name__ == '__main__':
    main()
