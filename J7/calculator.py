
class Algebra:
    def determinan(self, mat):
        pass



class Calculator:
    def __init__(self):
        self.memo = None
        self.oper = ['+', '-']

    def summ(self, a, b):
        self.memo = a + b
        return self.memo

    def subtr(self, a, b):
        self.memo = a - b
        return self.memo
