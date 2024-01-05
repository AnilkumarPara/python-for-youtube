# You want to greet someone
# Hello Anil
name = input("Enter the person name to greet: ")

# You want to add 2 numbers and print on the screen
# Addition = 6
a = int(input("Enter a number for the Addition: "))
b = int(input("Enter a number for the Addition: "))

# Old Style (%-formatting)
print("--- Old Style (%-formatting)---")
print("Hello %s" % name)
print("Addition = %d" % (a+b))

# str.format() Method
print("--- format() Method ---")
print("Hello {}".format(name))
print("Addition = {}".format(a+b))

# Using f-string (Formatted String Literals)
print("--- Formatted String Literals (f-strings) ---")
print(f"Hello {name}")
print(f"Addition = {a+b}")
