import turtle

def spezzataQuad(t, lato, livello):
    if livello == 0:
        t.forward(lato)
    else:
        spezzataQuad(t, lato / 3, livello - 1)
        t.right(90)
        spezzataQuad(t, lato / 3, livello - 1)
        t.left(90)
        spezzataQuad(t, lato / 3, livello - 1)
        t.left(90)
        spezzataQuad(t, lato / 3, livello - 1)
        t.right(90)
        spezzataQuad(t, lato / 3, livello - 1)
    return

def stellaQuadParam(t, lato, livello, n_lati):
    for i in range(0,n_lati):
        spezzataQuad(t, lato, livello)
        t.left(2*180/n_lati)
    return

if __name__ == "__main__":
    window = turtle.Screen()
    t = turtle.Pen()
    t.hideturtle()
    t.speed(100)
    #stellaQuad(t, 200, 2)
    stellaQuadParam(t, 50, 2, 5)
    window.exitonclick()
