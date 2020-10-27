#A00829207 Isaac Alejandro Enriquez Trejo
#A00827133 Andrea Fernanda Molina Blandon
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
        #Genera una nueva localizacion random para la comida
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #Este ciclo pinta los recuadros de la serpiente con el color inicial
    for body in snake:
        square(body.x, body.y, 9, 'black')
        
    #Esta linea le da el color a la comida
    square(food.x, food.y, 9, 'green')
    
    update()
    ontimer(move, 100)

#Esta función mueve la comida de forma
#aleatoria dentro de los bordes del juego
def move_food():
    
    
    food_direction = randrange(8) #Se genera un número al azar del 0 al 7
    #La comida se mueve de 10 en 10 porque es lo que mide el cuadrado
    #Este primer if lo mueve a la derecha
    if food_direction == 1 and food.x < 180:
        food.x += 10
    #Si sale dos se mueve arriba
    elif food_direction == 2 and food.y < 180:
        food.y += 10
    #Si sale tres se mueve a la izquierda
    elif food_direction == 3 and food.x > -190:
        food.x -= 10
    #Si sale cuatro se mueve abajo
    elif food_direction == 4 and food.y > -190:
        food.y -= 10
    #Este if lo mueve arriba a la derecha
    elif food_direction == 5 and food.x < 180 and food.y < 180:
        food.x += 10
        food.y += 10
    #Si sale 6 se mueve arriba a la izquierda
    elif food_direction == 6 and food.x > -190 and food.y < 180:
        food.x -= 10
        food.y += 10
    #Con el 7 se mueve abajo a la derecha
    elif food_direction == 7 and food.x < 180 and food.y > -190:
        food.x += 10
        food.y -= 10
    #Si da cero se moverá abajo a la izquieda
    elif food_direction == 0 and food.x > -190 and food.y > -190:
        food.x -= 10
        food.y -= 10
    
    #La comida se mueve cada 600 ticks, lo cual hace que sea un
    #poco más lenta que la serpiente, la cual se mueve cada 100
    ontimer(move_food, 600)
   
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
move_food()
done()