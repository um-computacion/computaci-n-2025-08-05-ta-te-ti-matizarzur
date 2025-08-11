import unittest
from src.models.tablero import Tablero, PosOcupadaException

class TestExcepcion(unittest.TestCase):
    
    def test_excepcion_tiene_mensaje(self):
        """La excepción debe mostrar el mensaje correcto"""
        tablero = Tablero()
        tablero.poner_la_ficha(0, 0, "X")
        
        try:
            tablero.poner_la_ficha(0, 0, "O")
            self.fail("Debería haber lanzado excepción")
        except PosOcupadaException as e:
            self.assertEqual(str(e), "pos ocupada!")

if __name__ == '__main__':
    unittest.main()