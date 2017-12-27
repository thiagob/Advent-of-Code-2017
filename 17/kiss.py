def do_it(buffer, iterations):
    values = [0]
    position = 0

    for i in range(1, iterations + 1):
        position = (position + buffer) % len(values) + 1
        values.insert(position, i)
        print 'i == {0}; {1}'.format(i, values)

    return values

def get_subsequent(buffer, iterations, value):
    values = do_it(buffer, iterations)

    index = values.index(value)
    return values[index + 1 % len(values)]

print get_subsequent(3, 2017, 2017)
print get_subsequent(314, 2017, 2017)
# print get_subsequent(314, 50000000, 0)