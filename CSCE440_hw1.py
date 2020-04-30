import math


def f(x):
    # return 2 * x ** 3 - x ** 2 + 6 * x - math.e ** x + 2
    # return 3 * x ** 4 + x ** 2 - 2
    return 3 * x - 3 * x ** 2 + 2 * math.e ** x - 2
    # return 2 * x - math.cos(x)


def g(x):
    return (3 * x ** 2 - 2 * math.e ** x + 2)/3
    # return math.sqrt((3*x + 2 * math.e ** x - 2)/3)
    # return 3 + 2 * (math.e ** x) / x - (2/x)
    # return math.log((3 * x ** 2 - 3 * x + 2)/2, math.e)


def f_prime(x):
    h = .00000000001
    out = (f(x+h) - f(x))/h
    return out


def bisection(a, b, tol):
    print("===================Bisection===============")
    i = 1  # iteration counter

    maxIteration = 50
    f_a = f(a)
    p = b

    while (i < maxIteration):
        p_temp = p
        p = a + (b - a)/2
        f_p = f(p)

        if f_p == 0 or (b - a)/2 < tol:
            print('solution:' + str(p))
            break
        print(p)

        i += 1

        if (f_a * f_p) > 0:
            a = p
            f_a = f_p
        else:
            b = p


def fixedPoint(p_0, tol):
    print("=========================Fixed Point======================")
    i = 1  # iteration counter

    maxIteration = 50
    while (i < maxIteration):
        p = g(p_0)
        # print(str(f(p)))
        if abs(p - p_0) < tol:
            # print("%.0f: %.8f %.8f (root found)" % (i, p, f(p)))
            print(p)
            print("solution:" + str(p))
            break
        # print("%.0f: %.8f %.8f" % (i, p, f(p)))
        print(p)
        p_0 = p
        i += 1


def newtonsMethod(p_0, tol):
    print("===================Newton's Method==========================")
    i = 1
    maxIterations = 50

    while i < maxIterations:
        p = p_0 - f(p_0)/f_prime(p_0)
        # print("%.0f %.8f %.8f %.8f" % (i, p_0, p, f(p)))
        print(p_0)
        if abs(p - p_0) < tol:
            print('solution ' + str(p))
            break
        i += 1
        p_0 = p


def secant(p_0, p_1, tol):
    print("============================Secant========================")
    i = 2
    q_0 = f(p_0)
    q_1 = f(p_1)
    maxIterations = 50
    while (i < maxIterations):
        p = p_1 - q_1*(p_1 - p_0)/(q_1 - q_0)
        f_p = f(p)
        print(str(p))
        if f_p == 0 or abs(p - p_1) < tol:
            print('solution ' + str(p))
            break
        i += 1
        p_0 = p_1
        q_0 = q_1
        p_1 = p
        q_1 = f(p)


bisection(-2, 2, .0001)
fixedPoint(-1, .0001)
newtonsMethod(.5, .0001)
secant(-2, 2,.0001)
