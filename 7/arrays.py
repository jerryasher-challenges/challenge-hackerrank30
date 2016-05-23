#!/bin/python3

n = int(input().strip())
arr = [str(int(arr_temp)) for arr_temp in input().strip().split(' ')]
arr.reverse()
print(" ".join(arr))
