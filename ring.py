# ring.py

import sys
from math import pi

if len(sys.argv) != 3: # display error message for missing arguments
    raise SystemExit("usage : ring.py \"metal\" radius")

# sys.argv[0] is the file name
# metal = "Copper"
metal = sys.argv[1]

# radius = 10
# input is read as string therefore it is converted into float
radius = float(sys.argv[2])

perimeter = 2*pi*radius
area = pi * radius**2

print("Metal =", metal)
# print("pi =", pi)
print("Perimeter = ", perimeter)
print("area =", area)