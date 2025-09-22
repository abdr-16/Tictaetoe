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
    color('red')  #Cambié color a rojo
    pensize(5)    #Engrosar el trazo para mejor visibilidad
    offset = 20   #Offset para centrar el símbolo dentro del cuadro

    # Líneas ajustadas para que la X quede centrada
    line(x + offset, y + offset, x + 133 - offset, y + 133 - offset)
    line(x + offset, y + 133 - offset, x + 133 - offset, y + offset)


def drawo(x, y):
    """Draw O player centered, bigger and blue."""
    color('blue')  # Cambié color a azul
    pensize(5)     #Engrosar el trazo
    up()
    #Ajustar posición inicial para centrar el círculo en la casilla
    goto(x + 133/2, y + 20)
    down()
    circle(46)  #Cambié el radio del círculo para que quede centrado y más grande


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()