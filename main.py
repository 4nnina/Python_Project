#https://www.reddit.com/r/learnpython/comments/7wwtj5/saving_turtle_graphics_output_as_png_or_jgp/
import io
import turtle
from PIL import Image

from alberoBernsley import alberoBern
from alberoPitagora import alberoPitagora
from triSierpinski import triSierpinski
from quadSierpinski import quadSierpinski
from stellaKoch import stellaKochParam
from stellaQuad import stellaQuadParam


def clearPenScreen(w, t):
    w.clear()
    t.reset()
    return


def inizializeTrutle():
    p = turtle.Pen()
    w = turtle.Screen()
    return p, w


def allFun():
    pen, window = inizializeTrutle()

    # albero di Bernsley
    pen.speed(50)
    alberoBern(pen, 80, 100, 5)
    clearPenScreen(window, pen)

    # albero di Pitagora
    pen.speed(100)
    alberoPitagora(pen, 50, 30, 6)
    clearPenScreen(window, pen)

    # triangolo di Sierpinsky
    pen.speed(100)
    triSierpinski(pen, 250, 4)
    clearPenScreen(window, pen)

    # sierpinsky con forma base il rettangolo
    pen.speed(100)
    quadSierpinski(pen, 200, 3)
    clearPenScreen(window, pen)

    # stella di Koch prametrica
    pen.speed(100)
    stellaKochParam(pen, 50, 2, 10)
    clearPenScreen(window, pen)

    # stella di Koch con il quadrato
    pen.speed(100)
    stellaQuadParam(pen, 50, 2, 5)

    print('\nPer terminare cliccare sulla finestra')
    window.exitonclick()
    turtle.TurtleScreen._RUNNING = True
    return


def oneFun():
    while True:
        while True:
            print('\nFunzioni disponibili:')
            print('1. Albero di Bernsley\n2. Albero di Pitagora\n3. Figura con curva di Koch')
            print('4. Figura con curva di Koch modificata (quadrato invece di trinagolo)\n5. Triangolo di Sierpinski\n'
                  '6. Tringolo di Sierpinski con quadrati\n7. Torna al menù principale')
            sc = int(input('Scleta: \t'))
            if sc > 0 and sc <= 7:
                break
            else:
                print('\nE\' stato inserito un valore non valido (1, 2, 3, 4, 5, 6)')

        if sc != 7:
            dim = int(input('Lunghezza lato:\t'))
            livelli = int(input('Numero livelli (livello base = 0):\t'))

        if sc == 1:
            angolo = int(input('Angolo tra i due rami:\t'))
            pen, window = inizializeTrutle()
            alberoBern(pen, dim, angolo, livelli)
        elif sc == 2:
            angolo = int(input('Angolo tra uno cateto e l\'ipotenusa:\t'))
            pen, window = inizializeTrutle()
            alberoPitagora(pen, dim, angolo, livelli)
        elif sc == 3:
            lati = int(input('Numero di lati del poligono di base:\t'))
            pen, window = inizializeTrutle()
            stellaKochParam(pen, dim, livelli, lati)
        elif sc == 4:
            lati = int(input('Numero di lati del poligono di base:\t'))
            pen, window = inizializeTrutle()
            stellaQuadParam(pen, dim, livelli, lati)
        elif sc == 5:
            pen, window = inizializeTrutle()
            triSierpinski(pen, dim, livelli)
        elif sc == 6:
            pen, window = inizializeTrutle()
            quadSierpinski(pen, dim, livelli)
        else:
            return

        saveimg = input('\nSi vuole salvare l\'immagine?(S/N)\t')
        if saveimg.lower() == 's':
            filename = input('Inserire il nome del file in cui si vuole salvare\t') + '.png'
            ps = turtle.getscreen().getcanvas().postscript(colormode="color")
            im = Image.open(io.BytesIO(ps.encode("utf-8")))
            im.save(filename, lossless = True)
            #ts = turtle.getscreen()
            #ts.getcanvas().postscript(file='out.eps')
            #convertire in png
            #im = Image.open('out.eps')
            #fig = im.convert('RGBA')
            #fig.save('testImg.png', lossless = True)
            print('... Salvataggio completato')

        print('\nPer terminare cliccare sulla finestra')
        window.exitonclick()
        turtle.TurtleScreen._RUNNING = True

        finito = input('Si vuole visualizzare un\'altra figura?(S/N)\t')
        if finito.lower() == 'n':
            return
    return


def main():
    while True:
        print('\n*********************MENU\' PRINCIPALE*********************')
        print('Cosa si vuole eseguire?')
        print('1. Tutte le curve\n2. Solo una curva a scelta per volta\n3. Esci')
        scelta = input('Scelta:\t')

        if scelta == '1':
            allFun()
        elif scelta == '2':
            oneFun()
        elif scelta == '3':
            break
        else:
            print('\nE\' stato inserito un valore non valido, inserirne uno valido\n')
    return


if __name__ == "__main__":
    main()
