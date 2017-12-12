data = list(open('11\input.txt').readlines())
data = data[0].strip().split(',')

movements = {
    "n" : {
        "x": -1,
        "y": 1,
        "z": 0
    },
    "ne" : {
        "x": 0,
        "y": 1,
        "z": -1
    },
    "nw" : {
        "x": -1,
        "y": 0,
        "z": 1
    },
    "s" : {
        "x": 1,
        "y": -1,
        "z": 0
    },
    "se" : {
        "x": 1,
        "y": 0,
        "z": -1
    },
    "sw" : {
        "x": 0,
        "y": -1,
        "z": 1
    }
}

class Grid():

    def __init__(self):
        self.reset()
        self.max_distance = 0

    def reset(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def get_distance(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) / 2

    def move(self, steps):
        for step in steps:
            self.x += movements[step]["x"]
            self.y += movements[step]["y"]
            self.z += movements[step]["z"]

            if self.get_distance() > self.max_distance:
                self.max_distance = self.get_distance()

samples = [
    ["ne", "ne", "ne"],
    ["ne", "ne", "sw", "sw"],
    ["ne", "ne", "s", "s"],
    ["se", "sw", "se", "sw", "sw"]
]

g = Grid()

'''for sample in samples:
    g.reset()
    g.move(sample)
    print g.get_distance()'''

g.reset()
g.move(data)
print g.get_distance()
print g.max_distance