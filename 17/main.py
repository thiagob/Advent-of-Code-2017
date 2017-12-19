class SpinLock():

    def __init__(self, buffer=0):
        self.max = 2017
        self.buffer = buffer
        self.reset()

    def reset(self):
        self.values = []
        self.current = -1
        self.position = 0

    def next(self):
        self.current += 1

        pos = (self.position + self.buffer) % len(self.values) if len(self.values) > 0 else 0
        self.position = pos + 1

        self.values = self.values[:pos + 1] + [self.current] + self.values[pos + 1:]

    def run(self):
        self.reset()

        while self.current <= self.max:
            self.next()

    def find_ultimately_after(self, number):
        index = self.values.index(number)
        index = (index + 1) % len(self.values)
        return self.values[index]

def part1_sample():
    s = SpinLock(3)
    s.run()
    print s.find_ultimately_after(2017)

def part1_input():
    s = SpinLock(314)
    s.run()
    print s.find_ultimately_after(2017)

part1_sample()
part1_input()