# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
import pendulum

# create some base datetimes
dt1 = pendulum.datetime(2020, 7, 28, 23, 0, 0)
dt2 = pendulum.datetime(2020, 12, 22)
print("--- Original Dates ---")
print(dt1.to_date_string())
print(dt2.to_date_string())
print("------\n")

# TODO: handle rollover of time
newdate = dt1.add(hours=1)
print(newdate.to_date_string())

newdate = dt1.add(minutes=60)
print(newdate.to_date_string())

# TODO: add and subtract various values
dt1 = dt1.add(years=2, months=3)
print(dt1.to_date_string())

dt1 = dt1.subtract(months=48, hours=72)
print(dt1.to_date_string())

# TODO: negative values also work
dt1 = dt1.add(years=-1, months=-4)
print(dt1.to_date_string())

# TODO: use helper functions for quick comparisons
print(dt1.is_past())
print(dt2.is_future())
print(dt2.is_dst())
print(dt2.is_leap_year())

# TODO: Try comparing datetimes
print(dt1 > dt2)
print(dt1 < dt2)

dt3 = pendulum.datetime(2020, 12, 22)
print(dt3 == dt2)
dt3 = dt3.set(second=1)
print(dt3 == dt2)

# TODO: Create a Period using difference
dt1 = dt1.set(year=2020, month=7, day=28)
p = dt1.diff(dt2)
print(p.in_hours())
print(p.in_days())
print(p.in_months())

p = dt2.diff_for_humans(dt1)
print(p)
