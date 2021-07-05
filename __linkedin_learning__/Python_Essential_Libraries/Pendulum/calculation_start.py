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


# TODO: negative values also work


# TODO: Try comparing datetimes


# TODO: Create a Period using difference
