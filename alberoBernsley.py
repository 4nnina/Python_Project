import turtle


def alberoBernRec(t1, dim, angolo, livello, livelloInizio):
    if livelloInizio == livello:
        t1.left(90)
        t1.fd(dim * 1.25)
    t2 = t1.clone()
    t1.left(angolo / 2)
    t1.fd(dim)
    t2.right(angolo / 2)
    t2.fd(dim)
    if livello == 0:
        return
    alberoBernRec(t1, dim / 2, angolo, livello - 1, livelloInizio)
    alberoBernRec(t2, dim / 2, angolo, livello - 1, livelloInizio)


def alberoBern(t, dim, angolo, livello):
    t.hideturtle()
    alberoBernRec(t, dim, angolo, livello, livello)
    return


if __name__ == "__main__":
    window = turtle.Screen()

    t = turtle.Pen()
    t.hideturtle()

    alberoBern(t, 80, 100, 1)
    ts = turtle.getscreen()

    window.exitonclick()
