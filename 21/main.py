import numpy as np

rules = list(open('21\input.txt').readlines())
#rules = map(lambda l: l.strip().replace('.', '0').replace('#', '1').split(' => '), rules)
rules = map(lambda l: l.strip().split(' => '), rules)
rules = map(lambda l: [a.split('/') for a in l], rules)


class Program():

    def __init__(self, rules):
        self.rules = rules
        self.grid = ['.#.', '..#', '###']
        # self.grid = ['010', '001', '111']

    def generate(self):
        for i in range(0, 5):
            self.enhance()

    def enhance(self):
        # block dimensions
        length = 2 if len(self.grid) % 2 == 0 else 3
        count = len(self.grid) / length

        new_grid = self.create_grid((length + 1) * count)

        for row in range(0, count):
            for col in range(0, count):
                block = self.get_block(row * length, col * length, length)
                pattern = self.find_pattern(block)
                self.set_block(new_grid, row * len(pattern), col * len(pattern), pattern)

        self.grid = new_grid

    def create_grid(self, size):
        return ['*' * size for row in range(0, size)]

    def get_block(self, row, column, length):
        return [line[column:column + length] for line in self.grid[row: row + length]]

    def set_block(self, grid, row, column, block):
        length = len(block)
        for r in range(0, length):
            line = list(grid[row + r])
            for c in range(0, length):
                line[column + c] = block[r][c]
            grid[row + r] = ''.join(line)

    def find_pattern(self, block):
        variations = self.get_block_variations(block)
        for rule, pattern in self.rules:
            if rule in variations:
                return pattern

        raise Exception('Pattern not found for {0}'.format(block))

    def get_block_variations(self, block):
        matrix = [list(line) for line in block]

        variations = []
        variations.append(block)
        variations.append(np.flip(matrix, 0))
        variations.append(np.flip(matrix, 1))
        variations.append(np.rot90(matrix, 1))
        variations.append(np.flip(np.rot90(matrix, 1), 0))
        variations.append(np.rot90(matrix, 2))
        variations.append(np.flip(np.rot90(matrix, 2), 0))
        variations.append(np.rot90(matrix, 3))
        variations.append(np.flip(np.rot90(matrix, 3), 0))
        variations.append(np.transpose(matrix))

        for i in range(0, len(variations)):
            variations[i] = [''.join(line) for line in variations[i]]

        return variations

    def count_pixels(self, grid):
        count = 0
        for line in grid:
            for char in line:
                if char == '#':
                    count += 1

        return count

    def print_block(self, block):
        for line in block:
            print line
        print '-' * len(block)

p = Program(rules)

# a = ['.#.','..#','###']
# blocks = p.get_block_variations(a)
# for b in blocks:
#     p.print_block(b)

p.generate()

# for rule, pattern in p.rules:
#     if p.count_pixels(rule) == 5:
#         p.print_block(rule)

print 'Total of pixels: {0}'.format(p.count_pixels(p.grid))