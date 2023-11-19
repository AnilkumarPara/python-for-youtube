from datetime import datetime
dt1 = datetime(2023, 11, 17, 22, 11, 33)
dt2 = datetime(2022, 11, 16, 21, 12, 33)
print(dt1-dt2)
local = datetime.now()
utc = datetime.utcnow()
print(local-utc)
