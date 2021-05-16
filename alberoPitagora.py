import turtle
import math

def triQuad(t, lato, angolo, livello):
    if livello == 0:
        t.color('green')
    else:
        t.color('brown')

    c1 = lato*math.cos(math.radians(angolo))
    c2 = lato*math.sin(math.radians(angolo))
    #costruisco a partire "dal lato destro"
    t.left(90)
    t.forward(lato)

    #rami del cateto 1
    if livello > 0:
        C1 = t.clone()
        C1.right(90 + angolo)
        triQuad(C1, c1, angolo, livello - 1) #da cateto 1
    t.left(90 - angolo)
    t.forward(c1)

    #rami del cateto 2
    if livello > 0:
        C2 = t.clone()
        C2.right(90)
        triQuad(C2, c2, angolo, livello - 1) #da cateto 2
    t.left(90)
    t.forward(c2)

    #finisco il disegno del quadrato
    t.left(90+angolo)
    t.forward(lato)
    t.pen()
    t.backward(lato)
    t.pendown()
    t.right(90)
    t.forward(lato)
    return

def alberoPitagora(t,lato, angolo, livelli):
    t.speed(50)
    t.hideturtle()
    t.color('brown')
    t.forward(lato)
    triQuad(t, lato, angolo, livelli)
    return

if __name__ == "__main__":
    window = turtle.Screen()
    t = turtle.Pen()

    alberoPitagora(t,50,30,6)
    window.exitonclick()

