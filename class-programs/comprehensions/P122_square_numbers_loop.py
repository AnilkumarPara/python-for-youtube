"""
Creating a dictionary of squares for numbers from 1 to 5
using dictionary comprehension
"""
numbers = [1, 2, 3, 4, 5]
squared_numbers = {}
for n in numbers:
    squared_numbers[n] = n * n
print(squared_numbers)
