#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  print(now.strftime("the current year is: %Y"))

  #### Date Formatting ####
  
  """
  # %y %Y - Year, 
  # %a %A - weekday, 
  # %m %b %B - month, 
  # %d    - day of month
  """
  print(now.strftime("%a %d-%B-%y"))  

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Local date and time: %c"))  
  print(now.strftime("Local date: %x"))  
  print(now.strftime("Local time: %X"))  

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, 
  # %M - minute, 
  # %S - second, 
  # %p - locale's AM/PM
  print(now.strftime("Current time: %I:%M:%S %p"))  
  print(now.strftime("24-hour time: %H:%M"))  


if __name__ == "__main__":
  main()
