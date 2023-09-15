# Skipping Weekends in a Work Schedule:
"""Suppose you are generating a work schedule and want to skip weekends
when assigning tasks. You can use "continue" to skip Saturdays and Sundays.
"""
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in days:
    if day == 'Saturday' or day == 'Sunday':
        continue  # Skip weekends
    print("assign the tasks on ", day)
print("End of the program")

