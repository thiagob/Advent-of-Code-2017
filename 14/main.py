import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from hashes import Knot
from random import randint

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

        b = ''
        for c in knot_hash:
            b += bin(int(c, 16))[2:].zfill(4)

        if len(b) != 128:
            raise Exception('Error to generate binary for ' + knot_hash + ' ' + str(len(b)))

        return b

    def get_used_squares(self):
        count = 0
        for row in self.disk:
            for square in row:
                if square == '1':
                    count += 1
        return count

class Groups():
    def __init__(self, size=128):
        self.size = size
        self.matrix = np.zeros((size, size))
    
    def load(self, disk):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if row < len(disk) and col < len(disk[row]):
                    self.matrix[row, col] = disk[row][col]
                else:
                    raise Exception({ "col": col, "row": row})

    def gen_groups(self):
        group = 100
        for r in range(0, len(self.matrix)):
            for c in range(0, len(self.matrix[0])):
                if self.matrix[r, c] == 1:
                    group += 1
                    self.flood(r, c, group)
        return group - 100

    def flood(self, row, col, group):
        if self.matrix[row, col] == 1:
            self.matrix[row, col] = group

            for i in [-1, 1]:
                radj = row + i
                if radj >= 0 and radj < self.size:
                    if self.matrix[radj, col] == 1:
                        self.flood(radj, col, group)

                cadj = col + i
                if cadj >= 0 and cadj < self.size:
                    if self.matrix[row, cadj] == 1:
                        self.flood(row, cadj, group)

class Dispaly():
    def show(self, matrix):
        plt.matshow(matrix)
        plt.show()

input_string = 'ljoxqyyw'
#input_string = 'flqrgnkx'

d = Defrag()
#print d.get_binary_hash('flqrgnkx-0')
d.gen_input(input_string)
#print d.get_used_squares()
#print d.disk

g = Groups()
g.load(d.disk)
print g.gen_groups()

#print g.matrix

dsp = Dispaly()
dsp.show(g.matrix)