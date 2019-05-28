#!/usr/bin/env python

from jnius import autoclass
import classes.model as m
import classes.intvar as i

# MODEL
model = m.Model('Mon tout premier modele')

# INTVAR

x = i.IntVar("X", 0, 5)
y = i.IntVar("Y", 1, 8)
print(x.getValue)
print(y)
"""
# CONSTRAINT
model.arithm(x, "+", y, "<", 5).post()
model.times(x, y, 4).post()

# SOLVER
model.getSolver().solve()

# PRINT THE SOLUTION
print(x.getValue())
print(y.getValue())

"""
