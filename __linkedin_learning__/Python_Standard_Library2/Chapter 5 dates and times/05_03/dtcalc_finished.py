# Perform calculations with dates and times using timedelta
import datetime

# create some date objects
dt1 = datetime.datetime(2019, 1, 15, 10)
dt2 = datetime.datetime(2019, 1, 20, 15)

# dates and times can be compared
print(dt1 < dt2)
print(dt1 > dt2)

# Subtracting one date from another creates a timedelta
delta = dt2 - dt1
print(delta)
# timedeltas have components
print(delta.days)
print(delta.seconds)


# timedeltas can be used to perform date math
now = datetime.datetime.now()
oneyear = datetime.timedelta(days=365)
oneweek = datetime.timedelta(weeks=1)

print("One year from now will be: ", now + oneyear)
print("One week from now will be: ", now + oneweek)
print("One week ago was: ", now - oneweek)
