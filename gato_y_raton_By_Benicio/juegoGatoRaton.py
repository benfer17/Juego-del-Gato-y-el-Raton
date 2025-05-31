import random

# Estado inicial del juego
estado_juego = {
    "raton": (7, random.choice([1, 2, 3, 4])),
    "gato": (1, 2),
    "turno": 1,
    "turnos_maximos": 15
}

def imprimir_tablero():
    """Imprime el tablero 8x6 con ratón 🐭, gato 🐱 y queso 🧀"""
    tablero = [
        ["🔳", "🧀", "🧀", "🧀", "🧀", "🔳"],  
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],  
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],  
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],  
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],  
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],  
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],  
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳"]   
    ]

    fila_gato, columna_gato = estado_juego["gato"]
    fila_raton, columna_raton = estado_juego["raton"]

    # Colocar las piezas en el tablero
    if (fila_gato, columna_gato) == (fila_raton, columna_raton):
        tablero[fila_gato][columna_gato] = "🐱"  # Si están en la misma posición, solo mostrar gato
    else:
        tablero[fila_gato][columna_gato] = "🐱"
        tablero[fila_raton][columna_raton] = "🐭"

    # Imprimir el tablero
    for fila in tablero:
        print("".join(fila))
    print()

def mover_raton():
    """El jugador mueve al ratón con el teclado"""
    movimientos = {
        "w": (-1, 0),   # arriba
        "s": (1, 0),    # abajo
        "a": (0, -1),   # izquierda
        "d": (0, 1),    # derecha
        "q": (-1, -1),  # diagonal arriba-izquierda
        "e": (-1, 1),   # diagonal arriba-derecha
        "z": (1, -1),   # diagonal abajo-izquierda
        "c": (1, 1),    # diagonal abajo-derecha
    }

    print("Controles: w(arriba) s(abajo) a(izq) d(der) + diagonales q,e,z,c")
    
    while True:
        tecla = input("¿Cómo quieres mover al ratón? ").lower().strip()

        if tecla in movimientos:
            fila_actual, columna_actual = estado_juego["raton"]
            cambio_fila, cambio_columna = movimientos[tecla]
            nueva_fila = fila_actual + cambio_fila
            nueva_columna = columna_actual + cambio_columna

            # Verificar que la nueva posición esté dentro del tablero
            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 6:
                estado_juego["raton"] = (nueva_fila, nueva_columna)
                return  # Salir de la función inmediatamente
            else:
                print("❌ No puedes salir del tablero! Intenta otro movimiento.")
        else:
            print("❌ Tecla inválida. Usa w, a, s, d, q, e, z, c")

def evaluar_posicion(posicion_gato, posicion_raton):
    """Evalúa qué tan buena es una posición para el Gato"""
    # Si el gato atrapa al ratón
    if posicion_gato == posicion_raton:
        return 100
    
    # Si el ratón llegó al queso
    if posicion_raton[0] == 0 and posicion_raton[1] in [1, 2, 3, 4]:
        return -100
    
    # Calcular distancia Manhattan entre gato y ratón
    distancia = abs(posicion_gato[0] - posicion_raton[0]) + abs(posicion_gato[1] - posicion_raton[1])
    
    # Mientras más cerca esté el gato del ratón, mejor para el gato
    return 10 - distancia

def obtener_movimientos_gato(posicion_gato):
    """Obtiene todos los movimientos válidos del gato (4 direcciones)"""
    movimientos = []
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, derecha

    for cambio_fila, cambio_columna in direcciones:
        nueva_fila = posicion_gato[0] + cambio_fila
        nueva_columna = posicion_gato[1] + cambio_columna

        if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 6:
            movimientos.append((nueva_fila, nueva_columna))

    return movimientos

def obtener_movimientos_raton(posicion_raton):
    """Obtiene todos los movimientos válidos del ratón (8 direcciones)"""
    movimientos = []
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1),  # básicas
                   (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonales
    
    for cambio_fila, cambio_columna in direcciones:
        nueva_fila = posicion_raton[0] + cambio_fila
        nueva_columna = posicion_raton[1] + cambio_columna

        if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 6:
            movimientos.append((nueva_fila, nueva_columna))

    return movimientos

def minimax(posicion_gato, posicion_raton, profundidad, turno_gato):
    """Algoritmo Minimax para el gato"""
    # Caso base: profundidad 0 o juego terminado
    if profundidad == 0 or posicion_gato == posicion_raton or (posicion_raton[0] == 0 and posicion_raton[1] in [1, 2, 3, 4]):
        return evaluar_posicion(posicion_gato, posicion_raton), None
    
    if turno_gato:
        # Turno del gato: maximizar puntaje
        mejor_puntaje = -999
        mejor_movimiento = None

        for movimiento in obtener_movimientos_gato(posicion_gato):
            puntaje, _ = minimax(movimiento, posicion_raton, profundidad - 1, False)
            
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movimiento

        return mejor_puntaje, mejor_movimiento
    
    else:
        # Turno del ratón: minimizar puntaje
        mejor_puntaje = 999
        mejor_movimiento = None

        for movimiento in obtener_movimientos_raton(posicion_raton):
            puntaje, _ = minimax(posicion_gato, movimiento, profundidad - 1, True)
            
            if puntaje < mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movimiento

        return mejor_puntaje, mejor_movimiento

def mover_gato_con_minimax():
    """El gato usa Minimax para decidir su mejor movimiento"""
    posicion_gato = estado_juego["gato"]
    posicion_raton = estado_juego["raton"]

    _, mejor_movimiento = minimax(posicion_gato, posicion_raton, 3, True)

    if mejor_movimiento:
        estado_juego["gato"] = mejor_movimiento
        

def verificar_ganador():
    """Revisa si alguien ganó el juego"""
    raton = estado_juego["raton"]
    gato = estado_juego["gato"]

    # ¿El gato atrapó al ratón?
    if raton == gato:
        print("🐱 ¡EL GATO GANÓ! Atrapó al ratón.")
        return True
    
    # ¿El ratón llegó al queso?
    elif raton[0] == 0 and raton[1] in [1, 2, 3, 4]:
        print("🐭 ¡EL RATÓN GANÓ! Llegó al queso.")
        return True
    
    # ¿Se acabaron los turnos?
    elif estado_juego["turno"] > estado_juego["turnos_maximos"]:
        print("⏰ ¡SE ACABÓ EL TIEMPO! El ratón sobrevivió.")
        return True
    
    return False

# === JUEGO PRINCIPAL ===
def main():
    print("🎮 ¡BIENVENIDO AL JUEGO DEL GATO Y EL RATÓN! 🎮")
    print("📍 Objetivo: El ratón debe llegar al queso 🧀 sin ser atrapado")
    print("El gato usa un Algoritmo Informatico para atraparte")
    print(f"⏰ Tienes {estado_juego['turnos_maximos']} turnos para lograrlo\n")

    # Bucle principal del juego
    while True:
        print(f"=== TURNO {estado_juego['turno']} ===")
        imprimir_tablero()

        # Turno del ratón
        print("🐭 Tu turno:")
        mover_raton()

        # ¿Ganó alguien después del movimiento del ratón?
        if verificar_ganador():
            print("\n" + "="*30)
            imprimir_tablero()
            break
        
        # Turno del gato
        print("\n🐱 Turno del gato...")
        mover_gato_con_minimax()

        # ¿Ganó alguien después del movimiento del gato?
        if verificar_ganador():
            print("\n" + "="*30)
            imprimir_tablero()
            break

        # Siguiente turno
        estado_juego["turno"] += 1
        print("-" * 40)

    print("🎮 ¡JUEGO TERMINADO! ¡Gracias por jugar!")

if __name__ == "__main__":
    main()