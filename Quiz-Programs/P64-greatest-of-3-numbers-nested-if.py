# WAP to find the greatest of 3 numbers using nested if condition
a = int(input("Enter value of 'a' "))
b = int(input("Enter value of 'b' "))
c = int(input("Enter value of 'c' "))

if a > b:
    if a > c:
        print("a is greatest")
if b > a:
    if b > c:
        print("b is greatest")
if c > a:
    if c > b:
        print("c is greatest")

# Better code optimization using the nested if else
if a > b:
    if a > c:
        print("a is greatest")
    else:
        print("c is greatest")

else:
    if b > c:
        print("b is greatest")
    else:
        print("c is greatest")


