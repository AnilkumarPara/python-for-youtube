"""
Retrieve 'G' from last_name using following dictionary with negative indexing
Retrieve 3000 from salaries using following dictionary with positive indexing
Retrieve 50 from Age using following dictionary with negative indexing
"""
D1 = {'names': [{'first_name': 'Anilkumar', 'last_name': 'Para'},
                {'first_name': 'Sachin', 'last_name': 'Tendulkar'},
                {'first_name': 'Mahesh', 'last_name': 'G'}],
      'Salaries': [2000, 3000, 4000],
      'Age': (35, 50, 47)
      }
print(D1['names'][-1]['last_name'])
print(D1['Salaries'][1])
print(D1['Age'][-2])
