"""
WAP to find the class in which student has passed in the exams
based on the percentage of marks he scored in the exam
"""
percentage_of_marks = float(input("Enter the percentage of marks student secured in the exams"))
if 70 <= percentage_of_marks <= 100:
    print("Student has passed in the Distinction")
elif 60 <= percentage_of_marks < 70:
    print("Student has passed in the First class")
elif 50 <= percentage_of_marks < 60:
    print("Student has passed in the Second class")
elif 35 <= percentage_of_marks < 50:
    print("Student has passed in the Third class")
elif 0 <= percentage_of_marks < 35:
    print("Student failed perfectly in the exam")
else:
    print("Student has entered the incorrect marks, please re-enter the correct marks")
print("End of the program")


