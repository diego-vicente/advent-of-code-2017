from operator import itemgetter
from copy import copy

def main():
    state = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
    prev_states= []
    steps = 0
    while state not in prev_states:
        prev_states.append(copy(state))
        state = redistribute(state)
        steps += 1
    print('Solution to the problem 1 is', steps)

def redistribute(state):
    """Redistribute the blocks from the biggest slot in memory."""
    idx, blocks = max(enumerate(state), key=itemgetter(1))
    state[idx] = 0
    while blocks:
        idx = (idx+1) % len(state)
        state[idx] += 1
        blocks -= 1
    return state

if __name__ == '__main__':
    main()
