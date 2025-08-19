import unittest
from src.models.tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
    
    def test_tablero_inicializa_vacio(self):
        for fila in self.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, "")
    
    def test_tablero_es_3x3(self):
        self.assertEqual(len(self.tablero.contenedor), 3)
        for fila in self.tablero.contenedor:
            self.assertEqual(len(fila), 3)
    
    def test_poner_ficha_en_casilla_vacia(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")
    
    def test_poner_ficha_en_otra_posicion(self):
        self.tablero.poner_la_ficha(1, 2, "O")
        self.assertEqual(self.tablero.contenedor[1][2], "O")
    
    def test_no_puede_ocupar_casilla_ocupada(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(0, 0, "O")
    
    def test_puede_poner_x_y_o(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.tablero.poner_la_ficha(0, 1, "O")
        
        self.assertEqual(self.tablero.contenedor[0][0], "X")
        self.assertEqual(self.tablero.contenedor[0][1], "O")

    def test_poner_ficha_en_todas_las_posiciones(self):
        ficha = "X"
        for fila in range(3):
            for col in range(3):
                tablero = Tablero()
                tablero.poner_la_ficha(fila, col, ficha)
                self.assertEqual(tablero.contenedor[fila][col], ficha)

    def test_poner_diferentes_simbolos(self):
        simbolos = ["X", "O", "A", "1", "@", "♠"]
        posiciones = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
        
        for i, simbolo in enumerate(simbolos):
            fila, col = posiciones[i]
            self.tablero.poner_la_ficha(fila, col, simbolo)
            self.assertEqual(self.tablero.contenedor[fila][col], simbolo)

    def test_excepcion_tiene_mensaje_correcto(self):
        self.tablero.poner_la_ficha(1, 1, "X")
        
        with self.assertRaises(PosOcupadaException) as context:
            self.tablero.poner_la_ficha(1, 1, "O")
        
        self.assertEqual(str(context.exception), "pos ocupada!")

    def test_llenar_tablero_completo(self):
        fichas = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        
        for fila in range(3):
            for col in range(3):
                self.tablero.poner_la_ficha(fila, col, fichas[fila][col])
        
        self.assertEqual(self.tablero.contenedor, fichas)

    def test_tablero_vacio_todas_posiciones(self):
        for fila in range(3):
            for col in range(3):
                self.assertEqual(self.tablero.contenedor[fila][col], "")

    def test_poner_ficha_en_centro(self):
        self.tablero.poner_la_ficha(1, 1, "X")
        self.assertEqual(self.tablero.contenedor[1][1], "X")

    def test_poner_fichas_esquinas(self):
        esquinas = [(0, 0), (0, 2), (2, 0), (2, 2)]
        fichas = ["X", "O", "X", "O"]
        
        for i, (fila, col) in enumerate(esquinas):
            self.tablero.poner_la_ficha(fila, col, fichas[i])
            self.assertEqual(self.tablero.contenedor[fila][col], fichas[i])

    def test_poner_fichas_bordes(self):
        bordes = [(0, 1), (1, 0), (1, 2), (2, 1)]
        
        for fila, col in bordes:
            self.tablero.poner_la_ficha(fila, col, "X")
            self.assertEqual(self.tablero.contenedor[fila][col], "X")

    def test_excepcion_en_cualquier_posicion_ocupada(self):
        posiciones = [(0, 0), (1, 1), (2, 2)]
        
        for fila, col in posiciones:
            tablero = Tablero()
            tablero.poner_la_ficha(fila, col, "X")
            
            with self.assertRaises(PosOcupadaException):
                tablero.poner_la_ficha(fila, col, "O")

    def test_poner_mismo_simbolo_multiples_veces(self):
        posiciones = [(0, 0), (0, 1), (0, 2)]
        
        for fila, col in posiciones:
            self.tablero.poner_la_ficha(fila, col, "X")
            self.assertEqual(self.tablero.contenedor[fila][col], "X")

if __name__ == '__main__':
    unittest.main()