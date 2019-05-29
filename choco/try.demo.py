import core.model as m

my_model = m.Model('simple problem')

x = my_model.intVar('X', 0, 4)
y = my_model.intVar('Y', 1, 8)
my_model.arithm(x, '+', y, '<', 5).times(x, y, 9999)
my_model.solve()
my_model.printStatistics()

print('X -> ' + str(x.getValue()))
print('Y -> ' + str(y.getValue()))