import re

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

if __name__ == '__main__':
    main()
