from datetime import*

today=datetime.today()
today=today.strftime("%d %B %Y")

today_string=datetime.strptime(today,"%d %B %Y")

print(today_string)