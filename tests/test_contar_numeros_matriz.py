import unittest
from contar_numeros_matriz import contar_numeros_matriz

class TestContarNumerosMatriz(unittest.TestCase):
    def test_ejemplo(self):
        self.assertEqual(contar_numeros_matriz([[2, 2], [2, 2]]), [0, 1])

    def test_ejemplo2(self):
        self.assertEqual(contar_numeros_matriz([[2, 1, 3], [4, 5, 2], [6, 6, 6]]), [4, 2])

if __name__ == '__main__':
    unittest.main()