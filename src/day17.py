def spinlock(length, insertions):
    """Perform a spinlock"""
    lst = [0]
    current = 0

    for i in range(insertions):
        current = (current + length) % len(lst)
        lst.insert(current + 1, i + 1)
        current += 1

    return lst, current


def simulate_spinlock(length, insertions):
    """Simulate the effects of a spinlock."""
    len_lst = 1
    current = 0
    value_after_0 = None

    for i in range(insertions):
        current = (current + length) % len_lst
        if current + 1 == 1:
            value_after_0 = i + 1
        current += 1
        len_lst += 1

    return value_after_0


def main():
    lst, idx = spinlock(312, 2017)
    print('Solution to problem 1 is', lst[idx + 1])

    value = simulate_spinlock(312, 50000000)
    print('Solution to problem 2 is', value)

if __name__ == '__main__':
    main()
