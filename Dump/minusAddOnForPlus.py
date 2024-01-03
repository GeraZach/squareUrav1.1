def minus(num_array1, num_array2):


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
    finalMinus = False
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


# Дописать связанность плюса и минуса при разных знаках
# Засунуть в функцию добавление нулей слева и справа

