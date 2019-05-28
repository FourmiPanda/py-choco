from jnius import autoclass

from . import intvar

class Model(object):


    def getName(self):
        return self.model.getName()

    def intVar(self, name, lb, ub):
        return self.model.intVar(name, lb, ub)

    def intVarl(self, name, l):
        return self.model.intVar(name,l)
        """
        liste=[]
        for i in range(0,l.len-1):
            liste[i]=self.model.intVar(name, l[i], l[i])
        return liste
        """

    def arithm(self, var1, op1, var2, op2, cste):
        self.model.arithm(var1, op1, var2, op2, cste).post()

    def times(self, var1, var2, equ):
        self.model.times(var1, var2, equ).post()

    def solve(self):
        self.model.getSolver().solve()

    def __init__(self, name):
        Mod = autoclass('org.chocosolver.solver.Model')
        self.model = Mod(name)

    def boolVar(self, name,val):
        if val==True:
            return self.model.intVar(name,1,1)
        elif val==False:
            return self.model.intVar(name,0,0)
        else:
            raise SyntaxError ("boolean expected")