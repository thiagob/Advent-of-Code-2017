import datetime

class SpinLock():

    def __init__(self, buffer, max=2017):
        self.max = max
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

        self.values.insert(pos, self.current)

        self.show_progress()

    def run(self):
        self.reset()

        while self.current <= self.max:
            self.next()

    def find_ultimately_after(self, number):
        index = self.values.index(number)
        index = (index + 1) % len(self.values)
        return self.values[index]

    def show_progress(self):
        progress = float(self.current) / self.max * 100
        if progress % 0.5 == 0:
            print '>> {0} - {1}% completed > Array Size: {2}'.format(
                str(datetime.datetime.now().time()), progress, len(self.values))

def part1_sample():
    s = SpinLock(3)
    s.run()
    print s.find_ultimately_after(2017)

def part1_input():
    s = SpinLock(314)
    s.run()
    print s.find_ultimately_after(2017)

def part2_input():
    s = SpinLock(314, 50000000)
    s.run()
    print s.find_ultimately_after(0)

print 'SAMPLE'
part1_sample()

print 'PART 1'
part1_input()

print 'PART 2 !!! NOT ABLE TO EXECUTE !!!'
part2_input()