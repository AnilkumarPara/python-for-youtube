# Diamond Pattern
"""
    *
   ***
  *****
 *******
  *****
   ***
    *
"""
n = 4
for row1 in range(1, n+1):
    print(' '*(n-row1) + '*'*((2*row1)-1))
for row2 in range(1, n):
    print(' '*row2 + '*'*((2*(n-row2))-1))

