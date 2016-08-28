#!/bin/python3

# day 29: bitwise

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]

    max = 0
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            bw = a & b
            if bw > max and bw < k:
                max = bw
    print(max)
