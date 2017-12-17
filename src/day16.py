import re

def main():
    with open('src/day-16.txt', 'r') as f:
        moves = f.read().split(',')

    final = dance(moves)
    print('Solution to Problem 1 is', final)

    party = None
    positions = []
    iterations = 1000000000000

    for i in range(iterations):
        party = dance(moves, party)
        if party in positions:
            cycle_length = i - positions.index(party)
            cycled_final = (iterations - 1) % cycle_length
            party = positions[cycled_final]
            break
        positions.append(party)

    print('Solution to Problem 2 is', party)


def dance(moves, party=None):
    """Perform a list of moves on the party."""
    if not party:
        party = list('abcdefghijklmnop')
    else:
        party = list(party)

    for move in moves:
        spin =     re.match(r"s(.+)", move)
        exchange = re.match(r"x(.+)/(.+)", move)
        partner =  re.match(r"p(.+)/(.+)", move)

        if spin:
            idx = int(spin.group(1))
            party = party[-idx:] + party[:-idx]
        elif exchange:
            a, b = exchange.group(1), exchange.group(2)
            idx_a, idx_b = int(a), int(b)
            party[idx_a], party[idx_b] = party[idx_b], party[idx_a]
        elif partner:
            a, b = partner.group(1), partner.group(2)
            idx_a = party.index(a)
            idx_b = party.index(b)
            party[idx_a], party[idx_b] = party[idx_b], party[idx_a]

    return ''.join(party)

if __name__ == '__main__':
    main()
