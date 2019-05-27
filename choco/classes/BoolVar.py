from jnius import autoclass

class BoolVar:

    def __init__(self):
        boolean = autoclass('org.chocosolver.solver.variables.BoolVar')
