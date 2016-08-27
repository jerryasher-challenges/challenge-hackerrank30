#!/bin/python3

n = int(input().strip())


def _factorial(N):
    if N <= 1:
        return 1
    return N * _factorial(N - 1)


def factorial(N):
    print(_factorial(N))

if __name__ == "__main__":
    factorial(n)
