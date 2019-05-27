from jnius import autoclass
import classes.intvar as i

class Model(object):

    def __init__(self, name):
        Mod = autoclass('org.chocosolver.solver.Model')
        self.model = Mod(name)
    
    def getName(self):
        return self.model.getName()

    def intVar(self, name, lb, ub):
        return i.__init__(self, name, lb, ub)
        