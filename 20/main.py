import re

data = list(open('20\input.txt').readlines())
data = map(lambda l: re.findall(r'(-\d+|\d+)', l), data)

particles = []
for d in data:
    p = {
        "position": {
            "x": int(d[0]),
            "y": int(d[1]),
            "z" : int(d[2])
        },
        "velocity": {
            "x": int(d[3]),
            "y": int(d[4]),
            "z" : int(d[5])
        },
        "acceleration": {
            "x": int(d[6]),
            "y": int(d[7]),
            "z" : int(d[8])
        }
    }
    particles.append(p)

def find_lower_acceleration(particles):
    acc = []
    for p in particles:
        a = p["acceleration"]
        acc.append(abs(a["x"]) + abs(a["y"]) + abs(a["z"]))

    return acc.index(min(acc))

def sort_by_position(particle):
    return particle["position"]["x"], particle["position"]["y"], particle["position"]["z"]

class Simulator():

    def __init__(self, particles):
        self.particles = particles[:]
        self.time = 0

    def simulate(self):
        self.export()

        for i in range(0, 10000):
            self.move()
            self.find_collisions()
            self.export()

    def move(self):
        self.time += 1
        for p in self.particles:
            for dimension in ['x', 'y', 'z']:
                p["velocity"][dimension] += p["acceleration"][dimension]
                p["position"][dimension] += p["velocity"][dimension]

    def find_collisions(self):
        self.particles = sorted(self.particles, key=sort_by_position)
        collisions = []

        index = 0
        while index < len(self.particles):

            inc = 1
            while index + inc < len(self.particles) and \
                    self.is_collision(self.particles[index], self.particles[index + inc]):
                if not index in collisions:
                    collisions.append(index)
                collisions.append(index + inc)
                inc += 1

            index += inc

        for index in reversed(collisions):
            del self.particles[index]

    def is_collision(self, p1, p2):
        return p1["position"]["x"] == p2["position"]["x"] and \
            p1["position"]["y"] == p2["position"]["y"] and \
            p1["position"]["z"] == p2["position"]["z"]
             

    def export(self):
        space = []
        for p in self.particles:
            space.append([p["position"]["x"], p["position"]["y"], p["position"]["z"]]) 
        print '{0} particles >> {1}'.format(len(self.particles), space if len(space) < 10 else 'Too big' ) 

print find_lower_acceleration(particles)

s = Simulator(particles)
s.simulate()