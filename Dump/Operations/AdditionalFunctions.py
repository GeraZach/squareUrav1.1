def equalize_zero_length(fractional1, fractional2):

    MaxFracLen = max(len(fractional1), len(fractional2))

    if len(fractional1) < len(fractional2):
        fractional1 += '0' * (MaxFracLen - len(fractional1))
    else:
        fractional2 += '0' * (MaxFracLen - len(fractional2))

    return fractional1, fractional2


def equalize_length_int(num1, num2):
    MaxFracLen = max(len(num1), len(num2))

    if len(num1) < len(num2):
        num1 = '0' * (MaxFracLen - len(num1)) + num1
    else:
        num2 = '0' * (MaxFracLen - len(num2)) + num2

    return num1, num2

def equalize_zeros_for_minuses_frac(num1, num2):

    w1, f1 = num1.split('.')
    w2, f2 = num2.split('.')

    w1, w2 = equalize_length_int(w1, w2)
    f1, f2 = equalize_zero_length(f1, f2)

    num1 = f'{w1}.{f1}'
    num2 = f'{w2}.{f2}'
    return num1, num2
