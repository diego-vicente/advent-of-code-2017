from collections import Counter

def main():
    passphrases = []
    with open('data/passphrases.txt', 'r') as f:
        passphrases = map(lambda x: x.split(), f.readlines())

    passphrases = list(passphrases)

    print('The solution to the first problem is', count_unique(passphrases))
    print('The solution to the second problem is', count_anagrams(passphrases))

def count_unique(passphrases):
    """Count the number of passphrases formed by unique words."""
    valid = 0
    for passphrase in passphrases:
        if len(passphrase) == len(set(passphrase)):
            valid += 1
    return valid

def count_anagrams(passphrases):
    """Count the number of passphrases whose words are not anagrams of each
    other."""
    valid = 0
    for passphrase in passphrases:
        to_tuple_list = lambda x: tuple(sorted(Counter(x).items()))
        anagrams = list(map(to_tuple_list, passphrase))
        if len(anagrams) == len(set(anagrams)):
            valid += 1
    return valid


if __name__ == '__main__':
    main()
