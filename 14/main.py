from hashes import Knot

class Defrag():
    def __init__(self):
        self.disk = []

    def gen_input(self, input_string):
        for i in range(0, 128):
            s = input_string + '-' + str(i)
            row = self.get_binary_hash(s)
            self.disk.append(row)

    def get_binary_hash(self, s):
        knot_hash = Knot.gen_knot_hash(s)
        return bin(int(knot_hash, 16))[2:]

    def get_used_squares(self):
        count = 0
        for row in d.disk:
            for square in row:
                if square == '1':
                    count += 1
        return count

input_string = 'ljoxqyyw'

d = Defrag()
d.gen_input(input_string)
print d.get_used_squares()