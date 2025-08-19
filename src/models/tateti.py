from src.models.tablero import Tablero
from src.models.jugador import Jugador

class Tateti:
    def __init__(self, pedir_nombres=True):
        self.tablero = Tablero()
        
        if pedir_nombres:
            
            nombre_x = Jugador.pedir_nombre(1, "X")
            nombre_o = Jugador.pedir_nombre(2, "O")
        else:
            
            nombre_x = "Jugador 1"
            nombre_o = "Jugador 2"
        
        self.jugadores = {
            "X": nombre_x,
            "O": nombre_o
        }
        
        self.turno = "X"  
        self.ganador = None

    def get_nombre_turno_actual(self):
        """Devuelve el nombre del jugador del turno actual"""
        return self.jugadores[self.turno]
    
    def get_nombre_ganador(self):
        """Devuelve el nombre del ganador"""
        if self.ganador:
            return self.jugadores[self.ganador]
        return None

    def ocupar_una_de_las_casillas(self, fil, col):
        # pongo la ficha...
        self.tablero.poner_la_ficha(fil, col, self.turno)
        
        if self.turno == "X":
            self.turno = "O"  
        else:
            self.turno = "X"

    def hay_ganador(self):
        """Verifica si hay un ganador en el juego"""

        for fila in self.tablero.contenedor:
            if fila[0] == fila[1] == fila[2] and fila[0] != "":
                self.ganador = fila[0]
                return True
        

        for col in range(3):
            if (self.tablero.contenedor[0][col] == 
                self.tablero.contenedor[1][col] == 
                self.tablero.contenedor[2][col] and 
                self.tablero.contenedor[0][col] != ""):
                self.ganador = self.tablero.contenedor[0][col]
                return True
        

        if (self.tablero.contenedor[0][0] == 
            self.tablero.contenedor[1][1] == 
            self.tablero.contenedor[2][2] and 
            self.tablero.contenedor[0][0] != ""):
            self.ganador = self.tablero.contenedor[0][0]
            return True
        

        if (self.tablero.contenedor[0][2] == 
            self.tablero.contenedor[1][1] == 
            self.tablero.contenedor[2][0] and 
            self.tablero.contenedor[0][2] != ""):
            self.ganador = self.tablero.contenedor[0][2]
            return True
        
        return False

    def obtener_ganador(self):
        """Devuelve el nombre del ganador del juego o None si no hay ganador"""
        if self.hay_ganador():
            return self.get_nombre_ganador()
        return None

    def es_empate(self):
        """Verifica si el juego está en empate"""
        
        if not self.hay_ganador():
            for fila in self.tablero.contenedor:
                for casilla in fila:
                    if casilla == "":
                        return False
            return True
        return False