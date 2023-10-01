# Hollow Square star pattern
"""
* * * *
*     *
*     *
* * * *
"""
n = 4
for row in range(1, n+1):
    for col in range(1, n+1):
        if row == 1 or col == 1 or row == n or col == n:
            print('*', end=' ')
        else:
            print(" ", end=" ")
    print()


