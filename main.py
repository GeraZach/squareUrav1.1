import cmath
from fractions import Fraction


# Сделать ввод комплексных, ввод инф без флота,

def calc_roots(a, b, c):

    discriminant = b ** 2 - 4 * a * c

    if a == 0:
        if b == 0:
            if c == 0:
                return "Бесконечное число решений"
            else:
                return "Нет корней."
        else:
            root = -c / b

            if root == -0.0:
                return abs(root)
            else:
                return root



    elif discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        if root1 == -0.0:
            root1 = abs(root1)
        if root2 == -0.0:
            root2 = abs(root2)

        return root1, root2

    elif discriminant == 0:
        root1 = -b / (2 * a)
        root2 = root1
        if root1 == -0.0:
            return abs(root1), abs(root2)
        else:
            return root1, root2

    elif discriminant < 0:



        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)


        formatted_root1 = f"{root1.real:.1f}{'+' if root1.imag >= 0 else '-'}{abs(root1.imag):.1f}i"
        formatted_root2 = f"{root2.real:.1f}{'+' if root2.imag >= 0 else '-'}{abs(root2.imag):.1f}i"

        return formatted_root1, formatted_root2


def is_valid(co_str):

    co_str.lower()

    if not co_str:
        return False

    invalid_chars = set(co_str) - set("0123456789.+-eEinfnaNA/")
    if invalid_chars:
        return False

    if co_str.count('.') > 1:
        return False

    if co_str.count("+") > 1:
        return False

    # if co_str.count("-") > 1:
    #     return False

    if co_str.count('e') > 1:
        return False

    if co_str.count('/') > 1:
        return False

    if '/' in co_str:
        co_str = Fraction(co_str)
        return True

    return True



nums = []

while len(nums) < 3:
    correct_input = False
    while correct_input == False:
        print("Введите 3 коэффициента квадратного уравнения:")
        ins = input().strip().split()
        a_str = ins[0]
        b_str = ins[1]
        c_str = ins[2]
        if is_valid(a_str) and is_valid(b_str) and is_valid(c_str) is True:
            nums.append(a_str)
            nums.append(b_str)
            nums.append(c_str)
            break
        else:
            print("Введено некорректное число")
            continue
if '/' in nums[0] or '/' in nums[1] or '/' in nums[2]:
    nums[0] = Fraction(nums[0])
    nums[1] = Fraction(nums[1])
    nums[2] = Fraction(nums[2])


a = float(nums[0])
b = float(nums[1])
c = float(nums[2])

roots = calc_roots(a, b, c)

if roots is None:
    print("Вывод: Нет корней") # None
elif type(roots) is not float:
    print(f"Вывод: {roots[0]} | {roots[1]}")
else:
    print("Вывод: ", roots)
