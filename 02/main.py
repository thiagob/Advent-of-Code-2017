data = list(open("02\input.txt").readlines())
data = map(lambda r: map(lambda c: int(c), r.split('\t')), data)

differences = []

for line in data:
    differences.append(max(line) - min(line))

print sum(differences)