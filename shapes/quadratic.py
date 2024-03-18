# THIS DOES NOT SOLVE THE ENTIRE QUADRATIC
# THIS WILL ONLY GET THE PARTS OF THE EQUATION

# INFORMATION
# QUADRATIC FORMULA IS AS FOLLOWS:
#
# -B +- SQRT(B^2 + 4(A)(C))
# -------------------------
#           2A

from math import *

# formula parameters, relative to X
a = 1
b = 2
c = 3

# repeat parameters to user
print("a={a}, b={b}, c={c}".format(a=a,b=b,c=c))

# get parts of formula
b_squared = b*b
b_external = b * -1
ac_quad = 4 * a * c

# tell the user specific parts
print("inside square root: ",b_squared - ac_quad)
print("outside square root: ",b_squared)
print("divide by:",a*2)
print("product of solutions: ", c/a)
