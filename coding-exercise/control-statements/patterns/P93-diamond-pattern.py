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
for row in range(1, n+1):
    # Printing leading spaces
    for col1 in range(n-row):
        print(end=' ')

    # Printing stars
    for col2 in range(1, ((row*2)-1)+1):
        print('*', end='')

    # Move to the next line
    print()

for row in range(n-1, 0, -1):
    # Printing leading spaces
    for col1 in range(n - row):
        print(end=' ')

    # Printing stars
    for col2 in range(1, ((row*2)-1)+1):
        print('*', end='')

    # Move to the next line
    print()

