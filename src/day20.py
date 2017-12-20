import re
from collections import defaultdict

class Particle:
    def __init__(self, id, px, py, pz, vx, vy, vz, ax, ay, az):
        self.id = id

        self.px = int(px)
        self.py = int(py)
        self.pz = int(pz)

        self.vx = int(vx)
        self.vy = int(vy)
        self.vz = int(vz)

        self.ax = int(ax)
        self.ay = int(ay)
        self.az = int(az)

    def absolute_acceleration(self):
        """The amount of acceleration from the origin outwards."""
        return abs(self.ax) + abs(self.ay) + abs(self.az)

    def absolute_velocity(self):
        """The amount of velocity from the origin outwards."""
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def move(self):
        """Update the particle properties one tick."""
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az

        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

def simulation(particles, iterations):
    """Run a simulation and return the state of the particles"""
    for t in range(iterations):
        positions = defaultdict(list)

        # Move every particle one tick
        for particle in particles:
            particle.move()
            pos = particle.px, particle.py, particle.pz
            positions[pos].append(particle.id)

        collided = []
        # Check all the collisions:
        for position in positions.values():
            if len(position) > 1:
                collided += position

        particles = list(filter(lambda p: p.id not in collided, particles))

    return particles


def main():
    with open('src/day-20.txt', 'r') as f:
        raw_particles = f.read().splitlines()

    particles = []

    for i, str_particle in enumerate(raw_particles):
        p_group = re.match(
            r"p=<(.+?),(.+?),(.+?)>, v=<(.+?),(.+?),(.+?)>, a=<(.+?),(.+?),(.+?)>",
            str_particle
        )
        particle = Particle( i,
            p_group.group(1), p_group.group(2), p_group.group(3),
            p_group.group(4), p_group.group(5), p_group.group(6),
            p_group.group(7), p_group.group(8), p_group.group(9)
        )

        particles.append(particle)

    print('Solution to problem 1 is', min(particles, key=lambda p: (
        p.absolute_acceleration(),
        p.absolute_velocity()
    )).id)

    particles = simulation(particles, 500)
    print('Solution to problem 2 is', len(particles))

if __name__ == '__main__':
    main()
