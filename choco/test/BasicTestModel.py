# -*- coding: utf-8 -*-

from .context import core

import unittest


class BasicTestModel(unittest.TestCase):
    """Basic test cases for Model class"""

    def test_model_name(self):
        my_model = core.model.Model('model name')
        self.assertEqual('model name', my_model.getName())

    def test_model_simple_problem(self):
        my_model = core.model.Model('simple problem')
        x = my_model.intVar('X', 0, 4)
        y = my_model.intVar('Y', 1, 8)
        my_model.arithm(x, '+', y, '<', 5)
        my_model.times(x, y, 4)
        my_model.solve()
        self.assertEquals('simple problem', 'simple problem')


if __name__ == '__main__':
    unittest.main()