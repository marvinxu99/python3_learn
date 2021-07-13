# read the contents of configuration files
import configparser


# Create the configuration parser
parser = configparser.ConfigParser()

# Read the configuration file
parser.read("config.cfg")

# print the sections
print(parser.sections())
print(parser.has_section("Section 1"))

# Access one of the default values
using_time_travel = bool(parser['DEFAULT']['UseTimeTravel'])
print(using_time_travel)
print(type(using_time_travel))

# Demonstrate the getXXX convenience functions
opd = parser['DEFAULT'].getboolean('ObeyPrimeDirective')
print(opd)
speed = parser['DEFAULT'].getfloat('Ship Speed')
print(speed)

# Access a non-existent value
try:
    title = parser['Section 3']['Title']
    print(title)
except KeyError as err:
    print("Whoa! There is no ", err)
