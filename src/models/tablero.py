class PosOcupadaException(Exception):
    ...


class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # ver si esta ocupado...
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")
    
    def mostrar(self):
        print("\n   0   1   2")
        print("  -----------")
        for i, fila in enumerate(self.contenedor):
            
            fila_visual = [celda if celda != "" else " " for celda in fila]
            print(f"{i} | {' | '.join(fila_visual)} |")
            if i < 2:  
                print("  |---|---|---|")
        print("  -----------\n")