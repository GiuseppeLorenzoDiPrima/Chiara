# Esercizio 1.6 Spostamenti casuali

# Stampa esercizio
print("\nEsercizio 1.6 Spostamenti casuali\n")

import turtle
import random

dimensione_spostamento = 5 # Imposto lo spostamento a 5 pixel

def muovi(movimenti):
    for _ in range(movimenti):
        turtle.forward(dimensione_spostamento)  # Mi muovo di 5 pixel
        angolo = random.randint(-30, 30)  # restituisco un angolo casuale compreso tra -30° e 30°
        turtle.right(angolo)  # Ruoto dell'angolo randomico calcolato

# Inserimento numero di mosse
numero_movimenti = int(input("Inserisci il numero di movimenti che verranno svolti dalla tartaruga: "))

turtle.speed(3) # Imposto la velocità di disegno ad 3
turtle.pensize(3) # Imposto lo spessore del tratto ad 3
turtle.pencolor("red") # Imposto il colore a rosso
turtle.showturtle # Mostro la tartaruga durante il disegno

# Eseguo le mosse
muovi(numero_movimenti)

# Concludo il disegno
turtle.done()
