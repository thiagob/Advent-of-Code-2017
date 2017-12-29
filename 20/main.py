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

print find_lower_acceleration(particles)
