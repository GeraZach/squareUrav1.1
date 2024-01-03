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

    if co_str.count('e') > 1:
        return False

    if co_str.count('/') > 1:
        return False

    if '/' in co_str:
        co_str = Fraction(co_str)
        return True

    return True


while len(nums) < 3:
    correct_input = False
    while correct_input == False:

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


def string_to_fraction(nums):
    nums = list(map(Fraction, nums))
    return nums


if '/' in nums[0] or '/' in nums[1] or '/' in nums[2]:   ## def check fractions
    nums = string_to_fraction(nums)


a = '23e3'