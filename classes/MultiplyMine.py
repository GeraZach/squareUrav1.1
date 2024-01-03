def multiply(num1,num2):

    biggerNumber = []
    lesserNumber = []

    if len(num1) >= len(num2):
        biggerNumber = num1
        lesserNumber = num2

    else:
        biggerNumber = num2
        lesserNumber = num1

    toSum