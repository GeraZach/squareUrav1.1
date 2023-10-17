from functions import *


try:
    a, b, c = list(map(float, input().split()))
except ValueError:
    print("Incorrect input: Only numbers are accepted")
    exit()


roots = solve_equation(a, b, c)

if roots is None:
    print('(nan, nan)')   # None
else:
    print(roots)


