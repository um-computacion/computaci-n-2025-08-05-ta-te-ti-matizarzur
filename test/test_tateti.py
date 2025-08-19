import unittest
from src.models.tateti import Tateti
from src.models.tablero import PosOcupadaException

class TestTateti(unittest.TestCase):
    
    def setUp(self):
        self.juego = Tateti(pedir_nombres=False)
    
    def test_juego_empieza_con_turno_x(self):
        self.assertEqual(self.juego.turno, "X")
    
    def test_ocupar_casilla_cambia_turno_correctamente(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, "O")  
        
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.assertEqual(self.juego.turno, "X")
    
    def test_pone_ficha_del_turno_actual(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")
        
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.assertEqual(self.juego.tablero.contenedor[0][1], "O")
    
    def test_detectar_ganador_fila_horizontal(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(1, 0)  
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 1")
    
    def test_detectar_ganador_columna_vertical(self):
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 0) 
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        self.juego.ocupar_una_de_las_casillas(2, 0)  
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 2")
    
    def test_detectar_ganador_diagonal_principal(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        self.juego.ocupar_una_de_las_casillas(2, 2)  
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 1")
    
    def test_sin_ganador_al_inicio(self):
        self.assertFalse(self.juego.hay_ganador())
        self.assertIsNone(self.juego.obtener_ganador())
    
    def test_detectar_empate(self):
        movimientos = [
            (0, 0), (0, 1), (0, 2),  
            (1, 1), (1, 0), (1, 2),  
            (2, 1), (2, 0), (2, 2)         
        ]
        
        for fil, col in movimientos:
            self.juego.ocupar_una_de_las_casillas(fil, col)
        
        self.assertTrue(self.juego.es_empate())

    def test_detectar_ganador_segunda_fila(self):
        self.juego.ocupar_una_de_las_casillas(1, 0)
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(1, 2)
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 1")

    def test_detectar_ganador_tercera_fila(self):
        self.juego.ocupar_una_de_las_casillas(2, 0)
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(2, 1)
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(2, 2)
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 1")

    def test_detectar_ganador_segunda_columna(self):
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.juego.ocupar_una_de_las_casillas(1, 0)
        self.juego.ocupar_una_de_las_casillas(2, 1)
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 1")

    def test_detectar_ganador_tercera_columna(self):
        self.juego.ocupar_una_de_las_casillas(0, 2)
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(1, 2)
        self.juego.ocupar_una_de_las_casillas(1, 0)
        self.juego.ocupar_una_de_las_casillas(2, 2)
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 1")

    def test_detectar_ganador_diagonal_secundaria(self):
        self.juego.ocupar_una_de_las_casillas(0, 2)
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(2, 0)
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 1")

    def test_no_hay_empate_si_hay_ganador(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(1, 0)
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.juego.ocupar_una_de_las_casillas(0, 2)
        
        self.assertFalse(self.juego.es_empate())

    def test_no_hay_empate_con_tablero_parcial(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        
        self.assertFalse(self.juego.es_empate())

    def test_ganador_jugador_o(self):
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.juego.ocupar_una_de_las_casillas(1, 0)
        self.juego.ocupar_una_de_las_casillas(0, 2)
        self.juego.ocupar_una_de_las_casillas(2, 0)
        
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.obtener_ganador(), "Jugador 2")

    def test_ocupar_casilla_ocupada_lanza_excepcion(self):
        self.juego.ocupar_una_de_las_casillas(1, 1)
        
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(1, 1)

    def test_juego_continua_despues_de_excepcion(self):
        self.juego.ocupar_una_de_las_casillas(1, 1)
        
        try:
            self.juego.ocupar_una_de_las_casillas(1, 1)
        except PosOcupadaException:
            pass
        
        self.assertEqual(self.juego.turno, "O")
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, "X")

    def test_get_nombre_turno_actual(self):
        self.assertEqual(self.juego.get_nombre_turno_actual(), "Jugador 1")
        
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.get_nombre_turno_actual(), "Jugador 2")

if __name__ == '__main__':
    unittest.main()