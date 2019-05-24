# -*- coding: utf-8 -*-

from .context import classes

import unittest


class BasicTestModel(unittest.TestCase):
    """Basic test cases for Model class"""

    def test_model_name(self):
        my_model = classes.Model('test')
        self.assertEqual('my model', my_model.getName())


if __name__ == '__main__':
    unittest.main()