# find the biggest country among 3 counties based on the population
# nested if else
print("start of the program")
country_1 = int(input("Enter population of country_1"))
country_2 = int(input("Enter population of country_2"))
country_3 = int(input("Enter population of country_3"))
if country_1 > country_2:
    if country_1 > country_3:
        print("country_1 is the biggest country")
    else:
        print("country_3 is the biggest country")
else:
    if country_2 > country_3:
        print("country_2 is the biggest country")
    else:
        print("country_3 is the biggest country")
print("End of the program")
