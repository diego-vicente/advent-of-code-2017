from itertools import tee

def pairwise(iterable):
    """Traverse a list in contiguous tuples."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def antipode(lst):
    """Generator that returns the opposing elements in a circular list."""
    half = len(lst) // 2
    for i, elem in enumerate(lst):
        yield elem, lst[(i + half) % len(lst)]


def main():
    with open('data/day-1.txt') as f:
        captcha = list(f.read().splitlines()[0])

    print('Solution to problem 1 is', sum_captcha(captcha))
    print('Solution to problem 2 is', circular_captcha(captcha))


def sum_captcha(captcha):
    """Sum the numbers that are equal to the next one in the captcha."""
    return sum(int(a) for a, b in pairwise(captcha + [captcha[0]]) if a == b)

def circular_captcha(captcha):
    """Sum the numbers that are equal to the next one in the captcha."""
    return sum(int(a) for a, b in antipode(captcha) if a == b)


if __name__ == '__main__':
    main()
