#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from os import replace

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print(f'today is: { now }')
print('today is:', now)
print('today is: ' + str(now))

# print today's date one year from now
print('one year rom now it will be:', now + timedelta(days=365))

# create a timedelta that uses more than one argument
print('In 2 days and 3 weeks will be', now + timedelta(days=2, weeks=3))

# calculate the date 1 week ago, formatted as a string
one_week_ago = now - timedelta(weeks=1)
print('One week ago is', one_week_ago.strftime("%a %d-%B-%Y %H:%M"))

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if (afd < today):
    print("April Fool's day already went by %d days ago" %((today - afd).days))
    afd = afd.replace(year = today.year+1)

# Now calculate the amount of time until April Fool's Day  
days_to_afd = afd - today
print("It is just ", days_to_afd.days, "until April Fools Day.")

# Print out tomrrow's day of the week;
today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday() + 1) % 7])