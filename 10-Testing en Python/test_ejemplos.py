import unittest

class TestEjemplos(unittest.TestCase):
    
    def setUp(self):
        print("-> Entra setUp (Prepara el entorno)")

    def tearDown(self):
        print("-> Entra tearDown (Limpia el entorno)")

    def test_1(self):
        print("\nEjecutando Test: test_1")

    def test_2(self):
        print("\nEjecutando Test: test_2")

if __name__ == '__main__':
    unittest.main()