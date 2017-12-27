def main():
    with open('data/firewall.txt', 'r') as f:
        lines = f.readlines()

    firewall = []
    for line in lines:
        layer, depth = line.split(': ')
        firewall.append((int(layer), int(depth)))

    print('Solution to problem 1 is', severity(firewall))

    wait = 0
    while caught(firewall, wait):
        wait += 1

    print('Solution to problem 2 is', wait)

def severity(firewall):
    """Compute the severity of a run through the firewall."""
    severity = 0

    for layer, depth in firewall:
        # Offset is necessary to compute the positions bouncing
        offset = layer % ((depth - 1) * 2)
        # The position of the guard at a layer when we arrive
        guard = 2 * (depth - 1) - offset if offset > depth - 1 else offset

        if guard == 0:
            severity += depth * layer

    return severity

def caught(firewall, wait):
    """Compute if you get caught after waiting for the run in a firewall."""
    for layer, depth in firewall:
        # Offset is necessary to compute the positions bouncing
        offset = (wait + layer) % ((depth - 1) * 2)
        # The position of the guard at a layer when we arrive
        guard = 2 * (depth - 1) - offset if offset > depth - 1 else offset

        if guard == 0:
            return True

    return False


if __name__ == '__main__':
    main()
