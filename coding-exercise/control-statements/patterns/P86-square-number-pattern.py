# Row-Repeated Sequential Square Number Pattern

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
for row in range(1, 6):
    for col in range(1, 6):
        print(col, end=' ')
    if row != 5:
        print()
