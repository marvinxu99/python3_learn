# read the contents of configuration files
import configparser


# TODO: Create the configuration parser
parser = configparser.ConfigParser()

# TODO: Read the configuration file
parser.read('config.cfg')

# TODO: print the sections
print(parser.sections())
print(parser.has_section('Section 1'))

# TODO: Access one of the default values
use_time_travel = bool(parser['DEFAULT']['UseTimeTravel'])
print(use_time_travel)
print(type(use_time_travel))

# TODO: Demonstrate the getXXX convenience functions
use_time_travel = parser.getboolean('DEFAULT', 'UseTimeTravel')
print(use_time_travel)
print(type(use_time_travel))

opd = parser.getboolean('DEFAULT', 'ObeyPrimeDirective')
print(opd)

dyj = parser['DEFAULT'].getint('DefaultYearJump')
print(dyj, type(dyj))

speed = parser.getfloat('DEFAULT', 'Ship Speed') 
print(speed, type(speed))

# TODO: Access a non-existent value
try:
    titile = parser['Section 3']['title']
    print(titile)
except KeyError as err:
    print(err)