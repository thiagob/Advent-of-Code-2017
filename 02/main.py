data = list(open("02\input.txt").readlines())
data = map(lambda r: map(lambda c: int(c), r.split('\t')), data)

def first_part(data):

    differences = []

    for line in data:
        differences.append(max(line) - min(line))

    return sum(differences)

def second_part(data):

    divisors = []

    for line in data:
        for col in line:
            divisor = filter(lambda n: col != n and col % n == 0, line)
            
            if len(divisor) > 0:
                divisors.append(col / divisor[0])

    return sum(divisors)

print first_part(data)
print second_part(data)