from datetime import datetime

now=datetime.now()

# print(now)
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
second=now.second

# print(year)
timestamp=now.timestamp()
print(timestamp)