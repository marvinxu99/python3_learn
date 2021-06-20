#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today is: ", today)

  # print out the date's individual components
  print("Date components: ", today.year, today.month, today.day)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  days = ['Mon', 'Tue', 'Wed', 'Thu', "Fri", 'Sat', 'Sun']
  print("today's weekday is: ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today2 = datetime.now()
  print('The current date and time is ', today2)
  
  # Get the current time
  t = datetime.time(today2)
  print(t)
 
  # The following is the same as date.today()
  datetime.date(datetime.now())
  
  
if __name__ == "__main__":
  main();
  