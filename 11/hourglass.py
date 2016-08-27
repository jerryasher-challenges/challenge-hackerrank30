#!/bin/python3

a = []

for i in range(6):
    line = input()
    a.append([int(x) for x in line.split()])


def hourglass_sum(a, i, j):
    sum = a[i][j] + a[i][j + 1] + a[i][j + 2]
    i += 1
    sum += a[i][j + 1]
    i += 1
    sum += a[i][j] + a[i][j + 1] + a[i][j + 2]
    return sum


def max_hourglasses(a):
    max = -9 * 36
    for i in range(0, 4):
        for j in range(0, 4):
            sum = hourglass_sum(a, i, j)
            # print(sum)
            if sum > max:
                max = sum
    return max

print(max_hourglasses(a))
