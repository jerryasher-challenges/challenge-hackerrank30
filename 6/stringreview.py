#!python

n = int(input().strip())


def walk(line):
    first = []
    second = []
    for i, c in enumerate(line):
        if i % 2 == 0:
            first.append(c)
        else:
            second.append(c)
    out = "".join(first) + " " + "".join(second)
    return out


for i in range(n):
    line = input()
    print(walk(line))
