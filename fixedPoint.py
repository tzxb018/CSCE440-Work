import math


def f(x):
    return 2 * x ** 3 - x ** 2 + 6 * x - math.e ** x + 2


def g(x):
    return (2 * x ** 3 - x ** 2 - math.e ** x + 2)/-6


i = 1  # iteration counter
p_0 = 1.5  # starting value
tol = .0001  # tolerance level

maxIteration = 50
while (i < maxIteration):
    p = g(p_0)
    # print(str(f(p)))
    if abs(p - p_0) < tol:
        # print("%.0f: %.8f %.8f (root found)" % (i, p, f(p)))
        print(f(p))
        print("solution:" + str(p))
        break
    # print("%.0f: %.8f %.8f" % (i, p, f(p)))
    print (f(p))
    p_0 = p
    i += 1
