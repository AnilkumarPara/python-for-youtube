"""
Write a program that takes a username and password as input,
checks if the user's credentials match a predefined username and password.
If they match, display a success message; otherwise, display a failure message.
"""
correct_user_name = 'anil'
correct_password = 'admin123'

username = input("Enter your username: ")
password = input("Enter your password: ")
if correct_user_name == username and correct_password == password:
    print("Authentication successful. Welcome", username)
else:
    print("Authentication failed. Invalid username or password")
