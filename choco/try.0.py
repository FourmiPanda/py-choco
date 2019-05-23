#!/usr/bin/env python

from jnius import autoclass

# EXAMPLE - java.util.Stack

# Stack = autoclass('java.util.Stack')
# stack = Stack()
# stack.push('world')
# stack.push('hello')

# print(stack.pop()) # --> 'world'
# print(stack.pop()) # --> 'hello

# MODEL
Model = autoclass('org.chocosolver.solver.Model')
model = Model('Mon tout premier modele')
# print(model.getName())

# INTVAR
IntVar = autoclass('org.chocosolver.solver.variables.IntVar')
x = model.intVar("X", 0, 5)
# print(x.getRange())

# Array = autoclass('java.lang.reflect.Array')
# array = Array().newInstance(3)
y = model.intVar("Y", 1, 8)

# CONSTRAINT
model.arithm(x, "+", y, "<", 5).post()
model.times(x, y, 4).post()

# SOLVER
model.getSolver().solve()

# PRINT THE SOLUTION
print(x.getValue())
print(y.getValue())

