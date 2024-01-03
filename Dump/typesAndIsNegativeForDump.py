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


def is_negative(num1, num2):
    type1, type2 = get_types(num1,num2)

    return 0