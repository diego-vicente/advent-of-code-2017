from itertools import tee

def pairwise(iterable):
    """Traverse a list in contiguous tuples."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    with open('data/day-1.txt') as f:
        captcha = list(f.read().splitlines()[0])

    # Add the first element to the end of the list
    captcha.append(captcha[0])

    print('Solution to problem 1 is', sum_captcha(captcha))

def sum_captcha(captcha):
    """Sum the numbers that are equal to the next one in the captcha."""
    return sum(int(a) for a, b in pairwise(captcha) if a == b)

if __name__ == '__main__':
    main()
