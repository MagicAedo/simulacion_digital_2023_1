# Implemente una simulación en 2D en la cual se tiene una pelota
# (representada por un punto) que se puede lanzar con una velocidad v0
# desde una posición inicial (x0, y0). La pelota se encuentra encerrada en
# una región rectangular, tal como se muestra en la figura. Ajuste su
# programa para que, al inicio de la simulación, el usuario pueda dar las
# coordenadas iniciales y la velocidad inicial en x,y (V0x, V0y). Asuma que se
# tienen paredes que absorben energía de tal forma que la componente
# normal a la superficie pierde un 10% de velocidad.

import turtle
import time
import numpy as np 

# Configuración de la ventana
ventana = turtle.Screen()
ventana.bgcolor("white")
ventana.title("Simulación de una pelota en una caja")
ventana.setup(width=600, height=600)
ventana.tracer(0)


# Altura inicial
h = 30
# posicion inicial
x0 = 200


# Configuración de la pelota
pelota = turtle.Turtle()
pelota.shape("circle")
# por defecto el diametro del circulo es 20px acá vamos a usar 10px 
pelota.shapesize(0.5)
pelota.color("red")
pelota.penup()
pelota.speed(0)
#punto de partida del circulo
pelota.goto(x0,h)

# Configuración de la caja
caja = turtle.Turtle()
caja.penup()
caja.setposition(250, 250)
caja.pendown()
caja.pensize(3)
for i in range(2):
    caja.right(90)
    caja.forward(250)
    caja.right(90)
    caja.forward(500)
caja.hideturtle()


#Gravedad modificable 
g = 9.8
#constante en que va decreciendo la energia despues de una colisión
c = 0.9
#tiempo
t = 0
#razon en que crece el tiempo
dt = 0.01


# altura inicial
y0 = h

#velocidad inicial en x
vx0 = -30
#velocidad inicial en y (como es en caida libre es 0)
vy0 = 0

# Bucle principal de la simulación
while True:

    x = x0 + vx0*t
    y = y0 + vy0*t - 0.5*g*t**2
    vx = vx0
    #Se va guardando la velocidad en cada punto en caso de que haya una colisión (y=0)
    vy = vy0 - g*t
    #se setea la posicion de la pelota
    pelota.setposition(x, y)
    print(x, y,vx, 't = ', t, ' s')

    #si choca con el piso o paredes dan las siguientes condiciones

    if pelota.ycor() <= 5: 
        #vy y vx ahora pierde energia por lo tanto tambien velocidad con dirección contraria
        vy = -np.sqrt(c)*vy
        vx = np.sqrt(c)*vx
        vx0 = vx
        vy0 = vy
        #y0 ahora su nueva posicion inicial es 5 (En realidad deberia ser 0 pero para fines de visualizacion se opto por 5)
        y0 = 5
        x0 = x
        #Es un nuevo sistema que ahora se va a estudiar, despues de la colisión el t debe ser 0
        t= 0

    if pelota.xcor() >= 245:
        vy = 0 
        vx = -np.sqrt(c)*vx 
        vx0 = vx 
        vy0 = vy
        y0 = y
        x0 = 245
        t = 0 
    
    if pelota.xcor() <= -245:
        vy = 0 
        vx = -np.sqrt(c)*vx 
        vx0 = vx 
        vy0 = vy
        y0 = y
        x0 = -245
        t = 0 
    
    t = t+dt
    ventana.update()
    #Descomentar la instrucción de abajo para ver la ejecucion en tiempo real
    #time.sleep(0.01)
