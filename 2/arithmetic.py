#!python

mealCost = float(input())  # original meal price
tipPercent = int(input())  # tip percentage
taxPercent = int(input())  # tax percentage

# Write your calculation code here.
cost = mealCost * (1 + (tipPercent + taxPercent) / 100.0)

# cast the result of the rounding operation to an int and save it as totalCost
totalCost = round(cost)

# Print your result
print("The total meal cost is " + str(totalCost) + " dollars.")
