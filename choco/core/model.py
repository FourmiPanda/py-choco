from jnius import autoclass

from . import intvar

class Model(object):


    def getName(self):
        return self.model.getName()

    def intVar(self, name, lb, ub):
        return self.model.intVar(name, lb, ub)

    def arithm(self, var1, op1, var2, op2, cste):
        self.model.arithm(var1, op1, var2, op2, cste).post()
        return self

    def times(self, var1, var2, equ):
        self.model.times(var1, var2, equ).post()
        return self

    def solve(self):
        self.model.getSolver().solve()

    def __init__(self, name):
        Mod = autoclass('org.chocosolver.solver.Model')
        self.model = Mod(name)
