lines = open("09\input.txt").readlines()

#lines = ['{{<a!>},{<a!>},{<a!>},{<ab>}}']

for line in lines:
    groups = []
    count = 0
    level = 0
    garbage = False
    skip_next = False
    garbage_count = 0

    for char in line:
        if skip_next:
            skip_next = False
            continue
        if char == "!":
            skip_next = True
            continue

        if not garbage:
            if char == "<":
                garbage = True
            elif char == "{":
                level += 1
                groups.append(level)
            elif char == "}":
                level -= 1
                count += groups[-1]
                groups.pop()
        else:
            if char == ">":
                garbage = False
            else:
                garbage_count += 1


    print count
    print garbage_count