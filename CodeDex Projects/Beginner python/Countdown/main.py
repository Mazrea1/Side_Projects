import datetime
import bday_messages

today = datetime.date.today()
next_birthday = datetime.date(year = 2026,month = 3,day = 21)
days_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {days_away} days away!")