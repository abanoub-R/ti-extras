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
print(f"slope of ({x1},{y1}) and ({x2},{y2}) is {offset_y/offset_x}")
