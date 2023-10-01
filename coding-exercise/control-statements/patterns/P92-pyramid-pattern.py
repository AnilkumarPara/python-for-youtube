# Pyramid Star Pattern
"""
    *
   ***
  *****
 *******
*********
"""
n = 5
for row in range(1, n+1):

    # Print the leading spaces
    for col in range(n-row, 0, -1):
        print(" ", end="")

    # Print the stars
    for col in range(1, ((2*row)-1)+1, 1):
        print("*", end="")
    print()
