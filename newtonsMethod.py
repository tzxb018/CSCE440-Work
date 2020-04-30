import math


def f(x):
    # return 2 * x ** 3 - x ** 2 + 6 * x - math.e ** x + 2
    return 3 * x ** 4 + x ** 2 - 2

# using the def of a derivative to give f'


def f_prime(x):
    h = .00000000001
    out = (f(x+h) - f(x))/h
    return out


i = 1
maxIterations = 50
p_0 = -.5
tol = .0001

while i < maxIterations:
    p = p_0 - f(p_0)/f_prime(p_0)
    # print("%.0f %.8f %.8f %.8f" % (i, p_0, p, f(p)))
    print(p_0)
    if abs(p - p_0) < tol:
        print('solution ' + str(p))
        break
    i += 1
    p_0 = p
