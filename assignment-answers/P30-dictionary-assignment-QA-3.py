"""
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employees = {'emp1': {'employee_name': 'Anil', 'salary': 2000, 'Designation': 'SE'},
             'emp2': {'employee_name': 'Sunil', 'salary': 3000, 'Designation': 'SSE'},
             'emp3': {'employee_name': 'Sachin', 'salary': 4000, 'Designation': 'Lead'},
             'emp4': {'employee_name': 'Jayansh', 'salary': 5000, 'Designation': 'Manager'}
             }

print(employees['emp3']['Designation'])
