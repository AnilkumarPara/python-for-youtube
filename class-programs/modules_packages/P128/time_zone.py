from datetime import datetime, timezone, date
utc_date_time = datetime.now(timezone.utc)
print(utc_date_time)
current_date_time = datetime.now()
print(current_date_time)
todays_date = date.today()
print(todays_date)
