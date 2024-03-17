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
print(f"a={a}, b={b}, c={c}")

if a == "unknown":
    print(f"a is {sqrt(c*c - b*b)}")
elif b == "unknown":
    print(f"b is {sqrt(c*c - a*a)}")
elif c == "unknown":
    print(f"c is {sqrt(a*a + b*b)}")
