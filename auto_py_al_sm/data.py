from datetime import datetime,timedelta
now = datetime.now()
print(type(now))
end_date = now + timedelta(days=1)
now_date = end_date.strftime("%A")
print(now_date)
print(end_date.strftime("%d %B %Y (%A)")) 