"""
WAP to retrieve Jayansh and Shanvika ages in reverse order using positive indexing.
Output should be [7,4].
Please use below dictionary.
"""
students_info = {'student_names': ['Anil', 'Jayansh', 'Shanvika'], 'ages': [19, 4, 7],
                 'roll_nos': (201, 202, 205), 'classes': ['Intermediate', 'UKG', '2nd Grade'],
                 'sections': ['A', 'E', 'G'], 'percentages': [65.6, 78.9, 99.1]
                 }
print(students_info['ages'][2:0:-1])
