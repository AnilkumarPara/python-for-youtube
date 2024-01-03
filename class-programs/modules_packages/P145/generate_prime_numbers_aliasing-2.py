# Find all prime numbers between 2 and n
from number_theory_functions import prime_number as pn
import random

n = random.randint(1, 100)
print("n value is :", n)
if n > 1:
    for number in range(2, n + 1):
        if pn(number):
            print(number)
else:
    print("Prime numbers apply only to natural numbers greater than 1.")
