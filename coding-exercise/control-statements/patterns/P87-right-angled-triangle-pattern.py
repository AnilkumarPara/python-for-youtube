# Right-Angled Triangle Number Pattern
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    if row != 5:
        print()
