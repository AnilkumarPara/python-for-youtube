"""
Count the frequency of letters in a string and output as
key: value
char:count
Write program using dictionary comprehension
"""
string = "hello"
print({char:string.count(char) for char in string})

