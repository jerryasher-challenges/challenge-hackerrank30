#!/bin/python3

# Day 26: Nested Logic
# https://www.hackerrank.com/challenges/30-nested-logic

return_date = [int(x) for x in input().split(' ')]
due_date = [int(x) for x in input().split(' ')]

year = 2
month = 1
day = 0

fine = 0
if return_date[year] > due_date[year]:
    fine = 10000
elif return_date[year] == due_date[year]:
    if return_date[month] > due_date[month]:
        fine = 500 * (return_date[month] - due_date[month])
    elif return_date[month] == due_date[month]:
        if return_date[day] > due_date[day]:
            fine = 15 * (return_date[day] - due_date[day])

print(fine)
