from typesAndIsNegative import get_sign_and_type
from AdditionalFunctions import equalize_zero_length, equalize_length_int
from typesAndIsNegative import *
from AdditionalFunctions import equalize_zeros_for_minuses_frac, equalize_length_int



def int_for_plus_minus(num1, num2):
    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    intToStr = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    finalMinus = False

    # Не сравнивает по нормальному, например 15 и 100, 15 больше 100 получается
    num1Compare, num2Compare = equalize_length_int(num1, num2)

    # Неверно может сравнить числа например 15 и 100, 15 больше -- уравнять нули у целой части
    if num1Compare < num2Compare:
        num1, num2 = num2, num1
        finalMinus = True

    # Отдельная функция - допилить

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


def minusforPlusFunction(num1, num2):
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
    # Пока первое число больше второго или дробная часть больше хз
    #

    # Отдельная функция - допилить

    MaxFracLen = max(len(frac1), len(frac2))

    if len(frac1) < len(frac2):
        frac1 += '0' * (MaxFracLen - len(frac1))
    else:
        frac2 += '0' * (MaxFracLen - len(frac2))

    # Длинное вычитание

    finalWhole = int_for_plus_minus(whole1, whole2)

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



def plusFunction(firstFloat, secondFloat):

    sign1, firstType, sign2, secondType = get_sign_and_type(firstFloat, secondFloat)

    if sign1 != sign2:
        if sign1 == 'neg':
            firstFloat = firstFloat[1:]
            return minusforPlusFunction(secondFloat, firstFloat)

        if sign2 == 'neg':
            secondFloat = secondFloat[1:]
            return minusforPlusFunction(firstFloat, secondFloat)


    if firstType == 'complex' or secondType == 'complex':
        finalSum = complex_sum(firstFloat, secondFloat, firstType, secondType)

    elif firstType == 'float' and secondType == 'float':
        finalSum = float_sum(firstFloat, secondFloat)

    else:
        finalSum = None

    return finalSum


def float_sum(firstFloat, secondFloat):

    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    intToStr = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    firstWhole, firstFraction = firstFloat.split('.')
    secondWhole, secondFraction = secondFloat.split('.')


    finalWhole = long_Int_Plus(firstWhole, secondWhole)


    # Уравниваем длинну дробных частей нулями справа
    firstFraction, secondFraction = equalize_zero_length(firstFraction, secondFraction)


    # Как раз длинная арифметика ( Мне кажется не стоит раскидывать по функциям, т.к тут использование будет только в этой функции)

    position = len(firstFraction) - 1  # i

    finalFractional = ''
    oneFromBefore = False

    while position >= 0:
        digitsSum = strToInt[firstFraction[position]] + strToInt[secondFraction[position]]

        if oneFromBefore:
            digitsSum += 1
            oneFromBefore = False

        # Работает над числом перед точкой
        if position == 0:
            if digitsSum < 10:
                finalFractional = intToStr[digitsSum] + finalFractional
                break

            else:
                finalFractional = intToStr[digitsSum % 10] + finalFractional
                finalWhole = long_Int_Plus(finalWhole, '1')
                break

        # Работает с другими числами
        if digitsSum < 10:
            finalFractional = intToStr[digitsSum] + finalFractional

        else:
            finalFractional = intToStr[digitsSum % 10] + finalFractional
            oneFromBefore = True

        position -= 1

    # Костыль !!!!
    # Ставит минус перед целой частью при сложении двух отрицательных чисел

    if firstWhole[0] == '-' and secondWhole[0] == '-':
        finalWhole = '-' + finalWhole

    return (f'{finalWhole}.{finalFractional}')


def complex_sum(firstComplex, secondComplex, firstType, secondType):

    if firstType == 'complex' and secondType == 'complex':

        # Нужна проверка на знаки между реальной и вообр частью

        firstTokens = firstComplex.split()
        secondTokens = secondComplex.split()

        realPart1 = firstTokens[0]
        imaginaryPart1 = firstTokens[2].strip('i')

        realPart2 = secondTokens[0]
        imaginaryPart2 = secondTokens[2].strip('i')

        finalReal = float_sum(realPart1, realPart2)
        finalImaginary = float_sum(imaginaryPart1, imaginaryPart2) + 'i'

        finalComplex = f"{finalReal} + {finalImaginary}"

    return finalComplex

def long_Int_Plus(firstNum, secondNum):
    strToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    intToStr = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    if firstNum[0] == '-' and secondNum[0] == '-':
        firstNum = firstNum[1:]
        secondNum = secondNum[1:]

    firstNum, secondNum = equalize_length_int(firstNum, secondNum)


    position = len(firstNum) - 1  # i

    finalNumber = ''
    oneFromBefore = False

    while position >= 0:
        digitsSum = strToInt[firstNum[position]] + strToInt[secondNum[position]]

        if oneFromBefore:
            digitsSum += 1
            oneFromBefore = False

        # Работает над числом перед точкой
        if position == 0:
            if digitsSum < 10:
                finalNumber = intToStr[digitsSum] + finalNumber
                break

            else:
                finalNumber = intToStr[digitsSum % 10] + finalNumber
                finalNumber = '1' + finalNumber
                break


        # Работает с другими числами
        if digitsSum < 10:
            finalNumber = intToStr[digitsSum] + finalNumber

        else:
            finalNumber = intToStr[digitsSum % 10] + finalNumber
            oneFromBefore = True

        position -= 1

    return finalNumber




# В конце каждой функции должны урезаться нули с конца

# Может складывать числа одного знака, как и должно быть

# num1 = '25.' + ('6' * 10000)
# num2 = '26.' + ('6' * 1) - bug










# MINUS


def minusFunction(num1, num2):
    sign1, type1, sign2, type2 = get_sign_and_type(num1, num2)

    if sign1 != sign2:
        if sign1 == 'neg':
            num2 = '-' + num2
            return plusFunction(num1, num2)

        if sign2 == 'neg':
            num2 = num2[1:]
            return plusFunction(num1, num2)
    else:
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

    # Отдельная функция - допилить

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
    # Пока первое число больше второго или дробная часть больше хз
    #

    # Отдельная функция - допилить

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





num1 = '50.' + ('9' * 30000)
num2 = '50.' + ('9' * 30000)

test1 = '99.7'
test2 = '1.9'

comp1 = '25.25 + 5.6i'
comp2 = '25.25 + 5.6i'

#
import time
start_time = time.time()
#
# print(plusFunction('123.0', '23.0'))
print(minusFunction('10.55', '1.55'))
#
print("--- %s seconds ---" % (time.time() - start_time))


# print(int_minus('15','15'))

# Bug 0.0 - 0.1 == 0.1
# '1.01', '1.1' = 0.9 - Фиксится добавлением - перед строкой целого числа
# '25.0', '5.5' == -- 20.5 - bug


