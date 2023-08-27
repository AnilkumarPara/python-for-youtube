# what is the output of following programs

a = 400.30123
b = 400.30123
print(a is b)  # True

i = 23
j = 23
print(i is j)  # True
print(i == j)  # True

a1 = 999
b1 = 999
print(a1 is b1)  # True
print(a1 == b1)  # True

y = 4
z = -4
print(y == z)  # False

s1 = 4096 * 'a'
s2 = 4096 * 'a'
print(s1 is s2)  # True
