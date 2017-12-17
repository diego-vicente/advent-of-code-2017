def generator(n, factor, times):
    """Create a generator defining its initial conditions."""
    for _ in range(times):
        n = (n * factor) % 2147483647
        yield n

def compare_generator(generator_a, generator_b):
    count = 0

    for a, b in zip(generator_a, generator_b):
        if '{:032b}'.format(a)[-16:] == '{:032b}'.format(b)[-16:]:
            count += 1

    return count


def main():
    generator_a = generator(883, 16807, 40000000)
    generator_b = generator(879, 48271, 40000000)

    print(compare_generator(generator_a, generator_b))


if __name__ == '__main__':
    main()
