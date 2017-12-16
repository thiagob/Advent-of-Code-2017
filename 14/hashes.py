import numpy as np

class Knot():
    @staticmethod
    def gen_knot_hash(input_string):
        k = Knot()
        k.gen_elements()
        k.gen_lengths(input_string)
        k.do_sparse_hash()
        return k.get_knot_hash(k.get_dense_hash())

    def __init__(self):
        self.selected = 0
        self.skip_size = 0
        self.lengths = []
        self.elements = []

    def gen_lengths(self, input_string):
        self.lengths = []
        for c in input_string:
            self.lengths.append(ord(c))
        self.lengths += [17, 31, 73, 47, 23]

    def gen_elements(self):
        self.elements = []
        for i in range(0, 256):
            self.elements.append(i)

    def get_index(self, index):
        return index % len(self.elements)

    def get_sublist(self, selected, length):
        sublist = []
        for i in range(0, length):
            sublist.append(self.elements[self.get_index(selected + i)])
        return sublist

    def do_sparse_hash(self):
        for t in range(0, 64):
            for length in self.lengths:
                sublist = self.get_sublist(self.selected, length)
                sublist = sublist[::-1]

                for idx, item in enumerate(sublist):
                    self.elements[self.get_index(self.selected + idx)] = item

                self.selected = self.get_index(self.selected + length + self.skip_size)
                self.skip_size += 1

    def get_dense_hash(self):
        dense_hash = []
        for b in range(0, int(len(self.elements) / 16)):
            block = self.get_sublist(b * 16, 16)
            number = np.bitwise_xor.reduce(block)
            dense_hash.append(number)
        return dense_hash

    def get_knot_hash(self, dense_hash):
        knot_hash = ''
        for i in range(0, len(dense_hash)):
            knot_hash += format(dense_hash[i], '02x')
        return knot_hash


# print Knot.gen_knot_hash('')
# print Knot.gen_knot_hash('AoC 2017')
# print Knot.gen_knot_hash('212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164')
