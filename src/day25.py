from collections import defaultdict

class TuringMachine:
    """A Turing machine, following the given blueprints."""
    def __init__(self):
        self.cursor = 0
        self.tape = defaultdict(int)
        self.state = 'A'

    def step(self):
        """Encode the finite state machine and cursor movement."""
        if self.state == 'A':
            if self.tape[self.cursor] == 0:
                self.tape[self.cursor] = 1
                self.cursor += 1
                self.state = 'B'
            elif self.tape[self.cursor] == 1:
                self.tape[self.cursor] = 0
                self.cursor -= 1
                self.state = 'E'

        elif self.state == 'B':
            if self.tape[self.cursor] == 0:
                self.tape[self.cursor] = 1
                self.cursor -= 1
                self.state = 'C'
            elif self.tape[self.cursor] == 1:
                self.tape[self.cursor] = 0
                self.cursor += 1
                self.state = 'A'

        elif self.state == 'C':
            if self.tape[self.cursor] == 0:
                self.tape[self.cursor] = 1
                self.cursor -= 1
                self.state = 'D'
            elif self.tape[self.cursor] == 1:
                self.tape[self.cursor] = 0
                self.cursor += 1
                self.state = 'C'

        elif self.state == 'D':
            if self.tape[self.cursor] == 0:
                self.tape[self.cursor] = 1
                self.cursor -= 1
                self.state = 'E'
            elif self.tape[self.cursor] == 1:
                self.tape[self.cursor] = 0
                self.cursor -= 1
                self.state = 'F'

        elif self.state == 'E':
            if self.tape[self.cursor] == 0:
                self.tape[self.cursor] = 1
                self.cursor -= 1
                self.state = 'A'
            elif self.tape[self.cursor] == 1:
                self.tape[self.cursor] = 1
                self.cursor -= 1
                self.state = 'C'

        elif self.state == 'F':
            if self.tape[self.cursor] == 0:
                self.tape[self.cursor] = 1
                self.cursor -= 1
                self.state = 'E'
            elif self.tape[self.cursor] == 1:
                self.tape[self.cursor] = 1
                self.cursor += 1
                self.state = 'A'

    def checksum(self):
        """Count the number of 1s in the tape."""
        return sum(self.tape.values())

def main():
    turing = TuringMachine()
    for _ in range(12208951):
        turing.step()

    print('Solution to problem is', turing.checksum())

if __name__ == '__main__':
    main()
