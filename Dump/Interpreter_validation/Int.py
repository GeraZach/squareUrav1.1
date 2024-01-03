def is_int_valid(str_num):
    tokens = {
        'SIGN': '1',
        'DIGIT': '2',
        'DOT': '3',
        'BLANK_SPACE': '4',
        'EXPRESSION': '5',
        'I_IMAG': '6',
        'EXPONENT': '7'
    }

    SIGN = ['+', '-']
    DIGIT = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    DOT = ['.']
    BLANK_SPACE = [' ']
    EXPRESSION = ['+', '-']
    I_IMAG = ['i', 'j']
    EXPONENT = ['e', "E"]

    #RULES
    #IF NO EXPONENT (SIGNED INT)
def signed_int_no_exp(str_num):
    if str_num[0] == '1' and str_num.count('7') == 0:
        if set(str_num) != ('2'):
            return 'INVALID'
    return str_num

    #IF EXPONENT (SIGNED INT)
# def signed_int_exp(str_num):
#     elif str_num[0] == '1' and str_num.count('7') == 1:
#         int_part, exponent_part = str_num.split('7')
#
#         if
