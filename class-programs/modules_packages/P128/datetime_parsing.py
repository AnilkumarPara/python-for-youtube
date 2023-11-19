from datetime import datetime

date_string = "2023-11-12 14:30:00"
date_format = "%Y-%m-%d %H:%M:%S"
parsed_datetime = datetime.strptime(date_string, date_format)
print(parsed_datetime)
print(type(parsed_datetime))

formatted_string = datetime.strftime(parsed_datetime, date_format)
print(formatted_string)
print(type(formatted_string))
