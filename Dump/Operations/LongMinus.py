from typesAndIsNegative import *
from AdditionalFunctions import equalize_zeros_for_minuses_frac, equalize_length_int


def long_minus(num1,num2):
    sign1, type1, sign2, type2 = get_sign_and_type(num1, num2)





    # if type1 == 'complex' or type2 == 'complex':
    #     finalDifference = complex_minus(num1, num2, type1, type2)

    if type1 == 'float' and type2 == 'float':
        finalDifference = float_minus(num1, num2)

    return finalDifference

def int_minus(num1, num2):

    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    intToStr = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    finalMinus = False

    # Не сравнивает по нормальному, например 15 и 100, 15 больше 100 получается
    num1Compare, num2Compare = equalize_length_int(num1, num2)

    # Неверно может сравнить числа например 15 и 100, 15 больше -- уравнять нули у целой части
    if num1Compare < num2Compare:
        num1, num2 = num2, num1
        finalMinus = True

    #Отдельная функция - допилить

    MaxFracLen = max(len(num1), len(num2))

    if len(num1) < len(num2):
        num1 = '0' * (MaxFracLen - len(num1)) + num1
    else:
        num2 = '0' * (MaxFracLen - len(num2)) + num2

    position = len(num1) - 1

    finalNumber = ''
    nextMinus = False

    while position >= 0:
        digitsDiff = strToInt[num1[position]] - strToInt[num2[position]]

        if nextMinus:
            digitsDiff -= 1
            nextMinus = False

        if position == 0:
            if digitsDiff > 0:
                finalNumber = intToStr[digitsDiff] + finalNumber
            elif digitsDiff < 0:
                finalNumber = intToStr[digitsDiff + 10] + finalNumber
                # Заменить инт
                finalNumber = '1' + finalNumber
            elif digitsDiff == 0 and len(finalNumber) == 0:
                finalNumber = '0' + finalNumber


        else:
            if digitsDiff >= 0:
                finalNumber = intToStr[digitsDiff] + finalNumber
            elif digitsDiff < 0:
                finalNumber = intToStr[digitsDiff + 10] + finalNumber
                nextMinus = True

        position -= 1

    if finalMinus:
        finalNumber = '-' + finalNumber

    return finalNumber

def float_minus(num1, num2):

    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    intToStr = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    finalMinus = False

    if num1[0] == '-' and num2[0] == '-':
        num1 = num1[1:]
        num2 = num2[1:]
        finalMinus = True

    num1Compare, num2Compare = equalize_zeros_for_minuses_frac(num1, num2)

    # Неверно может сравнить числа например 15 и 100, 15 больше -- уравнять нули у целой части
    if num1Compare < num2Compare:
        num1, num2 = num2, num1
        finalMinus = True

    whole1, frac1 = num1.split('.')
    whole2, frac2 = num2.split('.')

    #
    #Пока первое число больше второго или дробная часть больше хз
    #

    #Отдельная функция - допилить

    MaxFracLen = max(len(frac1), len(frac2))

    if len(frac1) < len(frac2):
        frac1 += '0' * (MaxFracLen - len(frac1))
    else:
        frac2 += '0' * (MaxFracLen - len(frac2))

    # Длинное вычитание

    finalWhole = int_minus(whole1, whole2)

    position = len(frac1) - 1


    finalFractional = ''
    nextMinus = False

    while position >= 0:
        digitsDiff = strToInt[frac1[position]] - strToInt[frac2[position]]

        if nextMinus:
            digitsDiff -= 1
            nextMinus = False

        if position == 0:
            if digitsDiff >= 0:
                finalFractional = intToStr[digitsDiff] + finalFractional
            elif digitsDiff < 0:
                finalFractional = intToStr[digitsDiff + 10] + finalFractional
                # Заменить инт
                finalWhole = int_minus(finalWhole, '1')


        else:
            if digitsDiff >= 0:
                finalFractional = intToStr[digitsDiff] + finalFractional
            elif digitsDiff < 0:
                finalFractional = intToStr[digitsDiff + 10] + finalFractional
                nextMinus = True

        position -= 1


    if finalMinus == True:
        finalWhole = '-' + finalWhole

    return f'{finalWhole}.{finalFractional}'


print(float_minus('1.0', '1000.0'))

# print(int_minus('15','15'))

# Bug 0.0 - 0.1 == 0.1
# '1.01', '1.1' = 0.9 - Фиксится добавлением - перед строкой целого числа
# '25.0', '5.5' == -- 20.5 - bug


