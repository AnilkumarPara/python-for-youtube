"""
WAP to find names starts with ‘A’ and ends with 'a'
in the given list of names using list comprehension
"""
names = ['Abeesha', 'Abelia', 'Anil', 'Shanvika', 'Jayansh']
print([name for name in names if name.startswith('A') if name.endswith('a')])

