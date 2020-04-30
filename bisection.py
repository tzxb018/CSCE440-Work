import math
import pandas as pd
import numpy as np


def f(x):
    # return x ** 3 + 4 * x ** 2 - 10
    # return 2 * x ** 3 - x ** 2 + 6 * x - math.e ** x + 2
    return 3 * x ** 4 + x ** 2 - 2


def bisection(a, b, tol):
    i = 1  # iteration counter

    maxIteration = 50
    f_a = f(a)
    p = b
    print("%-5s %-10s %-10s %-10s %-10s %-10s" %
          ('i', 'a', 'b', 'p', 'f_p', 'rel_error'))

    while (i < maxIteration):
        p_temp = p
        p = a + (b - a)/2
        f_p = f(p)
        # print(str(p) + " " + str(p_temp))

        if f_p == 0 or (b - a)/2 < tol:
            print('solution:' + str(p))
            break
        if p != 0:
            rel_error = abs(p - p_temp)/p
            print(a)
            # print("%-5.0f %-5.8f %-5.8f %-5.8f %-5.8f %5.8f" %
            #       (i, a, b, p, f_p, rel_error))
        else:
            print(a)
            # print("%-5.0f %-5.8f %-5.8f %-5.8f %-5.8f %5.8f" %
            #       (i, a, b, p, f_p, 0))

        i += 1

        if (f_a * f_p) > 0:
            a = p
            f_a = f_p
        else:
            b = p
