from alberoBernsley import alberoBern
from alberoPitagora import alberoPitagora
from triSierpinski import triSierpinski
from quadSierpinski import quadSierpinski
from stellaKoch import stellaKochParam
from stellaQuad import stellaQuadParam

import turtle


def clearPenScreen(w, t):
    w.clear()
    t.reset()
    return


def allFun():
    window = turtle.Screen()
    t = turtle.Pen()

    # albero di Bernsley
    alberoBern(t, 80, 100, 5)
    clearPenScreen(window, t)

    # albero di Pitagora
    alberoPitagora(t, 50, 30, 6)
    clearPenScreen(window, t)

    # triangolo di Sierpinsky
    t.speed(100)
    triSierpinski(t, 250, 4)
    clearPenScreen(window, t)

    # sierpinsky con forma base il rettangolo
    t.speed(100)
    quadSierpinski(t, 200, 3)
    clearPenScreen(window, t)

    # stella di Koch prametrica
    t.speed(100)
    stellaKochParam(t, 50, 2, 10)
    clearPenScreen(window, t)

    # stella di Koch con il quadrato
    t.speed(100)
    stellaQuadParam(t, 50, 2, 5)

    window.exitonclick()


def oneFun():
    window = turtle.Screen()
    t = turtle.Pen()

    t.speed(5)
    stellaQuadParam(t, 50, 2, 5)

    window.exitonclick()


if __name__ == "__main__":
    # oneFun()
    allFun()
