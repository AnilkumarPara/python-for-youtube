import time

time_string = "2023-11-12 14:30:00"
time_format = "%Y-%m-%d %H:%M:%S"
time_obj = time.strptime(time_string, time_format)
print(time_obj)
time_str = time.strftime(time_format, time_obj)
print(time_str)
