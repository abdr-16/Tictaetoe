"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *
from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player centered, bigger and red."""
    color('red')  # Cambié color a rojo
    pensize(5)    # Engrosar el trazo para mejor visibilidad
    offset = 20   # Offset para centrar el símbolo dentro del cuadro

    # Líneas ajustadas para que la X quede centrada
    line(x + offset, y + offset, x + 133 - offset, y + 133 - offset)
    line(x + offset, y + 133 - offset, x + 133 - offset, y + offset)


def drawo(x, y):
    """Draw O player centered, bigger and blue."""
    color('blue')  # Cambié color a azul
    pensize(5)     # Engrosar el trazo
    up()
    # Ajustar posición inicial para centrar el círculo en la casilla
    goto(x + 133/2, y + 20)
    down()
    circle(46)  # Cambié el radio del círculo para que quede centrado y más grande


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]

# ===================== AGREGADO: detección de fin de juego =====================
# Tablero lógico 3x3: None (vacío), 0 (X), 1 (O)
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Turtle para mostrar mensajes de fin de juego
writer = Turtle(visible=False)
writer.up()
writer.goto(0, 185)
writer.color('black')

def rc_from_xy(x, y):
    """AGREGADO: convertir coordenadas (x,y) 'floor' a índices fila/col 0..2."""
    c = int((x + 200) // 133)  # columna
    r = int((y + 200) // 133)  # fila
    return r, c

def check_winner():
    """AGREGADO: devuelve 0 si gana X, 1 si gana O, None si no hay ganador."""
    lines = []
    # Filas y columnas
    for i in range(3):
        lines.append(board[i])  # fila i
        lines.append([board[0][i], board[1][i], board[2][i]])  # columna i
    # Diagonales
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for p in (0, 1):
        if any(all(cell == p for cell in line) for line in lines):
            return p
    return None

def board_full():
    """AGREGADO: True si el tablero está completo (empate)."""
    return all(cell is not None for row in board for cell in row)

# Estado extra para saber si el juego terminó
state['game_over'] = False
# =================== FIN AGREGADO: detección de fin de juego ===================


def tap(x, y):
    """Draw X or O in tapped square."""
    # AGREGADO: ignorar taps si el juego ya terminó
    if state.get('game_over'):
        return

    x = floor(x)
    y = floor(y)

    # AGREGADO: obtener índices en el tablero lógico
    r, c = rc_from_xy(x, y)

    player = state['player']
    draw = players[player]
    draw(x, y)
    update()

    # AGREGADO: registrar jugada y verificar estado del juego
    board[r][c] = player

    winner = check_winner()
    if winner is not None:
        writer.clear()
        writer.write(f"¡Ganó {'X' if winner == 0 else 'O'}!", align="center",
                     font=("Arial", 18, "bold"))
        state['game_over'] = True
        onscreenclick(None)  # opcional: desactivar más clics al terminar
        return

    if board_full():
        writer.clear()
        writer.write("¡Empate!", align="center", font=("Arial", 18, "bold"))
        state['game_over'] = True
        onscreenclick(None)
        return

    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()

