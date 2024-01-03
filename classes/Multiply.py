def multiply(num1, num2):

    # создаем массив для хранения промежуточных результатов
    results = [0] * (len(num1) + len(num2))

    # переворачиваем строки для удобства
    num1 = num1[::-1]
    num2 = num2[::-1]

    for i in range(len(num1)):
        for j in range(len(num2)):
            results[i + j] += num1[i] * num2[j]

    carry = 0
    for i in range(len(results)):
        results[i] += carry
        carry = results[i] // 10
        results[i] %= 10

    while len(results) > 1 and results[-1] == 0:
        results.pop()

    results = results[::-1]

    return results
