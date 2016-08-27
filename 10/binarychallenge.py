#!/bin/python3

n = int(input().strip())


def to_binary(n):
    binary = []
    if n == 0:
        return [0]
    while n > 0:
        (n, bit) = divmod(n, 2)
        binary.append(bit)
    binary.reverse()
    return binary


def consecutive1s(binary):
    max_len = 0

    count = 0
    for bit in binary:
        if bit:
            count += 1
        else:
            count = 0
        if count > max_len:
            max_len = count

    return max_len


print(consecutive1s(to_binary(n)))
