# Formatting date and time information
import datetime

# create a datetime for today
now = datetime.datetime.now()

# print various day and month formatting
print(now.strftime("%a, %A, %w, %e"))
print(now.strftime("%b, %B, %m"))

# print various time formatting
print(now.strftime("%H, %I, %M, %S, %p"))

# Locale-specific
print(now.strftime("%c"))
print(now.strftime("%X"))

# short date format (m/d/y)
output = now.strftime("%m/%d/%y")
print("today is: ", output)

# long date format (Day, number, Month, Year)
output = now.strftime("%A %d, %B %Y")
print("today is: ", output)

# short date and time (m/d/y, H:M am/pm)
output = now.strftime("%m/%d/%y %I:%M %p")
print("today is: ", output)
