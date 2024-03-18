# INFORMATION
# DEG TO RAD = DEG/1 * PI/180
# RAD TO DEG = RAD/1 * 180/PI

from math import *

# convert from degrees to radians or vice versa
convert_to_radians = False

# parameters
value = 30

if convert_to_radians == True:
    print("attempting to convert {value} degrees to radians".format(value=value))
    numerator = value * pi
    denominator = 180
    total = numerator / denominator
else:
    print("attempting to convert {value} radians to degrees".format(value=value))
    numerator = value * 180
    denominator = pi
    total = numerator / denominator

print("got {total}".format(total=total))
