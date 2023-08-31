# nested if
"""
WAP to get the Karachi biscuits, when your friend goes to Hyderabad, Ameerpet,
Karachi biscuits shop
"""
print("Start of the program")
place_1 = input("if you are going to Hyderabad, Enter 'Hyderabad', otherwise Enter 'No'")
if place_1 == 'Hyderabad':
    place_2 = input("if you are going to Ameerpet, Enter 'Ameerpet', otherwise Enter 'No'")
    if place_2 == 'Ameerpet':
        place_3 = input("if you are going to Karachi biscuits shop, Enter 'Karachi', otherwise Enter 'No'")
        if place_3 == 'Karachi':
            print("Getting the Karachi biscuits")
print("End of the program")
