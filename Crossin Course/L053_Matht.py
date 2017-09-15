# Dorian Wang 2017.09.01
# lesson 53: Math

import math


def abc(a, b, c):
    if a == 0:
        print("x = %f" % -c / b)
    else:

        print("x1 = %f" % ((- b + math.sqrt(b * b - 4 * a * c)) / (2 * a)))
        print("x2 = %f" % ((- b - math.sqrt(b * b - 4 * a * c)) / (2 * a)))


abc(1.0, -3.0, 2.0)
