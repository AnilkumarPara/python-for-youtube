def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        return "The factorial function is only defined for non-negative integers"


print(factorial(5))

