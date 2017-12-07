data = list(open("05\input.txt").readlines())
data = map(lambda r: int(r), data)

index = 0
counter = 0

while True:

    steps = data[index]
    data[index] = data[index] + 1
    index += steps
    counter += 1

    if index >= len(data) or index < 0:
        break
    

print counter