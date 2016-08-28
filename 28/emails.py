#!/bin/python3

# Day 28: RegEx, Patterns

# https://www.hackerrank.com/challenges/30-regex-patterns

import re

names = []

T = int(input())
for i in range(T):
    name, id = input().split(" ")
    if re.search(r"@gmail\.com$", id):
        names.append(name)

names.sort()
for name in names:
    print(name)
