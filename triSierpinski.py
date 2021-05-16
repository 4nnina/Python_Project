import turtle

def triSierpinski(t, lato, livello):
    if livello == 0:
        t.begin_fill()
        for i in range(3):
            t.forward(lato)
            t.left(120)
        t.end_fill()
        return
    h_lato = lato/2
    #t.color('red')
    triSierpinski(t, h_lato, livello - 1)
    t.penup()
    t.forward(h_lato)
    t.pendown()
    #t.color('green')
    triSierpinski(t, h_lato, livello - 1)
    #t.color('black')
    t.penup()
    t.left(120)
    t.forward(h_lato)
    t.right(120)
    t.pendown()
    #t.color('blue')
    triSierpinski(t, h_lato, livello - 1)
    #t.color('yellow')
    t.penup()
    t.right(120)
    t.forward(h_lato)
    t.left(120)
    t.pendown()
    return


if __name__ == "__main__":
    window = turtle.Screen()
    t=turtle.Pen()
    #t.hideturtle()
    t.speed(5)
    triSierpinski(t,250,4)
    window.exitonclick()
