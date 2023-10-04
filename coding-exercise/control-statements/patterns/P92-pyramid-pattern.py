# Pyramid Star Pattern
"""
   *
  ***
 *****
*******
"""
n = 4
for row in range(1, n+1):
    print(' '*(n-row) + '*'*((2*row)-1))


