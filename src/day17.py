def spinlock(length, insertions):
    """Simulate the effects of a spinlock."""
    lst = [0]
    current = 0

    for i in range(insertions):
        current = (current + length) % len(lst)
        lst.insert(current + 1, i + 1)
        current += 1

    return lst, current

def main():
    lst, idx = spinlock(312, 2017)
    print('Solution to problem 1 is', lst[idx + 1])

if __name__ == '__main__':
    main()
