
from fractions import Fraction

noRootsOutput = "Нет корней"
infiniteRootsOutput = "Бесконечное число решений"

epsilon = 1e-6


def string_to_fraction(nums):
    nums = list(map(Fraction, nums))
    return nums


def check_roots(a, b, c):

    if a == 0:
        if b == 0:
            if c == 0:
                return infiniteRootsOutput
            else:
                return noRootsOutput
        else:
            root = -c / b
            if abs(root) < epsilon:
                root = 0.0
            return root
    else:
         return False


def calculate_roots(a, b, c):

    if check_roots(a, b, c) is False:

        discriminant = b ** 2 - 4 * a * c

        root1 = complex(-b + discriminant ** 0.5) / (2 * a)
        root2 = complex(-b - discriminant ** 0.5) / (2 * a)

        root1_str = str(root1).replace('j', 'i').strip('()')
        root2_str = str(root2).replace('j', 'i').strip('()')

        if discriminant > 0 or discriminant < 0:
            return root1_str, root2_str

        elif discriminant == 0:
            root1 = -b / (2 * a)
            root2 = root1
            if abs(root1) < epsilon and abs(root2) < epsilon:
                root1 = 0.0
                root2 = 0.0
            return root1, root2

    else:
        return check_roots(a, b, c)



