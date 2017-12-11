lengths = [212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164]
elements = []
for i in range(0, 256):
    elements.append(i)


#elements = [0, 1, 2, 3, 4]
#lengths = [3, 4, 1, 5]

selected = 0
skip_size = 0
index = 0

def get_index(index):
    return index % len(elements)

def get_sublist(selected, length):
    sublist = []
    for i in range(0, length):
        sublist.append(elements[get_index(selected + i)])
    return sublist
     

for length in lengths:
    sublist = get_sublist(selected, length)
    sublist = sublist[::-1]

    for idx, item in enumerate(sublist):
        elements[get_index(selected + idx)] = item

    selected = get_index(selected + length + skip_size)
    skip_size += 1

print elements[0] * elements[1]