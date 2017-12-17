def generator(n, factor):
    """Create a generator defining its initial conditions."""
    while True:
        n = (n * factor) % 2147483647
        yield n

def multiple_generator(n, factor, multiple):
    """Create a generator checking for multiplie defining."""
    while True:
        n = (n * factor) % 2147483647
        if (n % multiple) == 0:
            yield n

def compare_generator(generator_a, generator_b, pairs):
    """Compare two generators during a given amount of pairs."""
    count = 0

    for _ in range(pairs):
        a, b, = next(generator_a), next(generator_b)
        if a & 0xFFFF == b & 0xFFFF:
            count += 1

    return count

def main():
    generator_a = generator(883, 16807)
    generator_b = generator(879, 48271)

    print('Solution to problem 1 is',
          compare_generator(generator_a, generator_b, 40000000))

    generator_a = multiple_generator(883, 16807, 4)
    generator_b = multiple_generator(879, 48271, 8)

    print('Solution to problem 2 is',
          compare_generator(generator_a, generator_b, 5000000))


if __name__ == '__main__':
    main()
