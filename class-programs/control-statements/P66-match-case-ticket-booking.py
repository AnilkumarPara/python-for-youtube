# WAP to book the movie ticket based on the user choice
class_type = input("Enter the class type ['Diamond', 'Gold', 'Silver'] for movie ticket booking")
match class_type:
    case 'Diamond':
        print("Book the Diamond class ticket for movie.")
        print("Booking for the  Diamond class is successful, Enjoy the movie.")
    case 'Gold':
        print("Book the Gold class ticket for movie.")
        print("Booking for the  Gold class is successful, Enjoy the movie.")
    case 'Silver':
        print("Book the Silver class ticket for movie.")
        print("Booking for the  Silver class is successful, Enjoy the movie.")
    case _:
        print("User has entered the incorrect class type, please re-enter the correct class")
print("End of the program")
