tokens = {
    'SIGN': '1',
    'DIGIT': '2',
    'DOT': '3',
    'BLANK_SPACE': '4',
    'EXPRESSION': '5',
    'I_IMAG': '6',
    'EXPONENT': '7'
                }

SIGN = ('+', '-')
DIGIT = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
DOT = ['.',',']
BLANK_SPACE = [' ']
EXPRESSION = ['+', '-']
I_IMAG = ['i', 'j']
EXPONENT = ('e', "E")
EMPTY_STR = ['']

INT_TYPES = ('SIGNED_INT', "UNSIGNED_INT")

INVALID_INPUT = "INVALID_INPUT"

def remove_starting_zeroes(str_num):

    sign = ''
    onlyZeroes = False

    if str_num[0] == '+' or str_num[0] == '-':
        sign = str_num[0]
        str_num = str_num[1:]

    if str_num[0] == '0':
        zeroesCount = 0
        for char in str_num:

            if char not in DIGIT and char != '.':
                return INVALID_INPUT

            if char == '0':
                zeroesCount += 1
            elif char == '.':
                onlyZeroes = True
                break
            else:
                break

        str_num = str_num[zeroesCount:]

        if onlyZeroes:
            str_num = '0' + str_num


    return sign + str_num

def correct_input(str_num):
    str_num = str_num.replace(',', '.')
    str_num = str_num.replace('E', 'e')

    if str_num[0] == '.':
        str_num = '0' + str_num

    str_num = remove_starting_zeroes(str_num)

    return str_num


def to_list(str_num):
    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.', ',': '.', 'e': 'e', 'E': 'e', '+': '+', '-': '-'}

    str_num = correct_input(str_num)

    if str_num.count('.') == 0:
        str_num += '.0'

    num_array = []
    for char in str_num:
        num_array.append(strToInt[char])

    return num_array


def parse_str_number(str_num):
    parseResult = ''


    for char in str_num:
        if char in SIGN:
            parseResult += tokens['SIGN']

        elif char in DIGIT:
            parseResult += tokens['DIGIT']

        elif char in DOT:
            parseResult += tokens["DOT"]

        elif char in BLANK_SPACE:
            parseResult += tokens['BLANK_SPACE']

        elif char in EXPRESSION:
            parseResult += tokens["EXPRESSION"]

        elif char in I_IMAG:
            parseResult += tokens["I_IMAG"]

        elif char in EXPONENT:
            parseResult += tokens["EXPONENT"]

        elif char in EMPTY_STR:
            parseResult = INVALID_INPUT

        else:
            parseResult = INVALID_INPUT

    if len(parseResult) == 0:
        return "INVALID INPUT"

    return parseResult

def big_int(str_num):

    parseResult = parse_str_number(str_num)

    if parseResult == INVALID_INPUT:
        return INVALID_INPUT

    if (str_num[0] == '+' or str_num[0] == '-') and set(parseResult[1:]) == set('2'):
        str_num += '.0'
        # return to_list(str_num)
        return "SIGNED_INT"

    elif set(parseResult) == set('2'):
        str_num += '.0'

        # return to_list(str_num)
        return "UNSIGNED_INT"

    else:
        return big_float(str_num, parseResult)


def big_float(str_num, parseResult):

    if parseResult.startswith('13'):
        str_num = str_num[0] + '0' + str_num[1:]

    if parseResult[0] == '3':
        str_num = '0' + str_num

    if parseResult[-1] == '3':
        str_num += '0'

    #Check num of exponents
    if parseResult.count('7') > 1:
        return INVALID_INPUT

    elif parseResult.count('7') == 0:
        if parseResult.count('3') == 1:
            WHOLE, FRACTIONAL = str_num.split('.')

            if big_int(WHOLE) in INT_TYPES and big_int(FRACTIONAL) == "UNSIGNED_INT":

                # return to_list(str_num)

                return 'FLOAT'
            else:
                return INVALID_INPUT
        else:
            return INVALID_INPUT

    elif parseResult.count('7') == 1:
         return big_float_with_exp(str_num, parseResult)

    else:
        return INVALID_INPUT


def big_float_with_exp(str_num, parseResult):
    if parseResult.count('3') > 1:
        return INVALID_INPUT

    if parseResult.count('3') == 0:
        str_num += '.0'
        parseResult += '32'

    whole, fraction = str_num.split('.')

    if 'e' in whole:
        if whole[-1] != 'e' and whole[0] != 'e':
            if big_int(fraction) == "UNSIGNED_INT":
                mantissa, exponent = whole.split('e')
                if big_int(mantissa) in INT_TYPES and big_int(exponent) in INT_TYPES:
                    return "FLOAT_EXP"

                else:
                    return INVALID_INPUT
            else:
                return INVALID_INPUT
        else:
            return INVALID_INPUT

    elif 'e' in fraction:
        if fraction[-1] != 'e':
            if fraction[0] == 'e':
                exponent = fraction[1:]
                if big_int(exponent) in INT_TYPES:
                    return "FLOAT_EXP"
                else:
                    return INVALID_INPUT
            else:
                if big_int(whole) in INT_TYPES:
                    mantissa, exponent = fraction.split('e')
                    if big_int(mantissa) in INT_TYPES and big_int(exponent) in INT_TYPES:
                        return "FLOAT_EXP"

                    else:
                        return INVALID_INPUT
                else:
                    return INVALID_INPUT
        else:
            return INVALID_INPUT
    else:
        return INVALID_INPUT


# str_num = '1.'

# print(big_int(str_num))


def validate(str_num):
    numType = big_int(str_num)
    if numType != INVALID_INPUT:
        return to_list(str_num)
    else:
        return INVALID_INPUT

# print(validate(str_num))

#   0001
# + 0001
# .0
# 1.
#1. 0. - не прописаны

# соло знаки + -

# inf. nan
