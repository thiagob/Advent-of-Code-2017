data = list(open("04\input.txt").readlines())
data = map(lambda r: r.replace('\n', '').split(' '), data)

count = 0

for line in data:
    if len(line) == len(set(line)):
        count += 1

print count