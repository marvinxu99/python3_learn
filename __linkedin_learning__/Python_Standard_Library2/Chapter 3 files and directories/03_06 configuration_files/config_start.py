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


# TODO: Demonstrate the getXXX convenience functions


# TODO: Access a non-existent value

