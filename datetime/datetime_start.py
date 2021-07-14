# Basics of dates and times
from datetime import date, time, datetime


# TODO: create a new date object
d1 = date.today()
print(d1)

# TODO: create a new time object
t1 = time(12, 30, 00)
print(t1)

# TODO: create a new datetime object
dt1 = datetime.now()
print(dt1)

# TODO: access various components of the date and time objects
print(dt1.year, dt1.month, dt1.day)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(days[dt1.weekday()])

print(t1.hour)

# TODO: To modify values of date and time objects, use the replace function
d1 = d1.replace(year=2021, month=10, day=31)
print(d1)


