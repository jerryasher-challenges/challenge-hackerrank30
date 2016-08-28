#!/bin/python 3

# Day 25: Running Time and Complexity

import math


def is_prime(n):
    root = n**.5
    upper = math.floor(root) + 1

    if n == 1:
        return False
    elif n == 2:
        return True

    if n % 2 == 0:
        return False

    for divisor in range(3, upper, 2):
        if n % divisor == 0:
            return False
    else:
        return True

T = int(input())
for i in range(T):
    data = int(input())
    if is_prime(data):
        print("Prime")
    else:
        print("Not prime")
