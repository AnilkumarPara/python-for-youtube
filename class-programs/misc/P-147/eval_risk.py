user_input = input("Enter a Python command: ")
eval(user_input)

'''
Imagine a program that takes a string from the user and
uses eval() to execute it. This can lead to arbitrary code execution:
'''

'''
Risk: If a user inputs something malicious like
 __import__('os').system('rm -rf /'), 
 it could execute a system command that deletes files.
'''
