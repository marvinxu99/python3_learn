# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
from datetime import datetime, tzinfo
import time
import pendulum


# TODO: create a new datetime using pendulum
dt1 = pendulum.datetime(2021, 6, 25)   # default tz is UTC
dt1 = pendulum.datetime(2021, 6, 25, tz='America/New_York')   # default tz is UTC
print(dt1)
print(isinstance(dt1, datetime))
print(dt1.timezone_name)

# TODO: convert the time to another time zone
dt2 = dt1.in_timezone('Europe/Paris')
print(dt2, dt2.timezone_name)

# TODO: create a new datetime using the now() function
dt3 = pendulum.now()
print(dt3, dt3.timezone_name)

dt3 = pendulum.now('Europe/London')
print(dt3, dt3.timezone_name)

# TODO: Use the local function function
here = pendulum.local(2021, 7, 5)
print(here, here.timezone_name)

# TODO: Use today, tomorrow, yesterday
today = pendulum.today()
tomorrow = pendulum.tomorrow()
yest = pendulum.yesterday('America/New_York')
print('today =', today)
print("tomorrow =", tomorrow)
print('yesterday =', yest)

dt_here = pendulum.now()
dt_there = dt_here.in_timezone('Europe/London')
print(dt_here, "(Vancouver)")
print(dt_there, "(Lonoon)")

# TODO: create a datetime from a system timestamp
t = time.time()
dt4 = pendulum.from_timestamp(t)
print(dt4)

###################################
import pytz

ny_timezone = pytz.timezone('America/New_York')
t2 = datetime.now(ny_timezone)
print(t2, t2.tzinfo)

t3 = datetime.now(pytz.UTC)
print(t3, t3.tzinfo)
