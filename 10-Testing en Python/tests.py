import unittest
from funciones import calcula_media

class TestCalculaMedia(unittest.TestCase):
    def test_1(self):
        # Prueba con valores iguales
        resultado = calcula_media([10, 10, 10])
        self.assertEqual(resultado, 10)

    def test_2(self):
        # Prueba con valores variables
        resultado = calcula_media([5, 3, 4])
        self.assertEqual(resultado, 4)

if __name__ == '__main__':
    unittest.main()