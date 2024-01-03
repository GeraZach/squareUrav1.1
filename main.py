from functions import *
from Dump.v2funcs import *

a,b,c = input_module()


roots = solve_equation(a, b, c)

if roots is None:
    print('(nan, nan)')   # None
else:
    print(roots)


