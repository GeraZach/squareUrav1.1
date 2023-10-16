import cmath
from fractions import Fraction
from functions import *
try:

    a, b, c = list(map(float, input().split()))

    roots = solve_equation(a, b, c)

    if roots is None:
        print(noRootsOutput)   # None
    else:
        print(roots)

except ValueError:
    print("incorect input")
