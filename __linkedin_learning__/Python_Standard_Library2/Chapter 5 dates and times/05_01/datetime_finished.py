# Basics of dates and times
from datetime import date, time, datetime


# create a new date object
d1 = date.today()
print(d1)

# create a new time object
t1 = time(12, 30, 00)
print(t1)

# create a new datetime object
dt1 = datetime.now()
print(dt1)


# access various components of the date and time objects
print(d1.day)
print(d1.year)

print(t1.hour)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(dt1.month)
print(dt1.weekday())
print(days[dt1.weekday()])


# To modify values of date and time objects, use the replace function
d1 = d1.replace(year=2020, month=10, day=31)
t1 = t1.replace(hour=5)
dt1 = dt1.replace(year=2017, month=12)
print(d1)
print(t1)
print(dt1)
