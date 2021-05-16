import turtle

def spezzata(t, lato, livello):
    if livello == 0:
        t.forward(lato)
    else:
        spezzata(t, lato / 3, livello - 1)
        t.right(60)
        spezzata(t, lato / 3, livello - 1)
        t.left(120)
        spezzata(t, lato / 3, livello - 1)
        t.right(60)
        spezzata(t, lato / 3, livello - 1)
    return

def stellaTri(t, lato, livello):
    for i in range(0,3):
        spezzata(t, lato, livello)
        t.left(120)
    return

def stellaEsa(t, lato, livello):
    for i in range(0,6):
        spezzata(t, lato, livello)
        t.left(60)
    return

def stellaKochParam(t, lato, livello, n_lati):
    for i in range(0,n_lati):
        spezzata(t, lato, livello)
        t.left(2*180/n_lati)
    return

if __name__ == "__main__":
    window = turtle.Screen()
    t = turtle.Pen()
    t.hideturtle()
    t.speed(100)
    #stellaTri(t, 100, 0)
    #stellaEsa(t, 100, 1)
    stellaKochParam(t, 50, 2, 3)
    window.exitonclick()
