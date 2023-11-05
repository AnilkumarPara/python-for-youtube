"""
Count the frequency of letters in a string and output as
key: value
char:count
Write program using loop
"""
string = "hello"
string_count = {}
for char in string:
    string_count[char]=string.count(char)
print(string_count)

