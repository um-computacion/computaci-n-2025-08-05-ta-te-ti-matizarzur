from src.models.tateti import Tateti

def main():
    print("Bienvenidos al Tateti!")
    print("-" * 30)
    
    juego = Tateti(pedir_nombres=True)
    
    print(f"\n{juego.get_nombre_turno_actual()} (X) vs {juego.jugadores['O']} (O)")
        
    while True:
        print("Tablero actual:")
        juego.tablero.mostrar()
        
        nombre_actual = juego.get_nombre_turno_actual()
        simbolo_actual = juego.turno
        print(f"Turno de: {nombre_actual} ({simbolo_actual})")
                
        if juego.hay_ganador():
            print(f"Gano: {juego.obtener_ganador()}! 🎉")
            break
                    
        if juego.es_empate():
            print("Empate")
            break
                
        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese col (0-2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
            print()  
        except Exception as e:
            print(f"Error: {e}")
            print()

if __name__ == '__main__':
    main()