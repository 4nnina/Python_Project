import math
import turtle

def quadSierpinski(t, lato, livello):
    if livello == 0:
        t.begin_fill()
        for i in range(4):
            t.forward(lato)
            t.left(90)
        t.end_fill()
        return
    h_lato = lato/2
    angolo = math.degrees(math.atan(0.5))
    semi_d = h_lato / math.cos(math.radians(angolo))

    t.color('green')
    quadSierpinski(t, h_lato, livello - 1)
    t.penup()
    t.forward(h_lato)
    t.pendown()
    t.color('red')
    quadSierpinski(t, h_lato, livello - 1)
    t.penup()
    t.left(90 + angolo)
    t.forward(semi_d)
    t.right(90 + angolo)
    t.pendown()
    t.color('blue')
    quadSierpinski(t, h_lato, livello - 1)
    t.penup()
    t.right(90 + angolo)
    t.forward(semi_d)
    t.left(90 + angolo)
    t.pendown()
    return

'''
window = turtle.Screen()
t=turtle.Pen()
#t.hideturtle()
t.speed(10)
quadSierpinski(t,200,3)
window.exitonclick()
'''