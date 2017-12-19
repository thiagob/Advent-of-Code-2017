class Generator():

    def __init__(self, start, factor, multiple_of=1):
        self.previous = start
        self.factor = factor
        self.divisor = 2147483647
        self.multiple_of = multiple_of

    
    def get_next(self):
        while True:
            next = (self.previous * self.factor) % self.divisor
            self.previous = next

            if next % self.multiple_of == 0:
                return next

class Judge():

    def __init__(self, gen_a, gen_b, num_of_pairs=40000000):
        self.gen_a = gen_a
        self.gen_b = gen_b
        self.count = 0
        self.num_of_pairs = num_of_pairs

    def get_lowest_bits(self, num):
        return self.get_binary(num)[16:]

    def get_binary(self, num):
        return bin(num)[2:].zfill(32)

    def run(self):
        for i in range(0, self.num_of_pairs):
            a = self.get_lowest_bits(self.gen_a.get_next())
            b = self.get_lowest_bits(self.gen_b.get_next())

            if a == b:
                self.count += 1

            # notify every 10%
            progress = float(i) / self.num_of_pairs * 100
            if progress % 5 == 0:
                print '{0}% ==> Count: {1}'.format(progress, self.count)

# sample
# ga = Generator(65, 16807)
# gb = Generator(8921, 48271)

# input
# ga = Generator(618, 16807)
# gb = Generator(814, 48271)

# jdg = Judge(ga, gb)
# jdg.run()

# print '!!!!! Part1 >> Final Count: {0} !!!!!'.format(jdg.count)


# sample
# ga = Generator(65, 16807, 4)
# gb = Generator(8921, 48271, 8)

# input
ga = Generator(618, 16807, 4)
gb = Generator(814, 48271, 8)

jdg = Judge(ga, gb, 5000000)
jdg.run()

print '!!!!! Part2   >> Final Count: {0} !!!!!'.format(jdg.count)