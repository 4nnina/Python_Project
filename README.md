# LINGUAGGIO DI PROGRAMMAZIONE PYTHON 
Questo è il progetto finale del corso "Linguaggi di programmazione Python" dell'Università di Verona, svolto durante l'ultimo anno della laurea in Informatica.
E\' un programma che disegna delle curve matematiche utilizzando la ricorsione. E\' stata utilizzata la libreria Turtle di Python. Quanto segue è la documentazione presentata in esame.


**PROGETTO**: Curve

**AUTORE**:   Anna Dalla Vecchia 

Il progetto è stato suddiviso in più file, ogni file contiene le funzioni per la costruzione di una specifica curva.
Per poter avviare l'intero progetto occorre eseguire il file main.py.

All'avvio, nel terminale, apparirà il menù riportato di seguito in cui è richiesto l'inserimento di una scelta per proseguire:

```
*********************MENU' PRINCIPALE*********************
Cosa si vuole eseguire?
1. Tutte le curve
2. Solo una curva a scelta per volta
3. Esci
Scelta:
```

**1** : viene chiamata una funzione `allFun()` che inizia il disegno di tutte le curve implementate senza la possibilità di inserire parametri a proprio piacimento e senza la possibilità di salvataggio delle immagini disegnate.

**2** : viene chiamata la funzione `oneFun()`, questa attraverso un nuovo menù permette di scegliere quale curva visualizzare andando ad inserire a piacere alcuni parametri (ad es: dimensione del lato, numero di livelli di ricorsione, forma della figura di base, angolo del triangolo rettangolo).
Al termine del disegno viene chiesto se si vuole salvare l'immagine e, in caso affermativo, il nome del file di output (basta inserire il nome, l'estensione .png sarà inserita automaticamente).
Per poter proseguire è richiesto un click sulla finestra di dialogo, viene quindi chiesto se si vuole proseguire con la visualizzazione di una nuova immagine (verrà nuovamente visualizzato il menù) o se si vuole uscire (ritorno al menù principale).

```
Funzioni disponibili:
1. Albero di Bernsley
2. Albero di Pitagora
3. Figura con curva di Koch
4. Figura con curva di Koch modificata (quadrato invece di trinagolo)
5. Triangolo di Sierpinski
6. Tringolo di Sierpinski con quadrati
7. Torna al menù principale
Scelta:
```

**3** : il programma verrà chiuso senza messaggi di errore

Si noti che per entrambe le scelte dei menù è stato implementato un semplice controllo della scelta, per evitare spiacevoli casi di loop infiniti o terminazioni improvvise.

------

#### Descrizione scelta 2 del *MENU' PRINCIPALE*

###### Parte comune a tutte le scelte:

All'utente verrà chiesto:

1. `Lunghezza lato:`  --> lunghezza del lato di partenza
2. `Numero livelli (livello base = 0):` --> numeri di livelli di ricorsione
3. ... eventuali altre scelte illustrate di seguito

Alla completamento del disegno della curva 

`Si vuole salvare l'immagine?(S/N)` 

​	se **s/S**  `Inserire il nome del file in cui si vuole salvare` --> inserire il nome del file in output

Cliccare quindi sullo screen di Turtle, come da indicazioni del terminale

`Si vuole visualizzare un'altra figura?(S/N)`

​	se **s/S** verrà visualizzato nuovamente il menù Funzioni disponibili

​	se **n/N** si ritorna la MENU' PRINCIPALE

##### 1.Albero di Bernsley

1. `Angolo tra i due rami:` --> l'ampiezza dell'angolo tra i due rami in gradi

###### alberoBernsley.py

Alla prima chiamata della funzione `alberoBernRec(...)` viene disegnata una linea verticale e due linee oblique che vanno a formare l'angolo passato come argomento; per tutte le altre chiamate, ad eccezione dell'ultima, vengono disegnate solo le linee oblique, ovvero i rami.

##### 2.Albero di Pitagora

1. `Angolo tra uno cateto e l'ipotenusa:` --> si dà la possibilità di scelta dell'angolo del triangolo rettangolo

###### alberoPitagora.py

La funzione `alberoPitagora(...)` è solo una funzione in preparazione al disegno, la ricorsione avviene con la funzione `triQuad(...)` che disegna il quadrato e sul lato superiore poggia l'ipotenusa del triangolo rettangolo, i cateti del triangolo saranno la nuova base dei quadrati del livello successivo.
Si noti che a livello zero la penna è verde (per richiamare le foglie) invece per tutto il resto del disegno essa è marrone.

##### 3.Figura con curva di Koch

1. `Numero di lati del poligono di base:` --> si da la possibilità di scegliere il numero di lati della figura di partenza, se il livello base inserito sarà 0 verrà visualizzato il poligono con il numero di lati inserito, se il livello di ricorsione inserito sarà >=1 verrà effettivamente utilizzata la curva di Koch.

###### stellaKoch.py

La funzione chiamata dal main è `stellaKochParam()` nata a seguito dell'idea di estendere la curva vista a lezione basata sul triangolo.

##### 4.Figura con curva di Koch modificata (quadrato invece di triangolo)

###### stellaQuad.py

Come per la scelta 3, l'unica differenza è la curva di base: 
per la scelta 3 la curva sarà la seguente _ / \ _
per la scelta 4 la curva invece sarà _ |-| _ 

##### 5.Triangolo di Sierpinski

###### triSierpinsky.py

Questa figura è basata sulla ricorsione a partire da dei triangoli.
L'idea per l'implementazione è stata di disegnare triangolo a sinistra, triangolo a destra, triangolo in alto per poi riportare la penna in basso a sinistra. Al livello 0 verrà disegnato un triangolo.

##### 6.Triangolo di Sierpinski con quadrati

###### quadSierpinsky.py

Come per scelta 5 ma la figura di base è un quadrato.

------

## Il main

Il main, come descritto sopra, oltre alla gestione dei menù di scelta si occupa anche del salvataggio di immagini, gestione dello schermo Turtle e della penna anche grazie a delle funzioni di supporto.

###### clearPenScreen(w,t)

Questa funzione permette il reset della penna e dello screen tra il disegno di una curva e l'altra nell'esecuzione di `allFun()` (scelta 1 del menù principale). Essendo che la penna e lo screen per tutti i disegni sono gli stessi è necessario:

1. pulire lo screen alla fine del disegno altrimenti ci sarebbe la sovrapposizione delle varie curve
2. reimpostare la penna come se fosse appena creata, se così non fosse si manterrebbe la velocità di disegno, il colore e la posizione nello screen che aveva alla fine della curva precedente. Il disagio più evidente ad occhio umano sarebbe l'inizio della curva nel punto in cui si era conclusa la curva precedente, che solitamente non corrisponde al centro dello screen.

###### inizializeTrutle()

Questa funzione restituisce la penna e lo screen pronti per il disegno di una nuova curva.

###### saveImage()

Questa funzione permette il salvataggio dello screen di Turtle in un'immagine in formato .png .
`turtle.getscreen().getcanvas().postscript(...)` permette il salvataggio dello screen in formato .eps , essendo un formato poco "user friendly"  per l'utente medio ho deciso di servirmi del pacchetto `Image` di `Pillow`  per la conversione da .eps a .png.
Questa parte del progetto ha richiesto l'installazione di https://ghostscript.com/download/gsdnld.html

Siti che ho consultato per l'implementazione di questa funzione:

1. https://stackoverflow.com/questions/4071633/python-turtle-module-saving-an-image

2. https://www.reddit.com/r/learnpython/comments/7wwtj5/saving_turtle_graphics_output_as_png_or_jgp/

   

**Nota**: nella funzione `oneFun()` si può notare una particolare riga di codice (126) `turtle.TurtleScreen._RUNNING = True` , essa è necessaria dopo `turtle.exitonclick()` in quanto, se assente, non sarebbe possibile utilizzare la funzione `inizializeTrutle()`  perché verrebbero rimossi dalla memoria degli oggetti di cui *Turtle* ha bisogno per funzionare, quindi non sarebbe in grado di restituire l'istanza della penna e dello screen andando in errore.  (https://stackoverflow.com/questions/41548813/using-turtle-module-exitonclick)



Per l'utilizzo di Turtle ho consultato la seguente documentazione	https://docs.python.org/3/library/turtle.html
