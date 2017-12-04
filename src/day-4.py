def main():
    passphrases = []
    with open('src/day-4.txt', 'r') as f:
        passphrases = map(lambda x: x.split(), f.readlines())

    print(count_unique(passphrases))

def count_unique(passphrases):
    """Count the number of passphrases formed by unique words."""
    valid = 0
    for passphrase in passphrases:
        if len(passphrase) == len(set(passphrase)):
            valid += 1
    return valid

if __name__ == '__main__':
    main()
