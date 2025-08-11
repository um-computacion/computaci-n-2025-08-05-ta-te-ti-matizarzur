from src.models.tateti import Tateti

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    
    while True:
        print("Tablero: ")
        print(juego.tablero.contenedor)
        print("Turno: ")
        print(juego.turno)
        
        if juego.hay_ganador():
            print(f"GANADOR: {juego.obtener_ganador()}!")
            break
            
        if juego.es_empate():
            print("EMPATE!")
            break
        
        try:
            fil = int(input("Ingrese fila: "))
            col = int(input("Ingrese col: "))
            juego.ocupar_una_de_las_casillas(fil, col)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
