import numpy as np


def main():
    problem_A = knot_hash_round(
        [34, 88, 2, 222, 254, 93, 150, 0, 199, 255, 39, 32, 137, 136, 1, 167]
    )
    print('First solution is', problem_A[0] * problem_A[1])


def knot_hash_round(lengths):
    """Perform a single round of the knot hash."""
    circular_list = np.arange(256)

    skip_size = 0
    pos = 0

    for length in lengths:
        indices = np.arange(pos, pos + length) % len(circular_list)
        circular_list[indices] = circular_list.take(indices)[::-1]
        pos = (pos + length + skip_size) % len(circular_list)
        skip_size += 1

    return circular_list


if __name__ == '__main__':
    main()
