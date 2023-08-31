# WAP for the car cleaning and user can choose the person for cleaning

# Sequential Statements
"""
person = input("Enter the person name")
print(person, "will clean the car")
print("Car cleaning started")
print("Car cleaning is in progress")
print("Car cleaning completed")
"""

# Control statements
i = 1
while i <= 5:
    person = input("Enter the person name")
    car_cleaning_status = input(f"Enter 'Yes' if car-{i} is in cleaned state , 'No' Otherwise")
    if car_cleaning_status == 'No':
        print(person, f"will clean the car-{i}")
        print(f"Car-{i} cleaning started")
        print(f"Car-{i} cleaning is in progress")
        print(f"Car-{i} cleaning completed")
    else:
        print(f"Your car-{i} is already in cleaned state and no need to clean again")
    i = i+1
