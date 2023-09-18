# Searching for an Element in a List using For else

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = int(input("Enter a element to search from a list "))

for number in numbers:
    if number == search_element:
        print("Search element is found")
        break
else:
    print("Search element is not found")

print("End of the program")















