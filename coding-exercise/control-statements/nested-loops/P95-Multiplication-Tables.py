# Print multiplication tables from 1 to n
n = int(input("Enter n value to generate tables from 1 to n: "))
for number in range(1, n+1):
    print("Multiplication table for ", number)
    for i in range(1, 11):
        print(number, '*', i, '=', number*i)
    print()
