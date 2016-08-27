#!/bin/python3

# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer

S = input().strip()

try:
    n = int(S)
    print(n)
except:
    print("Bad String")
