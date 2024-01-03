from ArrPlus import *
from Interpreter import validate
from ArrMinus import *

class BigFloat:


    def __init__(self, str_num):

        if is_valid(str_num):
            self.container = to_container(str_num)

    def __add__(self, other):
        if self.data != 'INVALID_INPUT':
            return plus(self.data, other.data)
        else:
            return 'INVALID_INPUT: PLUS FUNC'

    def __sub__(self, other):
        if self.data != 'INVALID_INPUT':
            return minus(self.data, other.data)
        else:
            return "INVALID_INPUT: MINUS FUNC"


a = BigFloat(input())
b = BigFloat(input())
c = BigFloat(input())

print(a - b + c)

