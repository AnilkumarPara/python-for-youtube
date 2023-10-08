# Find all prime numbers between 2 and n
"""
The standard definition of prime numbers applies only to
positive integers greater than 1. A prime number is defined
as a number that has only two distinct positive divisors: 1 and itself.
For example, 2, 3, 5, 7, 11, etc. are prime numbers
because they can only be divided evenly by 1 and themselves
without leaving a remainder.
"""
n = int(input("Enter a 'n' value to find the prime numbers from '2 to n' "))
if n > 1:
    for number in range(2, n+1):
        counter = 0
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter == 2:
            print(number)
else:
    print("Prime numbers apply only to natural numbers greater than 1.")
