class Generator():

    def __init__(self, start, factor):
        self.previous = start
        self.factor = factor
        self.divisor = 2147483647

    
    def get_next(self):
        next = (self.previous * self.factor) % self.divisor
        self.previous = next
        return next

class Judge():

    def __init__(self, gen_a, gen_b):
        self.gen_a = gen_a
        self.gen_b = gen_b
        self.count = 0
        self.num_of_pairs = 40000000
        #self.num_of_pairs = 5

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

#ga = Generator(65, 16807)
#gb = Generator(8921, 48271)

ga = Generator(618, 16807)
gb = Generator(814, 48271)

jdg = Judge(ga, gb)
jdg.run()

print '!!!!! Final Count: {0} !!!!!'.format(jdg.count)
