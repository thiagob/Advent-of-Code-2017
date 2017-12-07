file_name = "05\input.txt"

######################################
# FIRST START
######################################
data = list(open(file_name).readlines())
data = map(lambda r: int(r), data)

index = 0
counter = 0

while True:

    steps = data[index]
    data[index] += 1
    index += steps
    counter += 1

    if index >= len(data) or index < 0:
        break
    

print "First: "
print counter

######################################
# SECOND START
######################################
data = list(open(file_name).readlines())
data = map(lambda r: int(r), data)

index = 0
counter = 0

while True:

    steps = data[index]
    data[index] += -1 if steps >= 3 else 1
    index += steps
    counter += 1

    if index >= len(data) or index < 0:
        break
    
print "Second: "
print counter
