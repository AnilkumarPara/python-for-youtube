"""
Floyd's triangle pattern
The Floyd's triangle is a right-angled triangle that contains
consecutive natural numbers, starting with a 1 in the top left corner.
"""
"""
1
2 3
4 5 6
7 8 9 10
"""
n = 4
num = 1
for row in range(1, n+1):
    for col in range(1, row+1):
        print(num, end=' ')
        num = num+1



