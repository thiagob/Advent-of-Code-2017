from collections import deque

def get_subsequent(input, iterations, value):

    spinlock = deque([0])

    for i in range(1, iterations + 1):
        spinlock.rotate(-input)
        spinlock.append(i)

        #print spinlock

    print '-'

    pos = (list(spinlock).index(value) + 1) % len(spinlock)
    return spinlock[pos]

# Sample
# print get_subsequent(3, 2017, 2017)

# First Part
# print get_subsequent(314, 2017, 2017)

# Second Part
print get_subsequent(314, 50000000, 0)