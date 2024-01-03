import time
start_time = time.time()

def long_multiply(number1, number2):
    dot_placement = number1.index('.') + number2.index('.')  #Проверить надо их ихмнять или нет
    number1.replace('.', '')
    number2.replace('.', '')




print("--- %s seconds ---" % (time.time() - start_time))