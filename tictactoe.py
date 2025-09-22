"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

<<<<<<< HEAD
=======
"""Tic Tac Toe  
 Exercises  
 1. Give the X and O a different color and width.  
 2. What happens when someone taps a taken spot?  
 3. How would you detect when someone has won?  
 4. How could you create a computer player?  
"""

>>>>>>> A01770834
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
<<<<<<< HEAD
    color('red')  #Cambié color a rojo
    pensize(5)    #Engrosar el trazo para mejor visibilidad
    offset = 20   #Offset para centrar el símbolo dentro del cuadro
=======
    color('red')  # Cambié color a rojo
    pensize(5)    # Engrosar el trazo para mejor visibilidad
    offset = 20   # Offset para centrar el símbolo dentro del cuadro
>>>>>>> A01770834

    # Líneas ajustadas para que la X quede centrada
    line(x + offset, y + offset, x + 133 - offset, y + 133 - offset)
    line(x + offset, y + 133 - offset, x + 133 - offset, y + offset)


def drawo(x, y):
    """Draw O player centered, bigger and blue."""
    color('blue')  # Cambié color a azul
<<<<<<< HEAD
    pensize(5)     #Engrosar el trazo
    up()
    #Ajustar posición inicial para centrar el círculo en la casilla
    goto(x + 133/2, y + 20)
    down()
    circle(46)  #Cambié el radio del círculo para que quede centrado y más grande
=======
    pensize(5)     # Engrosar el trazo
    up()
    # Ajustar posición inicial para centrar el círculo en la casilla
    goto(x + 133/2, y + 20)
    down()
    circle(46)  # Cambié el radio del círculo para que quede centrado y más grande
>>>>>>> A01770834


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


# ----------------- NUEVO CÓDIGO AGREGADO -----------------

# Creamos una estructura para almacenar casillas ocupadas
occupied = {}

def is_occupied(x, y):
    """Revisar si la casilla ya está ocupada."""
    return (x, y) in occupied

def mark_occupied(x, y, player):
    """Marcar una casilla como ocupada por un jugador."""
    occupied[(x, y)] = player
# ---------------------------------------------------------


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    #  Validación agregada
    if is_occupied(x, y):
        print("️ Casilla ocupada, intenta en otra.")  # Solo mensaje en consola
        return

    player = state['player']
    draw = players[player]
    draw(x, y)

    # Marcar casilla ocupada
    mark_occupied(x, y, player)

    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
<<<<<<< HEAD
done()
=======
done()

>>>>>>> A01770834
