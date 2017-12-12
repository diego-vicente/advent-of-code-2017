import numpy as np


def main():
    problem_A, _, _ = knot_hash_round(
        np.arange(256),
        [34, 88, 2, 222, 254, 93, 150, 0, 199, 255, 39, 32, 137, 136, 1, 167],
        0, 0
    )

    print('First solution is', problem_A[0] * problem_A[1])


    problem_B = knot_hash('34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167')
    print('Second solution is', problem_B)


def knot_hash_round(circular_list, lengths, skip_size, pos):
    """Perform a single round of the knot hash."""

    for length in lengths:
        indices = np.arange(pos, pos + length) % len(circular_list)
        circular_list[indices] = circular_list.take(indices)[::-1]
        pos = (pos + length + skip_size) % len(circular_list)
        skip_size += 1

    return circular_list, pos, skip_size

def knot_hash(string):
    """Obtain the knot hash of a certain string"""

    # Obtain the lengths from the ASCII codes
    lengths = list(map(ord, string)) + [17, 31, 73, 47, 23]

    # Initial values of the hash
    c_list = np.arange(256)
    skip_size = 0
    pos = 0

    # Run 64 rounds on the list
    for _ in range(64):
        c_list, pos, skip_size = knot_hash_round(c_list, lengths, skip_size, pos)

    # Compute 16 bins of reduced XOR
    indices = np.arange(0, 255, 16)
    bins = np.bitwise_xor.reduceat(c_list, indices)

    # Return the hexadecimal string representation of the dense hash
    return ''.join('{:02x}'.format(x) for x in bins)




if __name__ == '__main__':
    main()
