def get_types(num1, num2):

    # можно добавить поддтипы complexnegative, complexpositive, floatnegative, floatpositive

    if 'i' in num1:
        type1 = 'complex'
    else:
        type1 = 'float'

    if 'i' in num2:
        type2 = 'complex'
    else:
        type2 = 'float'

    return type1, type2


def get_sign_and_type(num1, num2):
    type1, type2 = get_types(num1, num2)

    if type1 == 'float' and type2 == 'float':
        if num1[0] == '-':
            sign1 = 'neg'
        else:
            sign1 = 'pos'

        if num2[0] == '-':
            sign2 = 'neg'
        else:
            sign2 = 'pos'

        return sign1, type1, sign2, type2
