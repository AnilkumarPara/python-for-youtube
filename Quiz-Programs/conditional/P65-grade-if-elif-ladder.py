"""
WAP to find the grade of a student based on the percentage of marks
he scored in the exam using if elif ladder
"""
percentage_of_marks = float(input("Enter the percentage of marks student secured in the exams"))
if 90 <= percentage_of_marks <= 100:
    print("Student has passed in the A1 Grade")
elif 80 <= percentage_of_marks < 90:
    print("Student has passed in the A2 Grade")
elif 70 <= percentage_of_marks < 80:
    print("Student has passed in the B1 Grade")
elif 60 <= percentage_of_marks < 70:
    print("Student has passed in the B2 Grade")
elif 50 <= percentage_of_marks < 60:
    print("Student has passed in the C1 Grade")
elif 40 <= percentage_of_marks < 50:
    print("Student has passed in the C2 Grade")
elif 33 <= percentage_of_marks < 40:
    print("Student has passed in the D Grade")
elif 0 <= percentage_of_marks < 33:
    print("Student failed in the exam, Grade is E")
else:
    print("Student has entered the incorrect marks, please re-enter the correct marks")
print("End of the program")
