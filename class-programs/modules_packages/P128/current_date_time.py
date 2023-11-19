from datetime import datetime
current_date_time = datetime.now()
print(current_date_time)
utc_date_time = datetime.utcnow()
print(utc_date_time)
current_date = current_date_time.date()
current_time = current_date_time.time()
print(current_date)
print(current_time)
