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

# TODO: add and subtract various values
newdate = dt1.add(hours=1)
print(newdate)
newdate2 = dt1.add(minutes=60)
print(newdate2)

dt1 = dt1.add(years=2, months=3)
print(dt1.to_date_string())

dt1 = dt1.subtract(months=48, hours=72)
print(dt1.to_date_string())

# TODO: negative values also work
print(dt1)
dt1 = dt1.add(years=-1, months=-4)
print(dt1.to_date_string())

# TODO: Try comparing datetimes
dt3 = pendulum.now()
print(dt3)
print(dt3.is_past())
print(dt3.is_future())
print(dt3.is_dst())         # Day saving time
print(dt3.is_leap_year())

print(dt1 > dt2)
print(dt1 < dt2)

# TODO: Create a Period using difference
print("dt1 =", dt1, "\ndt2 =", dt2)
p = dt1.diff(dt2)
print(p.in_hours(), "hours")
print(p.in_days(), "days")
print(p.in_months(), "months")

p = dt2.diff_for_humans(dt1)
print(p)