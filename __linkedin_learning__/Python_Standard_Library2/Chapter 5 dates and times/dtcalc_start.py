# Perform calculations with dates and times using timedelta
import datetime

# create some date objects
dt1 = datetime.datetime(2019, 1, 15, 10)
dt2 = datetime.datetime(2019, 1, 20, 15)

# TODO: dates and times can be compared
print(dt1 < dt2)
print(dt1 > dt2)

# TODO: Subtracting one date from another creates a timedelta
delta = dt2 - dt1
print(delta)

# timedeltas have components
print(delta.days)
print(delta.seconds)

# TODO: timedeltas can be used to perform date math
now = datetime.datetime.now()
one_year = datetime.timedelta(days=365) 
one_week = datetime.timedelta(weeks=1) 

print("One year from now will be: ".format(width=50, justify='right'), now + one_year)
print("One week from now will be: ", now + one_week)
print("One week ago was: ".rjust(27, '.'), now - one_week)

# stringName.center(width,fillChar)