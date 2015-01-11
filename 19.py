import datetime

total = 0
_date = datetime.date(1901, 1, 1)
_date += datetime.timedelta(days=6-_date.weekday())

while _date < datetime.date(2000, 12, 31):
    if _date.day == 1:
        total += 1

    _date += datetime.timedelta(weeks=1)
# datetime.date(1901, 1, 1).weekday() == 6

print total
