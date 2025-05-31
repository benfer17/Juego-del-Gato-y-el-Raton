# Juego-del-Gato-y-el-Raton
# 🐱🐭 Juego del Gato y el Ratón - Minimax

Un juego por turnos donde un jugador humano controla al ratón que debe llegar al queso, mientras una IA (usando el algoritmo Minimax) controla al gato que trata de atraparlo.

## 🎮 Cómo Jugar

1. El ratón (🐭) aparece en la fila inferior del tablero 8x6 en forma aleatoria en una de las casillas
2. El gato (🐱) comienza cerca del queso (🧀) en la fila superior 
3. El ratón se mueve con WASD + diagonales (Q,E,Z,C)
4. El gato usa Minimax para calcular el mejor movimiento
5. **Victoria del ratón**: Llegar al queso o sobrevivir 15 turnos
6. **Victoria del gato**: Atrapar al ratón

## ✅ Qué Funcionó

- **Algoritmo Minimax**: La IA es desafiante pero no imposible de vencer
- **Interfaz visual**: Los emojis hacen el juego claro y divertido
- **Controles intuitivos**: WASD + diagonales son familiares para gamers
- **Balance del juego**: Con 15 turnos y profundidad 3, el juego es justo
- **Función de evaluación**: La distancia Manhattan + casos extremos funciona bien

## 💥 Qué Fue un Desastre
- **Las endentanciones, hasta el ultimo momento
- **Primera función de evaluación**: Solo consideraba si el gato atrapaba al ratón, hacía que la IA fuera pasiva
- **Manejo de coordenadas**: Confundí filas/columnas varias veces, causando bugs extraños
- **El gato siempre ganaba**: Al tener los mismos movimientos en un tablero reducido
- **Validación de entrada**: No manejaba bien las teclas inválidas al principio
- **Debugging del Minimax**: Era difícil visualizar qué estaba "pensando" la IA

## 🔥 Mi Mejor "¡Ajá!" Durante el Proceso

**El momento eureka** fue cuando entendí que **la función de evaluación ES el alma del juego**.

Inicialmente pensé: *"Minimax es lo complicado, la evaluación es solo un detalle"*

Pero cuando cambié de:
```python
# Version ingenua
return 1 if gato_cerca_raton else 0
```

A:
```python
# Version inteligente  
return 10 - distancia_manhattan
```

¡El gato pasó de ser un zombie que vagaba sin rumbo a un depredador inteligente que acorralaba al ratón estratégicamente!

**La lección**: Un algoritmo sofisticado sin una buena heurística es como un Ferrari sin gasolina. La función de evaluación le da "personalidad" y estrategia a la IA.

## 🛠️ Tecnologías Utilizadas

- **Python 3**: Lenguaje principal
- **Algoritmo Minimax**: para el gato (profundidad 3)
- **Distancia Manhattan**: Heurística de evaluación
- **Emojis**: Interfaz visual en terminal


## 🚀 Posibles Mejoras

- Poda Alfa-Beta para mejor performance
- Diferentes niveles de dificultad
- Interfaz gráfica con Pygame
- Múltiples gatos
- Obstáculos en el tablero
- Tablero mas amplio o que se desarrolle en un tablero de ajedrez
_ Opción para volver a jugar
