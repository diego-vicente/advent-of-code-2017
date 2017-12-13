def main():
    with open('src/day-13.txt', 'r') as f:
        lines = f.readlines()

    firewall = []
    for line in lines:
        layer, depth = line.split(': ')
        firewall.append((int(layer), int(depth)))

    print(severity(firewall))

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

def test():
    for i in range(20):
        if i % ((3-1)*2) >= 3:
            guard = -(i+2) % 3
        else:
            guard = i % 3
        print(guard)

if __name__ == '__main__':
   main()
