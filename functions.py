
from fractions import Fraction

noRootsOutput = "Нет корней"
infiniteRootsOutput = "Бесконечное число решений"
fullEquation = 'Equation is solved normally'


epsilon = 1e-6


def negative_zero_check(root1):
    if abs(root1) < epsilon:
        root1 = 0.0
        return root1
    else:
        return root1


def fix_output_imaginary(root1, root2):

    root1_str = str(root1).replace('j', 'i').strip('()')
    root2_str = str(root2).replace('j', 'i').strip('()')

    return root1_str, root2_str


def discriminant(a,b,c):
    D = b ** 2 - 4 * a * c
    return D


def calculate_roots(a, b, c, D):

    root1 = complex(-b + D ** 0.5) / (2 * a)  # def roots calc, roots output
    root2 = complex(-b - D ** 0.5) / (2 * a)

    return root1, root2


def a_is_zero(b, c):
    root = -c / b
    root = negative_zero_check(root)
    return root


def coefficients_zero_check(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return infiniteRootsOutput
            else:
                return noRootsOutput
        else:
            return a_is_zero(b, c)
    else:
        return fullEquation


def discriminant_equals_zero(a, b):

    root1 = -b / (2 * a)
    root1 = negative_zero_check(root1)
    root2 = root1

    return root1, root2


def solve_equation(a, b, c):
    if coefficients_zero_check(a, b, c) == fullEquation:

        D = discriminant(a, b, c)

        root1, root2 = calculate_roots(a, b, c, D)

        if D > 0:
            return root1, root2

        elif D < 0:
            return fix_output_imaginary(root1, root2)

        elif D == 0:
            return discriminant_equals_zero(a, b)

    else:
        return coefficients_zero_check(a, b, c)





