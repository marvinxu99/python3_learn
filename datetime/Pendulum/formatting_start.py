# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
import pendulum

# create a datetime and print it
dt1 = pendulum.datetime(2020, 7, 28, 15, 30)
print(dt1)

# TODO: use some formatting functions
print(dt1.to_date_string())
print(dt1.to_time_string())
print(dt1.to_datetime_string())

# TODO: use functions for nice formatting
print(dt1.to_formatted_date_string())
print(dt1.to_day_datetime_string())

# TODO: use some common formats
print(dt1.to_cookie_string())
print(dt1.to_iso8601_string())
print(dt1.to_rfc822_string())

# TODO: use the format function for pretty printing
print(dt1.format("YYYY MM-DD HH:MM A"))
print(dt1.format("YYYY MM-DD HH:MM"))

# TODO: use localization
print(dt1.format("dddd DD MMM YYYY", locale='de'))
print(dt1.format("dddd DD MMM YYYY", locale='fr'))

# day of week, day of year
dt2 = pendulum.now()
print(dt2) 
print("day of week:", dt2.day_of_week) 
print("day of year:", dt2.day_of_year)
