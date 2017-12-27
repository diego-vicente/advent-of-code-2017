import numpy as np

from itertools import product


def main():
    input_list = np.fromfile('data/spreadsheet.txt', sep='\t', dtype=np.int32)
    input_list = input_list.reshape(16,16)
    print('Problem 1 solution is {}'.format(checksum(input_list)))
    print('Problem 2 solution is {}'.format(evensum(input_list)))

def checksum(arr):
    """First part of the problem"""
    return (np.max(arr, axis=1) - np.min(arr, axis=1)).sum()

def evensum(arr):
    """Second part of the problem"""
    return np.apply_along_axis(find_multiples, 1, arr).sum()

def find_multiples(row):
    """Returns the result of the two evenly divisible numbers of an array"""
    for i, j in product(row, repeat=2):
        if not i == j and i % j == 0:
            return i // j

if __name__ == '__main__':
    main()
