import sys

print("default recursion limit=", sys.getrecursionlimit())  # to get the recursion limit
sys.setrecursionlimit(2000)  # to set the recursion limit
print("recursion limit after setting=", sys.getrecursionlimit())  # to get the recursion limit after the update

i = 1  # global variable


def display_greetings():
    global i  # You need to use the global keyword to update the global variable
    print("Hello!", i)
    i = i + 1
    display_greetings()


display_greetings()
