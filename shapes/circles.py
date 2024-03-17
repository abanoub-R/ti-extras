# INFORMATION
# DEG TO RAD = DEG/1 * PI/180
# RAD TO DEG = RAD/1 * 180/PI

from math import *

# convert from degrees to radians or vice versa
convert_to_radians = False

# parameters
value = 30

if convert_to_radians == True:
    print(f"attempting to convert {value} degrees to radians")
    numerator = value * pi
    denominator = 180
    total = numerator / denominator
else:
    print(f"attempting to convert {value} radians to degrees")
    numerator = value * 180
    denominator = pi
    total = numerator / denominator

print(f"got {total}")
