from turtle import Screen, Turtle
import time

# Configuración de la pantalla
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

# Posiciones iniciales de la serpiente
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Crear la serpiente
snake = []
for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    snake.append(new_segment)

# Configuración de la dirección de la serpiente
direction = 'right'

# Funciones para cambiar la dirección
def go_up():
    global direction
    if direction != 'down':
        direction = 'up'

def go_down():
    global direction
    if direction != 'up':
        direction = 'down'

def go_left():
    global direction
    if direction != 'right':
        direction = 'left'

def go_right():
    global direction
    if direction != 'left':
        direction = 'right'

# Controles del teclado
screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')

# Lógica del juego
game = True
while game:
    screen.update()
    time.sleep(0.1)

    # Mover la serpiente
    for seg in range(len(snake) - 1, 0, -1):
        new_x = snake[seg - 1].xcor()
        new_y = snake[seg - 1].ycor()
        snake[seg].goto(new_x, new_y)

    # Mover la cabeza de la serpiente
    if direction == 'up':
        y = snake[0].ycor()
        snake[0].sety(y + 20)
    if direction == 'down':
        y = snake[0].ycor()
        snake[0].sety(y - 20)
    if direction == 'left':
        x = snake[0].xcor()
        snake[0].setx(x - 20)
    if direction == 'right':
        x = snake[0].xcor()
        snake[0].setx(x + 20)

screen.exitonclick()
