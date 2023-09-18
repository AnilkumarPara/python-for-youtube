# Password Authentication
"""
In a simple password authentication system, repeatedly ask the user for a password
until they enter the correct password or reach a maximum number of attempts
"""
correct_password = 'admin123'
max_attempts = 3
attempt = 1
while attempt <= max_attempts:
    password = input("Enter the correct password ")
    if password == correct_password:
        print("Access is granted")
        break
    else:
        print("Incorrect password, Please try again")
        attempt += 1
else:
    print("Access denied, You have reached the maximum number of attempts")


