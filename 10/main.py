import numpy as np

elements = []
for i in range(0, 256):
    elements.append(i)


input_string = '212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164'
#input_string = 'AoC 2017'

lengths = []
for c in input_string:
    lengths.append(ord(c))
lengths += [17, 31, 73, 47, 23]

selected = 0
skip_size = 0

def get_index(index):
    return index % len(elements)

def get_sublist(selected, length):
    sublist = []
    for i in range(0, length):
        sublist.append(elements[get_index(selected + i)])
    return sublist

# part 1 
# lengths = [212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164]

# sample 1
# elements = [0, 1,2,3,4]
# lengths = [3,4,1,5]
for t in range(0, 64):
    for length in lengths:
        sublist = get_sublist(selected, length)
        sublist = sublist[::-1]

        for idx, item in enumerate(sublist):
            elements[get_index(selected + idx)] = item

        selected = get_index(selected + length + skip_size)
        skip_size += 1

# part 1
# print elements[0] * elements[1]
# print elements

# sparse hash
print elements


# dense hash
dense_hash = []
for b in range(0, int(len(elements) / 16)):
    block = get_sublist(b * 16, 16)
    number = np.bitwise_xor.reduce(block)
    dense_hash.append(number)

# hexa
knot_hash = ''
for i in range(0, len(dense_hash)):
    knot_hash += format(dense_hash[i], '02x')

print knot_hash