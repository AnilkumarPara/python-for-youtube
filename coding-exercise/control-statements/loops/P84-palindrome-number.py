"""
A palindrome number is a number that remains the same when its digits are reversed.
For example, 121, 1331, 16461 are palindrome numbers, while 123 and 321 are not.
"""

# Approach 2: Using Integer Manipulation
"""
1. Store the number in a temporary variable.
2. Reverse the number by extracting each digit from the end and
building a new reversed number.
3. Compare the original and reversed numbers.
Here is a Python example for this approach:
"""
n = int(input("Enter a number to check for palindrome number "))
num = n
reversed_num = 0
while n > 0:
    reminder = n % 10
    reversed_num = reversed_num*10 + reminder
    n = n//10
if num == reversed_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")
