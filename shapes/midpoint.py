# INFORMATION
# FOR TWO POINTS
#   X1 + X2   Y1 + Y2
#   -------,  -------
#      2         2
#
# IF ONLY ONE IS AVAILABLE, DO JUST THAT

from math import *

# define dimensions
x1 = 4
x2 = 2
y1 = 4
y2 = 2

# announce
print("find midpoint of ({0} , {1}) and ({2} , {3})"
    .format(x1,y1,x2,y2))

# math
x_sum = x1 + x2
y_sum = y1 + y2

x_final = x_sum / 2
y_final = y_sum / 2

# tell user
print("midpoint is ({0} , {1})"
    .format(x_final, y_final))
