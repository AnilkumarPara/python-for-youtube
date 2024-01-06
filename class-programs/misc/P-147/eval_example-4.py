# Generally in real-time we get the data in the form of a string like
data_str = """
{
    'employees': [
        {'name': 'Alice', 'age': 30, 'department': 'Sales', 'skills': ['communication', 'negotiation']},
        {'name': 'Bob', 'age': 35, 'department': 'IT', 'skills': ['programming', 'system administration']},
        {'name': 'Charlie', 'age': 28, 'department': 'HR', 'skills': ['recruitment', 'policy planning']}
    ],
    'departments': {
        'Sales': {'manager': 'Alice', 'location': 'Building A'},
        'IT': {'manager': 'Bob', 'location': 'Building B'},
        'HR': {'manager': 'Charlie', 'location': 'Building C'}
    },
    'company': 'Tech Solutions',
    'location': ('City Center', 12345)
}"""
data = eval(data_str)
print(type(data))
