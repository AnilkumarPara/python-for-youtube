"""
WAP to extract each word from a sentence and store all the words
in the form of list using list comprehension
"""

paragraph = ["There was a fox.", 'It was brown in color.', "It was seen near that farm sometime back"]
print([word for sentence in paragraph for word in sentence.split()])
