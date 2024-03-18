# INFORMATION:
# PYTHAGOREAN THEORUM IS AS FOLLOWS
#
# A^2 + B^2 = C^2
#
# "unknown" is used for anonymous variables
# as such, multiple across abc will result in
# undefined behavior

from math import *

# define measurements
a = 3
b = 4
c = "unknown"

# announce known variables
print("a={a}, b={b}, c={c}".format(a=a,b=b,c=c))

if a == "unknown":
    operation = sqrt(c*c - b*b)
    print("a is {1}".format(operation))
elif b == "unknown":
    operation = sqrt(c*c - a*a)
    print("b is {1}".format(operation))
elif c == "unknown":
    operation = sqrt(a*a + b*b)
    print(f"c is {1}".format(operation))
