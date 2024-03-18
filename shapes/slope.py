# INFORMATION
# FORMULA FOR SLOPE IS AS FOLLOWS
#
# Y2 - Y1
# -------
# X2 - X1

from math import *

# define variables
y2 = 2
y1 = 1
x2 = 2
x1 = 1

# get offset
offset_y = y2 - y1
offset_x = x2 - x1

# get slope and return to user
print("slope of ({x1},{y1}) and ({x2},{y2}) is {offset_y/offset_x}"
    .format(x1=x1,y1=y1,x2=x2,y2=y2))
