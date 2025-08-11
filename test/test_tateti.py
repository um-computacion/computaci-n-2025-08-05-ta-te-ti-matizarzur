import unittest
from src.models.tateti import Tateti
from src.models.tablero import PosOcupadaException

class TestTateti(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.juego = Tateti()
    
    def test_juego_empieza_con_turno_x(self):
        """El juego debe empezar con turno X"""
        self.assertEqual(self.juego.turno, "X")
    
    def test_ocupar_casilla_cambia_turno_correctamente(self):
        """Debe cambiar X -> O -> X (no X -> 0)"""
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, "O")  
        
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.assertEqual(self.juego.turno, "X")
    
    def test_pone_ficha_del_turno_actual(self):
        """Debe poner la ficha correcta"""
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")
        
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.assertEqual(self.juego.tablero.contenedor[0][1], "O")
    
    def test_detectar_ganador_fila_horizontal(self):
        """Debe detectar ganador en fila horizontal"""
        # X gana en primera fila
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(1, 0)  
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "X")
    
    def test_detectar_ganador_columna_vertical(self):
        """Debe detectar ganador en columna"""
        # O gana en primera columna
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 0) 
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        self.juego.ocupar_una_de_las_casillas(2, 0)  
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "O")
    
    def test_detectar_ganador_diagonal_principal(self):
        """Debe detectar ganador en diagonal principal"""
        # X gana en diagonal
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        self.juego.ocupar_una_de_las_casillas(2, 2)  
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "X")
    
    def test_sin_ganador_al_inicio(self):
        """No debe haber ganador al inicio"""
        self.assertFalse(self.juego.hay_ganador())
        self.assertIsNone(self.juego.obtener_ganador())
    
    def test_detectar_empate(self):
        """Debe detectar empate cuando se llena sin ganador"""

        movimientos = [
            (0, 0), (0, 1), (0, 2),  
            (1, 1), (1, 0), (1, 2),  
            (2, 1), (2, 0), (2, 2)         
        ]
        
        for fil, col in movimientos:
            self.juego.ocupar_una_de_las_casillas(fil, col)
        
        self.assertTrue(self.juego.es_empate())

if __name__ == '__main__':
    unittest.main()