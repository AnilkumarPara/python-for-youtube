"""
Write a program that takes the current hour as input (in 24-hour format) and
displays a suitable greeting based on the time of the day
(morning, afternoon, evening).
"""
current_hour = int(input("Enter the current hour (0-23): "))
if 0 <= current_hour < 12:
    print("Good morning")
elif 12 <= current_hour < 18:
    print("Good afternoon")
elif 18 <= current_hour <= 23:
    print("Good evening")
else:
    print("Invalid hour, re-neter the correct hour")





