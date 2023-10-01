# Checkerboard Pattern
"""
The pattern typically contains two colours where a single checker
(that is a single square within the check pattern) is surrounded
on all four sides by a checker of a different colour.
"""
"""
B W B W
W B W B
B W B W
W B W B
"""
n = int(input("enter the number of rows: "))
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if (row+col) % 2 == 0:
            print("B", end=' ')
        else:
            print("W", end=' ')
    if row != n:
        print()
