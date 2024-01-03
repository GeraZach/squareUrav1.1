from typesAndIsNegativeForDump import  *

# В 10 раз быстрее длинной арифметики, но багованая

def complex_sum(num1, num2, type1, type2):

    if type1 == 'complex' and type2 == 'complex':

        # Нужна проверка на знаки

        tokens1 = num1.split()
        tokens2 = num2.split()

        float1 = tokens1[0]
        # !!! TEST
        imag1 = tokens1[2].strip('i')

        float2 = tokens2[0]
        # !!! test
        imag2 = tokens2[2].strip('i')

        finalFloat = float_sum(float1,float2)
        finalImag = float_sum(imag1, imag2) + 'i'

        finalFComplex = f"{finalFloat} + {finalImag}"

    return finalFComplex

#дописать сверху

def float_sum(num1, num2):
    whole1, frac1 = num1.split('.')
    whole2, frac2 = num2.split('.')

    MaxFracLen = max(len(frac1), len(frac2))

    # Test обе дробные части начинаются с нуля

    flag = False

    if frac2[0] == '0' and frac1[0] == '0':
        minLenZeroesBegin = min(len(str(int(frac1))), len(str(int(frac2))))
        flag = True



    if len(frac1) < len(frac2):
        frac1 += '0' * (MaxFracLen - len(frac1))
    else:
        frac2 += '0' * (MaxFracLen - len(frac2))

    frac1 = int(frac1)
    frac2 = int(frac2)
    whole1 = int(whole1)
    whole2 = int(whole2)

    finalWhole = whole1 + whole2
    finalFrac = frac1 + frac2

    # Test for zeroes in the begin bug
    if flag:
        finalFrac = '0' * minLenZeroesBegin + str(finalFrac)

    if len(str(finalFrac)) > MaxFracLen:
        finalWhole += 1
        finalFrac = str(finalFrac)[1:]



    finalFloat = f"{finalWhole}.{finalFrac}"

# Мб стоит возвращать целую и дробную часть! !!!!!!

    return finalFloat


def sum_function(str_num1, str_num2):

    type1, type2 = get_types(str_num1, str_num2)

    if type1 == 'complex' or type2 == 'complex':
        finalSum = complex_sum(str_num1, str_num2, type1, type2)

    if type1 == 'float' and type2 == 'float':
        finalSum = float_sum(str_num1, str_num2)

    return finalSum


import time
start_time = time.time()



print(sum_function('324546576874534254365476571.000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807', '2354365476587675645343524635746857986753645345246357468579687586475364253411.5612343254635746857674563453435246357468576985674563453000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807000560123142354364758769878675645344352463574685796807'))

print("--- %s seconds ---" % (time.time() - start_time))

# Надо переписать переписать в длинную

# URGENT !!!! ТОЧНО надо убирать лишние нули  - 1.000500 + 1.05 !!!! - создает новый баг , надо попросить интерпретатор убрать их нахуй

#1.0000000005 1.0000000000005 - BUG

 # Bug 1.005 + 1.05 = !!! 2.55  -- FIXED


# Минус на минус наверн стоит вывести сюда, так же как и плюс на плюс, остальное в разность
# Надо продумать как это реализовать, т.к мы не знаем числа с каким знаком мы складываем и вычитаем, может быть сумма отриц, или разность отриц и т.д