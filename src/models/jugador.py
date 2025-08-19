class Jugador:
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo
        self.movimientos_realizados = 0
        self.movimientos = []
    
    def hacer_movimiento(self, fil, col):
        self.movimientos_realizados += 1
        self.movimientos.append((fil, col))
        return fil, col
    
    def cambiar_simbolo(self, nuevo_simbolo):
        self.simbolo = nuevo_simbolo
    
    @staticmethod
    def pedir_nombre(numero_jugador, simbolo):
        """Pide el nombre del jugador al usuario"""
        nombre = input(f"Ingrese el nombre del jugador {numero_jugador} ({simbolo}): ").strip()
        
        if not nombre:
            nombre = f"Jugador {numero_jugador}"
        return nombre