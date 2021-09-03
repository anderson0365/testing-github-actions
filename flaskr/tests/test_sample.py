import unittest

__author__ = "Anderson Luis Cáceres Padilla"
__copyright__ = "Anderson Luis Cáceres Padilla"
__license__ = "mit"

class test_sample(unittest.TestCase):

    def test_validar_parametros(self):
        a = False
        self.assertFalse(a)