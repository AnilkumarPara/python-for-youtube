"""
Count Occurrences: Given a list and a target element,
count the occurrences of the target in the list.
"""
numbers = [1, 2, 3, 4, 5, 2, 2, 6, 7]
target = int(input("Enter the number to find the number of occurrence "))
counter = 0
for number in numbers:
    if number == target:
        counter += 1
print(f"The number {target} occurs {counter} times in the list.")
