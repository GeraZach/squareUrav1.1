def plus_addon(num_array1, num_array2):

    SIGNS = ('+', '-')

    negativeNumberFlag = False

    sign1 = num_array1[0]
    sign2 = num_array2[0]

    if sign1 in SIGNS:
        num_array1 = num_array1[1:]
    else:
        sign1 = '+'

    if sign2 in SIGNS:
        num_array2 = num_array2[1:]
    else:
        sign2 = '+'

    if sign1 == '-' and sign2 == '-':
        negativeNumberFlag = True

    # от сюда до 55 строки в функцию, такая же в минусе

    dotPlacement1 = num_array1.index('.') + 1
    dotPlacement2 = num_array2.index('.') + 1

    numLength1 = len(num_array1)
    numLength2 = len(num_array2)

    fracLength1 = numLength1 - dotPlacement1
    fracLength2 = numLength2 - dotPlacement2

    # 0's added to the back
    if fracLength1 < fracLength2:
        num_array1 += [0] * (fracLength2 - fracLength1)
    else:
        num_array2 += [0] * (fracLength1 - fracLength2)

    numLength1 = len(num_array1)
    numLength2 = len(num_array2)

    # 0's added to the front
    if numLength1 < numLength2:
        num_array1 = [0] * (numLength2 - numLength1) + num_array1
    else:
        num_array2 = [0] * (numLength1 - numLength2) + num_array2

    numLength1 = len(num_array1)

    position = numLength1-1

    finalNumber = []

    plusOneNext = False

    while position >= 0:

        if num_array1[position] == '.' or num_array2[position] == '.':
            finalNumber = ['.'] + finalNumber

        else:


            digitsSum = num_array1[position] + num_array2[position]

            if plusOneNext:
                plusOneNext = False
                digitsSum += 1

            if digitsSum > 9:
                plusOneNext = True
                surplus = digitsSum % 10

                if position == 0:
                    finalNumber = [1] + [surplus] + finalNumber
                    break

                finalNumber = [surplus] + finalNumber

            #digits sum less than 10
            else:
                finalNumber = [digitsSum] + finalNumber

        position -= 1

    if negativeNumberFlag:
        finalNumber = ['-'] + finalNumber

    return finalNumber


def minus(num_array1, num_array2):

    SIGNS = ('+', '-')

    finalMinus = False

    sign1 = num_array1[0]
    sign2 = num_array2[0]

    if sign1 in SIGNS:
        num_array1 = num_array1[1:]
    else:
        sign1 = '+'

    if sign2 in SIGNS:
        num_array2 = num_array2[1:]
    else:
        sign2 = '+'

    if sign1 == '-' and sign2 == '-':
        finalMinus = True

    if sign1 != sign2:
        if sign1 == '-':
            return plus_addon(['-'] + num_array2, ['-'] + num_array1)

        elif sign2 == '-':
            return plus_addon(num_array1, num_array2)

    # от сюда до 32 строки в функцию, такая же в плюсе

    dotPlacement1 = num_array1.index('.') + 1
    dotPlacement2 = num_array2.index('.') + 1

    numLength1 = len(num_array1)
    numLength2 = len(num_array2)

    fracLength1 = numLength1 - dotPlacement1
    fracLength2 = numLength2 - dotPlacement2

    # 0's added to the back
    if fracLength1 < fracLength2:
        num_array1 += [0] * (fracLength2 - fracLength1)
    else:
        num_array2 += [0] * (fracLength1 - fracLength2)

    numLength1 = len(num_array1)
    numLength2 = len(num_array2)

    # 0's added to the front
    if numLength1 < numLength2:
        num_array1 = [0] * (numLength2 - numLength1) + num_array1
    else:
        num_array2 = [0] * (numLength1 - numLength2) + num_array2

    #Сравниваем массивы
    # finalMinus = False
    if num_array1 < num_array2:
        finalMinus = True
        num_array1, num_array2 = num_array2, num_array1

    numLength1 = len(num_array1)

    position = numLength1 - 1

    finalNumber = []
    minusOneNext = False

    while position >= 0:

        if num_array1[position] == '.' or num_array2[position] == '.':

            finalNumber = ['.'] + finalNumber

            position -= 1
            continue

        digitsDifference = num_array1[position] - num_array2[position]

        if minusOneNext:
            digitsDifference -= 1
            minusOneNext = False

        if position == 0:
            if digitsDifference > 0:
                finalNumber = [digitsDifference] + finalNumber

            # elif digitsDifference < 0:
            #     finalNumber = [digitsDifference + 10] + finalNumber
            #     finalNumber = [1] + finalNumber

            elif digitsDifference == 0 and finalNumber[position] == '.':
                finalNumber = [0] + finalNumber

            break

        if digitsDifference >= 0:
            finalNumber = [digitsDifference] + finalNumber

        elif digitsDifference < 0:
            finalNumber = [digitsDifference + 10] + finalNumber
            minusOneNext = True

        position -= 1

    if finalMinus:
        finalNumber = ['-'] + finalNumber

    return finalNumber


# Засунуть в функцию добавление нулей слева и справа

# print(minus(['-', 5, '.', 0], ['-', 3, '.', 0]))