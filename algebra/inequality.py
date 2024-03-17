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
        print(f"{number1} is not greater than {number2}")
    else:
        print(f"{number1} is greater than {number2}")
elif context == "gte":
    if not number1 >= number2:
        print(f"{number1} is not greater than or equal to {number2}")
    else:
        print(f"{number1} is greater than or equal to {number2}")
elif context == "lt":
    if not number1 < number2: 
        print(f"{number1} is not less than {number2}")
    else:
        print(f"{number1} is less than {number2}")
elif context == "lte":
    if not number <= number2:
        print(f"{number1} is not less than or equal to {number2}")
    else:
        print(f"{number1} is less than or equal to {number2}")

