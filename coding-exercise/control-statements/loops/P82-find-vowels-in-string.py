# Count and display vowels in a string
s1 = input("Enter the string to find the vowels in a string ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
counter = 0
for char in s1:
    if char in vowels:
        print(char)
        counter += 1
print("Total Number of vowels in a string =", counter)




