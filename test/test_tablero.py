import unittest
from src.models.tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.tablero = Tablero()
    
    def test_tablero_inicializa_vacio(self):
        """El tablero debe empezar vacío"""
        for fila in self.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, "")
    
    def test_tablero_es_3x3(self):
        """El tablero debe ser de 3x3"""
        self.assertEqual(len(self.tablero.contenedor), 3)
        for fila in self.tablero.contenedor:
            self.assertEqual(len(fila), 3)
    
    def test_poner_ficha_en_casilla_vacia(self):
        """Debe poner ficha en casilla vacía"""
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")
    
    def test_poner_ficha_en_otra_posicion(self):
        """Debe poner ficha en cualquier posición válida"""
        self.tablero.poner_la_ficha(1, 2, "O")
        self.assertEqual(self.tablero.contenedor[1][2], "O")
    
    def test_no_puede_ocupar_casilla_ocupada(self):
        """No puede poner ficha donde ya hay una"""
        self.tablero.poner_la_ficha(0, 0, "X")
        
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(0, 0, "O")
    
    def test_puede_poner_x_y_o(self):
        """Puede poner tanto X como O"""
        self.tablero.poner_la_ficha(0, 0, "X")
        self.tablero.poner_la_ficha(0, 1, "O")
        
        self.assertEqual(self.tablero.contenedor[0][0], "X")
        self.assertEqual(self.tablero.contenedor[0][1], "O")


if __name__ == '__main__':
    unittest.main()