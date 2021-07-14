import datetime

now = datetime.datetime.now()
one_year = datetime.timedelta(days=365) 
one_week = datetime.timedelta(weeks=1) 

print("One year from now will be: ".format(width=50, justify='right'), now + one_year)
print("One week from now will be: ", now + one_week)
print("One week ago was: ".rjust(27, '.'), now - one_week)

# stringName.center(width,fillChar)

# ljust, center, rjust
names = ["Amy", "John", "George", "Michael", "Penelope"]
biggest = max(len(name) for name in names)

for name in names:
    print(name.ljust(biggest+2, '-') + ':')

for name in names:
    print(name.center(biggest+2, '-') + ':')

for name in names:
    print(name.rjust(biggest+2, '-') + ':')