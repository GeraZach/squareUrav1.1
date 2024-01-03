
def remove_useless_zeroes(fractional):

    index = len(fractional) - 1

    while fractional[index] == '0' and index >= 0:
        index -= 1

    fixed_str = fractional[:index+1]

    if fixed_str == '':
        fixed_str += '0'

    return fixed_str

# print(remove_useless_zeroes('0'))

def if_starts_w_dot(unsigned_str):
    if unsigned_str[0] == '.':
        return '0' + unsigned_str
    else:
        return unsigned_str

#returns strings !!!!1
def get_exponent(fractional_w_exponent):
    if 'e' in fractional_w_exponent:
        fractional, exponent = fractional_w_exponent.split('e')
        return fractional, exponent

    else:
        return fractional_w_exponent, '0'



def is_number_negative(str_num):
    if str_num[0] != '-' and str_num[0] != '+':
        return False, str_num

    elif str_num[0] == '-':
        return True, str_num[1:]

    elif str_num[0] == '+':
        return False, str_num[1:]


def prepare_to_transform(unsigned_str):

    unsigned_str = if_starts_w_dot(unsigned_str)

    if '.' in unsigned_str:
        whole, fractional_w_exponent = unsigned_str.split('.')
        fractional, exponent = get_exponent(fractional_w_exponent)

        if fractional != '0' and fractional != '':
            fractional = remove_useless_zeroes(fractional)
        else:
            fractional = ''

        to_get_contained_fractional = fractional
        to_get_contained_whole = whole

        from exponent_operations import exp_plus

        exponent = exp_plus.exp_to_int(exponent) - len(fractional)

    else:
        to_get_contained_whole = unsigned_str
        to_get_contained_fractional = ''
        exponent = 0

    return to_get_contained_whole, to_get_contained_fractional, exponent


def transform_whole(whole):

    container = dict()

    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    dictIndex = len(whole) - 1

    index = 0

    while index < len(whole):
        container[dictIndex] = strToInt[whole[index]]
        index += 1
        dictIndex -= 1

    return container, index - 1

# print(transform_whole('123'))


def transform_fractional(fractional):

    container = dict()

    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    index = 0

    dictIndex = -1

    while index < len(fractional):
        container[dictIndex] = strToInt[fractional[index]]
        index += 1
        dictIndex -= 1

    return container, dictIndex + 1


def to_container(str_num):
    isNeg, unsigned_str = is_number_negative(str_num)

    wholePart, fractionalPart, exponent = prepare_to_transform(unsigned_str)

    wholeContainer, wholeLen = transform_whole(wholePart)
    fractionalContainer, fracLen = transform_fractional(fractionalPart)

    container = wholeContainer | fractionalContainer

    container['exponent'] = exponent
    container['isNeg'] = isNeg
    container['lastIndFrac'] = fracLen
    container['lastIndWhole'] = wholeLen

    return container

print(to_container('-123.533e3'))
