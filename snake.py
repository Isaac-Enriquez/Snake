from turtle import *
from random import randrange
from freegames import square, vector

#Estas lineas inicializan la comida, la serpiente y su dirección
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Esa función toma una dirección en 'x' y 'y'
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#Esta función revisa si la cabeza de la
#serpiente está dentro del recuadro inicial.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Esta función sirve para mover a la serpiente
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    #Esta condición hace que si la serpiente se sale
    #o si se choca con ella misma el juego se pierda
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Esta condición es para hacer que la serpiente
    #crezca cada vez que se choque con la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

#Se inicializa el canvas inicial y se esconde la tortuga
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen() #Este comando lee todas las teclas que se presionan
#Este bloque cambia la dirección de la serpiente al presionar
#cualquiera de la teclas de las flechas direccionales
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()