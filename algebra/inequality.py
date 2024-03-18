# INFORMATION
# VARIABLES CANNOT BE INSERTED
# gt = greater
# gte = greater than or equal to
# lt = less than
# lte = less than or equal to

from math import *

number1 = 2
number2 = 2
context = "gte"

if context == "gt":
    if not number1 > number2:
        print("{} is not greater than {}".format(number1, number2))
    else:
        print("{} is greater than {}".format(number1, number2))
elif context == "gte":
    if not number1 >= number2:
        print("{} is not greater than or equal to {}".format(number1, number2))
    else:
        print("{} is greater than or equal to {}".format(number1, number2))
elif context == "lt":
    if not number1 < number2:
        print("{} is not less than {}".format(number1, number2))
    else:
        print("{} is less than {}".format(number1, number2))
elif context == "lte":
    if not number1 <= number2:
        print("{} is not less than or equal to {}".format(number1, number2))
    else:
        print("{} is less than or equal to {}".format(number1, number2))

