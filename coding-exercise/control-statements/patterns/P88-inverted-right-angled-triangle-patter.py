# Inverted Right-Angled Triangle Number Pattern
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
n = 5
for row in range(n, 0, -1):
    for col in range(1, row+1):
        print(col, end=' ')
    if row != 1:
        print()
