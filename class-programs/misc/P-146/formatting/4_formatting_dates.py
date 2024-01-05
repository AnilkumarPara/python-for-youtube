from datetime import datetime

current_date = datetime.now()

# Format date as YYYY-MM-DD
# Example Output: 2024-JAN-05

# using f-string
print(f"{current_date:'%Y-%b-%d'}")


"""
%Y is used for the four-digit year,
%y is used for the two-digit year,
%m is used to represent the month as a zero-padded decimal number.
%b for the abbreviated month name,
%d for the zero-padded day of the date
"""