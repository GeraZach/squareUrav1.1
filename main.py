import cmath
from fractions import Fraction
from functions import *

nums = input().split()

if '/' in nums[0] or '/' in nums[1] or '/' in nums[2]:
    nums = string_to_fraction(nums)

a = float(nums[0])
b = float(nums[1])
c = float(nums[2])

roots = calculate_roots(a, b, c)

if roots is None:
    print(noRootsOutput)   # None
else:
    print(roots)
