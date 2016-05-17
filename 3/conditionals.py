#!python

import sys


N = int(input().strip())

if N % 2 == 0:
    if 2 <= N <= 5:
        print("Not Weird")
    elif 6 <= N <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
