data = list(open("04\input.txt").readlines())
data = map(lambda r: r.replace('\n', '').split(' '), data)

def are_anagrams(word1, word2):
    w1 = list(word1)
    w1.sort()

    w2 = list(word2)
    w2.sort()

    return word1 != word2 and w1 == w2

count = 0

for line in data:
    # check duplicated lines (first star)
    if len(line) == len(set(line)):
        valid = True

        for word in line:
            for check in line:
                # check anagrams (second star)
                if are_anagrams(word, check):
                    valid = False
                    break

        if valid:
            count += 1

print count