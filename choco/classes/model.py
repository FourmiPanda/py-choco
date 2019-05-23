from jnius import autoclass

class Model(object):

    def __init__(self, name):
        Mod = autoclass('org.chocosolver.solver.Model')
        self.model = Mod(name)
    
    def getName(self):
        return self.model.getName()


        