def exp_to_int(str_exp):
    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


    toNeg = False

    if str_exp[0] == '-':
        str_exp = str_exp[1:]
        toNeg = True

    elif str_exp[0] == '+':
        str_exp = str_exp[1:]

    length = len(str_exp) - 1

    int_exp = 0

    for str_digit in str_exp:
        int_exp += strToInt[str_digit] * 10 ** length
        length -= 1

    if toNeg:
        int_exp *= -1

    return int_exp
