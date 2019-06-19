# -*- coding: utf-8 -*-

from context import core

# from pytest import fixture
# import unittest

# @fixture
# def op():
#     pass

# class BasicTestModel(unittest.TestCase):
#     """Basic tests cases for Model class"""

def test_model_name(self):
    my_model = core.model.Model('model name')
    # self.assertEqual('model name', my_model.getName())
    assert 'model name' == my_model.getName()

def test_model_simple_problem(self):
    my_model = core.model.Model('simple problem')
    x = my_model.intVar('X', 0, 4)
    y = my_model.intVar('Y', 1, 8)
    my_model.arithm(x, '+', y, '<', 5).times(x, y, 4)
    my_model.solve()
    # self.assertEquals((2, 2), (x.getValue(), y.getValue()))
    assert (2, 2) == (x.getValue(), y.getValue())

def test_model_bool_error(self):
    my_model = core.model.Model('bool problem')
    raised = False
    try:
        z=my_model.boolVar('z',3)
    except SyntaxError:
            # A syntax error was generated during the affectation...
        raised = True
    # self.assert_(raised, "'boolean expected' failed to raise a SyntaxError.")
    assert raised == "'boolean expected' failed to raise a SyntaxError."


# if __name__ == '__main__':
#     pytest.main()