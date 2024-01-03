class Bigfloat:

    def __init__(self, coefficient_str):
        self.number = coefficient_str

        self.wholeAndFraction = self.number.split('.')

        self.whole = int(self.wholeAndFraction[0])
        self.fraction = int(self.wholeAndFraction[1])

    def __add__(self, other):
        return Bigfloat(self.whole + other)


a = Bigfloat('2.5')
a = a + 2
print(a.whole, a.fraction)